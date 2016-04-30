#!/bin/python

# This will perform a run of a single set of boost tests
import tool_versions

import shutil
import os
import subprocess
import sys
import json
import threading
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

class Run(object):
    def __init__(self, config=None, run_file='CurrentRun.json', machine=None,
                 machine_file='machine_vars.json'):
        if not config and run_file:
            with open(run_file, 'r') as f:
                config = json.load(f)
        if not machine and machine_file:
            with open(machine_file, 'r') as f:
                machine = json.load(f)

        self.config = config
        self.machine = machine
        self.start_dir = os.getcwd()
        self.run_dir = os.path.join(self.start_dir, 'run')


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

    def process(self):
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



# For running standalone, typically in docker.
if __name__ == '__main__':
    run = Run(run_file='CurrentRun.json')
    run.process()

