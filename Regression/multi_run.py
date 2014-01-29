import shutil
import os
import subprocess
import sys
import json
import tee

class Runner(object):
    def __init__(self, machine_vars, cleanup=False):
        self.mvs = machine_vars
        self.runs = self.mvs['runs']
        self.cleanup = False
        self.start_dir = os.getcwd()

    def run_one(self, run_str):
        f = open("CurrentRun.json",'w')
        s = json.dump(run_str, f)
        f.close()
        
        run = self.runs[run_str]
    
        os.chdir(run["dir"])
        print ""
        print ""
        print "Starting run: " + run["dir"]
        print ""
        
        command = ['python', 'run.py', '--runner=' + self.mvs['machine'] + 
            run['dir'] + '-' + self.mvs['os'] + '-' + run['arch'] + "on" + 
            self.mvs['os_arch'], '--force-update', '--toolsets=' + 
            run['compilers'], '--bjam-options="-m5 -j' + 
            str(self.mvs['procs']) + ' address-model=' + run['arch'] + 
            '"', '--comment=..\info.html']

        if run['type'] == 'release' or run['type'] == 'branches/release':
            command.append('--tag=master')
        else: # type == develop or no type
            command.append('--tag=develop')

        # Output the command to the screen before running it            
        cmd_str = ""
        for s in command:
            cmd_str += " " + s
        print "Runing command:"            
        print cmd_str[1:]            
        print ""

        with open("output.log", "w") as log_file:
            log_file.write("Running command:\n:")
            log_file.write(cmd_str[1:])
            log_file.write("\n")

            # Run
            proc = subprocess.Popen(command, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE)
            tee.tee_process(proc, log_file, log_file)


        if self.cleanup:
            try:
                shutil.rmtree('results')
                #rmtree on temp???
            except OSError:
		pass # dir wasn't there...may indicate previous failure
            
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

            r = sorted_runs[num % len(sorted_runs)]
            self.run_one(r)
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
           

if __name__ == '__main__':
    f = open("machine_vars.json", 'r')
    machine_vars = json.load(f)
    f.close()
    
    r = Runner(machine_vars)
    if len(sys.argv) > 1:
        r.run_one(sys.argv[1])
    else:
        r.cleanup = True
        r.restart()
