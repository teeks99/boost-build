#!/bin/python

# This will perform a run of a single set of boost tests

import json
import os

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
        self.run_dir = os.join(self.start_dir, 'run')

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
        if 'tmpdir' in self.machine['machine']:
            self.tmpdir = self.machine['tmpdir']
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

    def process(self):
        pass


# For running standalone, typically in docker.
if __name__ == '__main__':
    run = Run(run_file='CurrentRun.json')
    run.process()

