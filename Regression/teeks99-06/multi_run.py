import shutil
import os
import subprocess
import sys
import json
import tee
import threading
import io
import datetime
import tempfile

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
        self.multi_run_log = "../all_runs.log"
        self.sys_tmpdir = tempfile.gettempdir()

    def copy_repo(self, origin="../boost_root"):
        repo_name = "boost_root"
        print("copying repo " + origin + " to " + repo_name)
        #shutil.rmtree(repo_name)
        win_rmtree(repo_name)
        shutil.copytree(origin, repo_name)

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

    def run_one(self):
        f = open("CurrentRun.json",'w')
        s = json.dump(self.current_run, f)
        f.close()
        
        run = self.runs[self.current_run]

        self.clean_and_make_tmp()
    
        os.chdir(run['dir'])
        print('')
        print('')
        print('Starting run: ' + run['dir'])
        print('')
        self.log_start()
        self.copy_repo()

        other_options = ''
        if 'other_options' in run:
            other_options = ' ' + run['other_options']
        
        command = ['python', 'run.py', '--runner=' + self.mvs['machine'] + 
            run['dir'] + '-' + self.mvs['os'] + '-' + run['arch'] + "on" + 
            self.mvs['os_arch'], '--toolsets=' + 
            run['compilers'], '--bjam-options=-j' + str(self.mvs['procs']) + 
            ' address-model=' + run['arch'] + ' --abbreviate-paths' +
            ' --remove-test-targets' + other_options, '--comment=..\info.html']

        if run['type'] == 'release' or run['type'] == 'branches/release':
            command.append('--tag=master')
        else: # type == develop or no type
            command.append('--tag=develop')

        # Output the command to the screen before running it            
        cmd_str = ""
        for s in command:
            cmd_str += " " + s
        print('Runing command:')     
        print(cmd_str[1:])       
        print('')
        print('at: ' + datetime.datetime.utcnow().isoformat(' ') + ' UTC')
        print('')

        with open('output.log', 'w') as log_file:
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
                    shutil.copy2('results/bjam.log', 'results-bjam.log')
                win_rmtree('results')
                win_rmtree('boost_root')
                #rmtree on temp???
            except OSError:
                pass # dir wasn't there...may indicate previous failure
        
        self.log_end()     
        os.chdir(self.start_dir)
        
    def loop(self, start_at=None):
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

    def log_start(self):
        with open(self.multi_run_log, "a") as log:
            log.write("Run " + self.current_run + " started at: " + 
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def log_end(self):
        with open(self.multi_run_log, "a") as log:
            log.write(" completed at: " + 
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")

    def update_base_repo(self):
        print("updating base repo")
        os.chdir('boost_root')
        subprocess.Popen(['git', 'checkout', 'master']).wait()
        subprocess.Popen(['git', 'pull']).wait()
        subprocess.Popen(['git', 'submodule', 'update']).wait()
        subprocess.Popen(['git', 'checkout', 'develop']).wait()
        subprocess.Popen(['git', 'pull']).wait()
        subprocess.Popen(['git', 'submodule', 'update']).wait()        
        os.chdir('..')

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
