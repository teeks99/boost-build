import tool_versions

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

class Runner(object):
    def __init__(self, machine_vars, cleanup=False):
        self.mvs = machine_vars
        self.runs = self.mvs['runs']
        self.cleanup = False
        self.start_dir = os.getcwd()
        self.current_run = None
        self.sys_tmpdir = tempfile.gettempdir()

    @property
    def multi_run_log(self):
        log_dir = os.path.join(self.start_dir, 'logs')
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        return os.path.join(log_dir, 'all_runs.log')

    def copy_repo(self, origin="../boost_root"):
        repo_name = "boost_root"
        print("copying repo " + origin + " to " + repo_name)
        #shutil.rmtree(repo_name)
        win_rmtree(repo_name)
        shutil.copytree(origin, repo_name)

    def update_base_repo(self, branch):
        orig_dir = os.getcwd()
        try:
            print('cd boost_root')
            os.chdir('boost_root')

            print('git checkout' + branch)
            os.system('git checkout ' + branch)
            print('git pull')
            os.system('git pull')
            print('git submodule init')
            os.system('git submodule init')
            print('git submodule update')
            os.system('git submodule update')

        finally:
            os.chdir(orig_dir)

    def clean_and_make_tmp(self):
        self.tmpdir = self.sys_tmpdir
        if 'tmpdir' in self.mvs:
            self.tmpdir = self.mvs['tmpdir']
        else:
            self.tmpdir = os.path.join(self.tmpdir, "boost_regression")

        if os.path.exists(self.tmpdir):
            if os.name == 'nt':
                win_rmtree(self.tmpdir)
            else:
                shutil.rmtree(self.tmpdir)
        os.makedirs(self.tmpdir)

        os.environ['TMPDIR'] = self.tmpdir
        os.environ['TMP'] = self.tmpdir
        os.environ['TEMP'] = self.tmpdir

    def branch(self):
        return self.runs[self.current_run]['type']

    def run_one(self):
        run = self.runs[self.current_run]

        print('')
        print('')
        print('Starting run: ' + run['dir'])
        print('')
        self.log_start()

        f = open("CurrentRun.json",'w')
        s = json.dump(self.current_run, f)
        f.close()

        self.clean_and_make_tmp()
        self.update_base_repo(self.branch())

        run_dir = 'run'
        win_rmtree(run_dir)
        os.mkdir(run_dir)
        os.chdir(run_dir)

        self.make_info()

        self.copy_repo()
        shutil.copy2('../run.py', './')

        other_options = ''
        if 'other_options' in run:
            other_options = ' ' + run['other_options']

        command = ['python', 'run.py', '--runner=' + self.mvs['machine'] +
            run['dir'] + '-' + self.mvs['os'] + '-' + run['arch'] + "on" +
            self.mvs['os_arch'], '--toolsets=' +
            run['compilers'], '--bjam-options=-j' + str(self.mvs['procs']) +
            ' address-model=' + run['arch'] + ' --abbreviate-paths' +
            ' --remove-test-targets' + other_options, '--comment=info.html',
            '--tag=' + self.branch()]

        # Output the command to the screen before running it            
        cmd_str = ""
        for s in command:
            cmd_str += " " + s
        print('Runing command:')
        print(cmd_str[1:])
        print('')
        print('at: ' + datetime.datetime.utcnow().isoformat(' ') + ' UTC')
        print('')

        with open('../logs/' + run['dir'] + '-output.log', 'w') as log_file:
            log_file.write('Running command:\n:')
            log_file.write(cmd_str[1:])
            log_file.write('\n')
            log_file.write('at: ' + datetime.datetime.utcnow().isoformat(' ') + ' UTC')
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

        if self.cleanup:
            try:
                if os.path.isfile('results/bjam.log'):
                    shutil.copy2('results/bjam.log', '../logs/' + run['dir'] +
                                 '-results-bjam.log')
                win_rmtree('results')
                win_rmtree('boost_root')
                #rmtree on temp???
            except OSError:
                pass # dir wasn't there...may indicate previous failure

        self.log_end()
        os.chdir(self.start_dir)

    def loop(self, start_at=None):
        self.log_startup()
        sorted_runs = sorted(self.runs.keys())

        num = 0
        if start_at:
            # Jump to that run
            num = sorted_runs.index(start_at)
            start_at = None

        while True:
            if self.check_for_stop():
               print("Stopping runs because file: 'stop_runs.on' exists")
               break

            self.current_run = sorted_runs[num % len(sorted_runs)]
            self.run_one()
            num += 1

    def check_for_stop(self):
        if os.path.exists(self.start_dir + "/stop_runs.on"):
            return True

    def restart(self):
        start_at = "a"
        try:
            f = open("CurrentRun.json",'r')
            at = json.load(f)
            f.close
            if isinstance(at, basestring):
                start_at = at
        except IOError:
            pass #No file?

        self.loop(start_at)

    def log_startup(self):
        with open(self.multi_run_log, "a") as log:
            log.write("\nStarting Runs at: " +
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")

    def log_start(self):
        with open(self.multi_run_log, "a") as log:
            log.write("Run " + self.current_run + " started at: " +
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def log_end(self):
        with open(self.multi_run_log, "a") as log:
            log.write(" completed at: " +
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")

    def make_info(self):
        info_template = None
        with open('../info.html.template', 'r') as info_template_file:
            info_template = string.Template(info_template_file.read())

        mapping = {
            'machine': self.mvs['machine'],
            'runner': self.current_run,
            'setup': self.mvs['setup'],
            'ram': self.mvs['ram'],
            'cores': self.mvs['procs'],
            'arch': self.mvs['os_arch'],
            'os': self.mvs['os'],
            'user_config': tool_versions.user_config(),
            'site_config': tool_versions.site_config(),
            'compiler_versions': tool_versions.build_version_string(),
            'python_version': tool_versions.python_version(),
            'git_version': tool_versions.git_version()}

        info_str = info_template.substitute(mapping)

        with open('info.html', 'w') as info_file:
            info_file.write(info_str)


if __name__ == '__main__':
    f = open("machine_vars.json", 'r')
    machine_vars = json.load(f)
    f.close()

    r = Runner(machine_vars)
    if len(sys.argv) > 1:
        r.current_run = sys.argv[1]
        r.run_one()
    else:
        r.cleanup = True
        r.restart()
