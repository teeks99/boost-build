import shutil
import os
import subprocess
import sys
import json
import io

class TeeStream(io.StringIO):
    def __init__(self, terminal_type, capture):
        if terminal_type not in ['stdout', 'stderr']:
            raise Exception('Invalid terminal type')
        self.terminal_type = terminal_type
        self.terminal = sys.__dict__[self.terminal_type]
        self.capture = capture
        io.StringIO.__init__(self)

    def fileno(self):
        return sys.__dict__[self.terminal_type].fileno()

    def write(self, message):
        self.terminal.write(message)
        self.capture.write(message)

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
            run['compilers'], '--bjam-options="-j' + str(self.mvs['procs']) + 
            ' address-model=' + run['arch'] + '"', '--comment=..\info.html']

        if run['type'] == 'release':
            command.append('--tag=branches/release')

        # Output the command to the screen before running it            
        cmd_str = ""
        for s in command:
            cmd_str += " " + s
        print "Runing command:"            
        print cmd_str[1:]            
        print ""

        with open("output.log", "w") as log_file:
            tee_stdout = TeeStream('stdout', log_file)
            tee_stderr = TeeStream('stderr', log_file)
            
            # Run
            proc = subprocess.Popen(command)#, 
                                stdout=tee_stdout, 
                                stderr=tee_stderr)

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
            r = sorted_runs[num % len(sorted_runs)]
            self.run_one(r)
            num += 1
        
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
