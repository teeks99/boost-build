import os, subprocess, shutil


runs = [Run('a','gcc-4.4'),
        Run('b','gcc-4.5'),
        Run('c','gcc-4.6'),
        Run('d','gcc-4.7'),
        Run('e','clang-3.0'),
        Run('f','clang-3.1'),
        Run('g','clang-3.2')]

start_path = ""

class Run(object):
    __init___(self, id, toolset):
       self.id = id
       self.toolset = toolset


def update_trunk():
    if os.path.exists('boost-trunk'):
        os.chdir('boost-trunk')
	stdout, stderr = subprocess.Popen(["svn", "up"], shell=False, stdout=subprocess.PIPE stderr=subprocess.STDOUT).communicate()
        print(stdout.split('\n'))
        os.chdir(start_path)
    else:
	stdout, stderr = subprocess.Popen(["svn", "co", "http://svn.boost.org/svn/boost/trunk"], shell=False, stdout=subprocess.PIPE stderr=subprocess.STDOUT).communicate()
        print(stdout.split('\n'))

def update_release():
    pass

def execute():
    start_path = os.getcwd()
    update_trunk()

    for run in runs:
        os.mkdir("run")
        os.chdir("run")
        shutil.copytree("../boost-trunk", "boost")
        shutil.copy("../info.html", "info.html")

        # Make start script
        # run start script

if __name__ == "__main__":
    execute()


        

