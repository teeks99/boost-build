import single

import shutil
import os
import sys
import json
import datetime
import time
import subprocess

PY3 = sys.version_info[0] == 3

if PY3:
    string_types = str
else:
    string_types = basestring

def win_rmtree(directory):
    if os.path.isdir(directory):
        os.system('rmdir /S /Q \"{}\"'.format(directory))
    passes = 1
    while os.path.isdir(directory):
        time.sleep(15.0)
        os.system('rmdir /S /Q \"{}\"'.format(directory))
        passes += 1
        if passes > 20:
            raise IOError("Could not delete windows directory: " + directory)

def my_rmtree(directory):
    if os.path.exists(directory):
        if os.name == 'nt':
            win_rmtree(directory)
        else:
            shutil.rmtree(directory)

class Runner(object):
    def __init__(self, machine_vars, cleanup=False):
        self.machine = machine_vars
        self._set_ids()
        self.runs = self.machine['runs']
        if 'run_order' in self.machine:
            self.run_order = self.machine['run_order']
        else:
            self.run_order = sorted(self.runs.keys())
        self.cleanup = False
        self.start_dir = os.getcwd()
        self.current_run_id = None
        self.docker_image_updates = {}

    def _set_ids(self):
        for key, val in self.machine['runs'].items():
            val["id"] = key

    def loop(self, start_at=0):
        self.log_startup()

        order_index = start_at

        while True:

            if self.check_for_stop():
               print("Stopping runs because file: 'stop_runs.on' exists")
               break

            order_index = self.run_one(order_index)

    def run_one(self, order_index):
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

        if not self.machine["source"] == single.NO_DOWNLOAD_SOURCE:
            self.update_base_repo(run_config['branch'])

        my_rmtree(run_dir)
        os.mkdir(run_dir)

        self.update_docker_img(run_config)

        self.write_run_config(run_config)
        self.log_start(run_config)
        if 'docker_img' in run_config:
            docker_cmd = 'docker run -v ' + os.getcwd()
            docker_cmd += ':/var/boost'
            if "docker_cpu_quota" in self.machine:
                docker_cmd += ' --cpu-quota '
                docker_cmd += str(self.machine['docker_cpu_quota'])
            docker_cmd += ' --rm -i -t '
            docker_cmd += run_config['docker_img']
            docker_cmd += ' /bin/bash /var/boost/inside.bash'
            print(docker_cmd)
            subprocess.call(docker_cmd, shell=True)
        else:
            run = single.Run(config=run_config, machine=self.machine)
            run.process()
        self.log_end()
        order_index += 1
        return order_index

    def update_docker_img(self, run_config):
        if 'docker_img' in run_config:
            img_name = run_config['docker_img']

            diu = self.docker_image_updates
            one_day = datetime.timedelta(days=1)
            if img_name in diu and \
                datetime.datetime.now() - diu[img_name] > one_day:

                subprocess.call('docker pull ' + img_name, shell=True)
                diu[img_name] = datetime.datetime.now()

            p = subprocess.Popen(
                'docker images ' + img_name
                + ' --format "{{.Repository}}:{{.Tag}} - {{.CreatedAt}} - '
                + '{{.ID}}" --no-trunc', stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, shell=True)
            out, err = p.communicate()
            run_config['docker_image_info'] = out

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
                      config['id'].ljust(12) + " - start: " +
                      config['start_time'])

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
            print('git submodule update -f --recursive --remote --init')
            os.system('git submodule update -f --recursive --remote --init')
            print('git clean -xfdf')
            os.system('git clean -xfdf')
        finally:
            os.chdir(orig_dir)


def add_external_runs(machine_vars):
    if isinstance(machine_vars['runs'], string_types):
        with open(machine_vars['runs'], 'r') as external_runs_file:
            external_runs = json.load(external_runs_file)
            machine_vars['runs'] = external_runs['runs']

def ensure_boost_root(source):
    if source == single.NO_DOWNLOAD_SOURCE:
        return

    if not os.path.exists("boost_root"):
        cmd = "git clone --recursive {} boost_root".format(source)
        print(cmd)
        subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    f = open("machine_vars.json", 'r')
    machine_vars = json.load(f)
    f.close()

    if not "source" in machine_vars:
        machine_vars["source"] = "https://github.com/boostorg/boost"
    ensure_boost_root(machine_vars["source"])

    add_external_runs(machine_vars)

    r = Runner(machine_vars)
    if len(sys.argv) > 1:
        run_id = sys.argv[1]
        r.run_one(run_id)
    else:
        r.cleanup = True
        r.restart()
