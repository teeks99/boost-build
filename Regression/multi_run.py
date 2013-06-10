import shutil
import os
import subprocess
import sys
import json

machine = "teeks99-03"
os = "win2008"
os_arch = "64"
procs = 4

runs = {}
runs["a"] = {"dir":"a", "type":"trunk", "arch":"64", "compilers":"msvc-8.0"}
runs["b"] = {"dir":"b", "type":"trunk", "arch":"64", "compilers":"msvc-9.0"}
runs["c"] = {"dir":"c", "type":"trunk", "arch":"64", "compilers":"msvc-10.0"}
runs["d"] = {"dir":"d", "type":"trunk", "arch":"64", "compilers":"msvc-11.0"}
runs["e"] = {"dir":"e", "type":"release", "arch":"64", "compilers":"msvc-8.0"}
runs["f"] = {"dir":"f", "type":"release", "arch":"64", "compilers":"msvc-9.0"}
runs["g"] = {"dir":"g", "type":"release", "arch":"64", "compilers":"msvc-10.0"}
runs["h"] = {"dir":"h", "type":"release", "arch":"64", "compilers":"msvc-11.0"}


class Runner(object):
    def __init__(self, runs, machine, cleanup=False):
        self.runs = runs
        self.machine = machine
        self.cleanup = cleanup
        self.start_dir = os.getcwd()

    def run_one(self, run):
        f = open("CurrentRun.json",'w')
        s = json.dump(run, f)
        f.close()        
    
        os.chdir(self.runs[run]["dir"])
        
        command = ['python', 'run.py', '--runner=' + machine + run['dir'] + 
            '-' + os + '-' + run['arch'] + "on" + os_arch, '--force-update',
            '--toolsets=' + run['compilers'], '--bjam-options="-j' + 
            str(procs) + ' address-model=' + run['arch'] + '"', 
            '--comment=..\info.html']

        # Output the command to the screen before running it            
        cmd_str = ""
        for s in command:
            cmd_str += " " + s
        print "Runing command:"            
        print cmd_str[1:]            
            
        # Run
        proc = subprocess.Popen(command, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE)
        
        # Tee the output to output.log as well as the screen
        with open("output.log", "w") as log_file:
          while proc.poll() is None:
             line = proc.stderr.readline()
             if line:
                print line.strip()
                log_file.write(line)
             line = proc.stdout.readline()
             if line:
                print line.strip()
                log_file.write(line)      

        if self.cleanup:
            shutil.rmtree('results')
            #rmtree on temp???
            
        os.chdir(self.start_dir)
        
    def loop(self, start_at=None):
        sorted_runs = self.runs.keys().sort()
        
        num = 0
        if start_at:
            # Jump to that run
            num = sorted_runs.index(start_at)
            start_at = None

        while True:
            r = sorted_runs[num % len(sorted_runs)]
            self.run_one(r)
            index += 1
        
    def restart(self)
        start_at = "a"
        try:
            f = open("CurrentRun.json",'r')
            at = json.load(f)
            f.close
        except IOError:
            pass #No file?

        if isinstance(at, basestring):
            start_at = at

        self.loop(start_at)
           

if __name__ == '__main__':
    r = Runner(runs, machine)
    if len(sys.argv) > 1:
        r.run_one(sys.argv[1])
    else:
        r.restart()
