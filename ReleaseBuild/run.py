# Runs the Visual Studio Build for a python version
import os
import shutil
import subprocess
try:
    from urllib.request import urlretrieve
except ImportError: # Python 2
    from urllib import urlretrieve

class Builder(object):
    def __init__(self):
        self.version = "64"
        self.type = "master-snapshot"
        self.repo = "bintray"
        self.url = None
        self.build_drive = "D:"
        self.build_dir = "ReleaseBuild"
        self.lib_check_dir = "LibraryCheck"

    def make_vars(self):
        self.build_path = os.path.join(self.build_drive, self.build_dir)
        self.lib_check_path = os.path.join(self.build_drive, self.lib_check_dir)
        self.source = "boost_1_" + self.version + "_0_" + self.type
        self.source_path = os.path.join(self.build_path, self.source)

    def make_dirs(self):
        shutil.copytree("../ReleaseBuild", self.build_path)
        shutil.copytree("../LibraryCheck", self.lib_check_path)
 
    def get_source(self):
        if not self.url:
            if self.repo == "bintray":
                if self.type == "master-snapshot":
                    # https://dl.bintray.com/boostorg/master/:boost_1_64_0-snapshot.tar.bz2
                    self.url = "https://dl.bintray.com/boostorg/master/:boost_1_" + self.version + "_0-snapshot.tar.bz2"
        urlretrieve(self.url, self.source_path + ".tar.bz2")

    def extract_deps(self):
        zip_cmd = os.path.join(self.build_path, "7z465/7z.exe")
        subprocess.call(zip_cmd + " x Python27-32.7z")
        subprocess.call(zip_cmd + " x Python27-64.7z")
        subprocess.call(zip_cmd + " x zlib-1.2.8.tar.gz")
        subprocess.call(zip_cmd + " x zlib-1.2.8.tar")
        subprocess.call(zip_cmd + " x bzip2-1.0.6.tar.gz")
        subprocess.call(zip_cmd + " x bzip2-1.0.6.tar")
        os.environ["ZLIB_SOURCE"] = os.path.join(self.build_path, "zlib-1.2.8")
        os.environ["BZIP2_SOURCE"] = os.path.join(self.build_path, "bzip2-1.0.6")

    def extract_source(self):
        zip_cmd = os.path.join(self.build_path, "7z465/7z.exe")
        subprocess.call(zip_cmd + " x " + self.source + ".tar.bz2")
        subprocess.call(zip_cmd + " x " + self.source + ".tar")
        shutil.move("boost_1_" + self.version + "_0", self.source)

    def bootstrap(self):
        subprocess.call("bootstrap.bat", shell=True)

    def build_version(self, vc, arch):
        cmd = "b2 -j%NUMBER_OF_PROCESSORS% --without-mpi --build-type=complete toolset=msvc-" + vc + " address-model=" + arch + " architecture=x86 --prefix=.\ --libdir=lib" + arch + "-msvc-" + vc + " --includedir=garbage_headers install"
        print("Running: " + cmd)
        subprocess.call(cmd, shell=True)

        with open(arch + "bitlog.txt", "w+") as log:
            log.write(cmd + "\n")

        subprocess.call(cmd + " >> " + arch + "bitlog.txt 2>&1", shell=True)

        shutil.copy("../DEPENDENCY_VERSIONS.txt", "lib" + arch + "-msvc-" + vc + "/DEPENDENCY_VERSIONS.txt")

    def run_build(self):
        # Load comamd arguments
        self.make_vars()
        self.make_dirs()
        self.get_source() # Do this in a thread
        os.chdir(self.build_path)
        self.extract_deps()
        self.extract_source()
        os.chdir(self.source_path)
        self.bootstrap()
        self.build_version("32", "8.0")
        # ...
        self.build_version("64", "14.0")



if __name__ == "__main__":
    b = Builder()
    b.run_build()
