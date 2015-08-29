import tool_versions
import single

import shutil
import os
import subprocess
import sys
import json
import threading
import io
import datetime
import tempfile
import string

class StreamThread ( threading.Thread ):
    def __init__(self, source, sink1, sink2):
        threading.Thread.__init__(self)
        self.source = source
        self.sink1 = sink1
        self.sink2 = sink2

    def run ( self ):
        while 1:
            line = self.source.readline()
            if line == '':
                break
            self.sink1.write(line)
            self.sink1.flush()
            self.sink2.write(line)
            self.sink2.flush()

def win_rmtree(directory):
    if os.path.isdir(directory):
        os.system('rmdir /S /Q \"{}\"'.format(directory))
    if os.path.isdir(directory):
        os.system('rmdir /S /Q \"{}\"'.format(directory))

def my_rmtree(directory):
    if os.path.exists(directory):
        if os.name == 'nt':
            win_rmtree(directory)
        else:
            shutil.rmtree(directory)

class Runner(object):
    def __init__(self, machine_vars, cleanup=False):
        self.machine = machine_vars
        self.runs = self.machine['runs']
        if 'run_order' in self.machine:
            self.run_order = self.machine['run_order']
        else:
            self.run_order = sorted(self.runs.keys())
        self.cleanup = False
        self.start_dir = os.getcwd()
        self.current_run_id = None

    def copy_repo(self, origin="../boost_root"):
        repo_name = "boost_root"
        print("copying repo " + origin + " to " + repo_name)
        shutil.copytree(origin, repo_name)

    def clean_and_make_tmp(self):
        tmpdir = tempfile.gettempdir()
        if 'tmpdir' in self.machine:
            tmpdir = self.machine['tmpdir']
        else:
            tmpdir = os.path.join(tmpdir, "boost_regression")

        my_rmtree(tmpdir)
        os.makedirs(tmpdir)

        os.environ['TMPDIR'] = tmpdir
        os.environ['TMP'] = tmpdir
        os.environ['TEMP'] = tmpdir

    def make_info(self):
        info_template = None
        with open('../info.html.template', 'r') as info_template_file:
            info_template = string.Template(info_template_file.read())

        mapping = {
            'machine': self.machine['machine'],
            'runner': self.config['id'],
            'setup': self.machine['setup'],
            'ram': self.machine['ram'],
            'cores': self.machine['procs'],
            'arch': self.machine['os_arch'],
            'os': self.machine['os'],
            'user_config': tool_versions.user_config(),
            'site_config': tool_versions.site_config(),
            'compiler_versions': tool_versions.build_version_string(),
            'python_version': tool_versions.python_version(),
            'git_version': tool_versions.git_version()}

        info_str = info_template.substitute(mapping)

        with open('info.html', 'w') as info_file:
            info_file.write(info_str)

    def run_one(self):
        os.chdir(self.config['run_dir'])

        self.clean_and_make_tmp()
        self.make_info()

        self.copy_repo()
        shutil.copy2('../run.py', './')

        other_options = ''
        if 'other_options' in self.config:
            other_options = ' ' + self.config['other_options']

        command = ['python', 'run.py', '--runner=' + self.machine['machine'] +
            self.config['id'] + '-' + self.machine['os'] + '-' +
            self.config['arch'] + "on" + self.machine['os_arch'], '--toolsets=' +
            self.config['compilers'], '--bjam-options=-j' +
            str(self.machine['procs']) + ' address-model=' + self.config['arch'] +
            ' --abbreviate-paths' + ' --remove-test-targets' + other_options,
            '--comment=info.html', '--tag=' + self.config['branch']]

        # Output the command to the screen before running it            
        cmd_str = ""
        for s in command:
            cmd_str += " " + s
        print('Runing command:')
        print(cmd_str[1:])
        print('')
        print('at: ' + datetime.datetime.utcnow().isoformat(' ') + ' UTC')
        print('')

        with open('../logs/' + self.config['id'] + '-output.log', 'w') as \
                log_file:
            log_file.write('Running command:\n:')
            log_file.write(cmd_str[1:])
            log_file.write('\n')
            log_file.write(
                'at: ' + datetime.datetime.utcnow().isoformat(' ') + ' UTC')
            log_file.write('\n\n\n')

            proc = subprocess.Popen(command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
            stdoutThread = StreamThread(proc.stdout, sys.stdout, log_file)
            stderrThread = StreamThread(proc.stderr, sys.stderr, log_file)
            stdoutThread.start()
            stderrThread.start()
            proc.wait()
            stdoutThread.join()
            stderrThread.join()

        if os.path.isfile('results/bjam.log'):
            shutil.copy2('results/bjam.log', '../logs/' + self.config['id'] +
                         '-results-bjam.log')

        os.chdir(self.start_dir)

    def loop(self, start_at=0):
        self.log_startup()

        order_index = start_at

        while True:
            if self.check_for_stop():
               print("Stopping runs because file: 'stop_runs.on' exists")
               break

            if order_index >= len(self.run_order):
                order_index = 0

            self.current_run_id = self.run_order[order_index]
            run_dir = 'run'

            self.start_time = datetime.datetime.now()
            start_str = self.start_time.strftime('%m-%d %H:%M:%S')

            run_config = self.runs[self.current_run_id].copy()
            run_config['order_index'] = order_index
            run_config['start_time'] = start_str
            run_config['run_dir'] = run_dir

            self.update_base_repo(run_config['branch'])
            win_rmtree(run_dir)
            os.mkdir(run_dir)

            self.write_run_config(run_config)
            self.log_start(run_config)
            self.config = run_config
            self.run_one()
            #run = single.Run(config=run_config, machine=self.machine)
            #run.process()
            self.log_end()
            order_index += 1

    def check_for_stop(self):
        if os.path.exists(self.start_dir + "/stop_runs.on"):
            return True

    def restart(self):
        start_at = 0
        try:
            f = open("CurrentRun.json",'r')
            status = json.load(f)
            f.close
            start_at = status['order_index']
        except IOError:
            pass #No file?

        self.loop(start_at)

    def log_startup(self):
        with open(self.multi_run_log, "a") as log:
            log.write("\nStarting Runs at: " +
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")

    @property
    def multi_run_log(self):
        log_dir = os.path.join(self.start_dir, 'logs')
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        return os.path.join(log_dir, 'all_runs.log')

    def log_start(self, config):
        print('')
        print('')
        print('Starting run: ' + config['id'])
        print('')

        with open(self.multi_run_log, "a") as log:
            log.write("Run " + str(config['order_index']) + '-' +
                      config['id'] + " - start: " + config['start_time'])

    def write_run_config(self, config):
        with open("CurrentRun.json",'w') as status_file:
            json.dump(config, status_file)

    def log_end(self):
        end = datetime.datetime.now()
        end_str = end.strftime('%m-%d %H:%M:%S')
        duration_hrs = (end - self.start_time).total_seconds() / 3600.0
        duration_hrs_str = '%.2f' % duration_hrs
        with open(self.multi_run_log, "a") as log:
            log.write(" complete: " +
                datetime.datetime.now().strftime('%m-%d %H:%M:%S') + "in: " +
                duration_hrs_str + "hrs\n")

    def update_base_repo(self, branch):
        orig_dir = os.getcwd()
        try:
            print('cd boost_root')
            os.chdir('boost_root')

            print('git checkout ' + branch)
            os.system('git checkout ' + branch)
            print('git pull')
            os.system('git pull')
            print('git submodule init')
            os.system('git submodule init')
            print('git submodule update')
            os.system('git submodule update')

        finally:
            os.chdir(orig_dir)


if __name__ == '__main__':
    f = open("machine_vars.json", 'r')
    machine_vars = json.load(f)
    f.close()

    r = Runner(machine_vars)
    if len(sys.argv) > 1:
        r.current_run_id = sys.argv[1]
        r.run_one(r.runs[r.current_run_id])
    else:
        r.cleanup = True
        r.restart()
