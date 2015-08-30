import single

import shutil
import os
import sys
import json
import datetime

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
            run = single.Run(config=run_config, machine=self.machine)
            run.process()
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
