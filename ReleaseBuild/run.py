# Runs the Visual Studio Build for a python version
import os
import shutil
import subprocess
from string import Template
try:
    from urllib.request import urlretrieve
except ImportError: # Python 2
    from urllib import urlretrieve

tk_boost_deps = "https://boost.teeks99.com/deps/"

python2_ver = "2.7.13"
python3_ver = "3.6.0"

zlib_ver = "1.2.8"
zlib_base_path = "http://www.zlib.net/fossils/"

bzip2_ver = "1.0.6"
bzip2_base_path = "http://www.bzip.org/"

inno_ver = "5.5.9"

vc_versions = ["8.0", "9.0", "10.0", "11.0", "12.0", "14.0", "14.10"]
vc_archs = ["32", "64"]


class Builder(object):
    def __init__(self):
        self.version = "64"
        self.type = "master-snapshot"
        self.repo = "bintray"
        self.url = None
        self.build_drive = "D:" + os.sep
        self.build_dir = "ReleaseBuild"
        self.lib_check_dir = "LibraryCheck"

    def make_vars(self):
        self.build_path = os.path.join("/", self.build_drive, self.build_dir)
        self.lib_check_path = os.path.join(self.build_drive, self.lib_check_dir)
        if self.type == "master-snapshot":
            self.source = "boost_1_" + self.version + "_0_" + self.type
        elif self.type == "release":
            self.source = "boost_1_" + self.version + "_0"
        self.source_path = os.path.join(self.build_path, self.source)
        self.zip_cmd = os.path.join(self.build_path, "7z1604/7za.exe")
        self.inno_cmd = os.path.join(self.build_path, "Inno Setup 5/Compil32.exe")

    def make_dirs(self):
        shutil.copytree("../ReleaseBuild", self.build_path)
        shutil.copytree("../LibraryCheck", self.lib_check_path)
 
    def get_source(self):
        if not self.url:
            if self.repo == "bintray":
                if self.type == "master-snapshot":
                    # https://dl.bintray.com/boostorg/master/boost_1_64_0-snapshot.tar.bz2
                    self.url = "https://dl.bintray.com/boostorg/master/boost_1_" + self.version + "_0-snapshot.tar.bz2"
        print("Downloading: " + self.url + " to: " + self.source_path + ".tar.bz2")
        urlretrieve(self.url, self.source_path + ".tar.bz2")

    def get_and_extract_deps(self):
        self.py_extract("Python" + python2_ver + "-32.7z")
        self.py_extract("Python" + python2_ver + "-64.7z")
        self.py_extract("Python" + python3_ver + "-32.7z")
        self.py_extract("Python" + python3_ver + "-64.7z")
        self.standard_extract(zlib_base_path, "zlib-" + zlib_ver, [".tar", ".gz"])
        self.standard_extract(bzip2_base_path + bzip2_ver + "/", "bzip2-" + bzip2_ver, [".tar", ".gz"])
        self.standard_extract(tk_boost_deps, "InnoSetup-" + inno_ver, [".7z"])

    def py_extract(self, file_name):
        urlretrieve(tk_boost_deps + file_name, file_name)
        subprocess.call(self.zip_cmd + " x " + file_name)

    def standard_extract(self, base_url, archive_name, extensions):
        download_name = archive_name
        for extension in extensions:
            download_name += extension
        urlretrieve(base_url + download_name, download_name)
        for extension in reversed(extensions):
            subprocess.call(self.zip_cmd + " x " + download_name)
            download_name = download_name[:-len(extension)]        

    def extract_source(self):
        subprocess.call(self.zip_cmd + " x " + self.source + ".tar.bz2")
        subprocess.call(self.zip_cmd + " x " + self.source + ".tar")
        shutil.move("boost_1_" + self.version + "_0", self.source)

    def make_dependency_versions(self):
        with open("VS_DEPENDENCY_VERSIONS.txt", "r") as vs_versions:
            with open("DEPENDENCY_VERSIONS.txt", "w") as dep_ver:
                dep_ver.write("Python 2: " + python2_ver + "\n")
                dep_ver.write("Python 2: " + python2_ver + " amd64\n")
                dep_ver.write("Python 3: " + python3_ver + "\n")
                dep_ver.write("Python 3: " + python3_ver + " amd64\n")
                dep_ver.write("zlib: " + zlib_ver + "\n")
                dep_ver.write("bzip2: " + bzip2_ver + "\n")
                dep_ver.write("\n")
                dep_ver.write(vs_versions.read())

    def bootstrap(self):
        subprocess.call("bootstrap.bat", shell=True)

    def build_version(self, arch, vc):
        cmd = "b2 -j%NUMBER_OF_PROCESSORS% --without-mpi --build-type=complete toolset=msvc-" + vc + " address-model=" + arch + " architecture=x86 --prefix=.\ --libdir=lib" + arch + "-msvc-" + vc + " --includedir=garbage_headers install"
        print("Running: " + cmd)
        subprocess.call(cmd, shell=True)

        with open(arch + "bitlog.txt", "a") as log:
            log.write(cmd + "\n")

        subprocess.call(cmd + " >> " + arch + "bitlog.txt 2>&1", shell=True)

        #TODO Generate DEPENDENCY_VERSIONS.txt automatically
        shutil.copy("../DEPENDENCY_VERSIONS.txt", "lib" + arch + "-msvc-" + vc + "/DEPENDENCY_VERSIONS.txt")

    def copy_logs(self, arch):
        shutil.copy(arch + "bitlog.txt", "../" + self.source + "-" + arch + "bitlog.txt")
        cmd = "start \"Build Output\" notepad " + self.build_path + "\\" + self.source + "-" + arch + "bitlog.txt"
        subprocess.call(cmd)

    def midway_cleanup(self):
        shutil.rmtree(os.path.join(self.source_path, "garbage_headers"))
        shutil.copy("DEPENDENCY_VERSIONS.txt", os.path.join(self.source_path, "DEPENDENCY_VERSIONS.txt"))

    def make_archive(self):
        shutil.move(os.path.join(self.source_path, "bin.v2"), "bin.v2")
        archive = self.source + "-bin-msvc-all-32-64.7z"
        subprocess.call(self.zip_cmd + " a " + archive + " " + self.source_path)
        shutil.move("bin.v2", os.path.join(self.source_path, "bin.v2"))

    def make_installer(self, arch, vc):
        build_dir = "build-msvc-" + vc + "-" + arch
        os.mkdir(build_dir)
        os.chdir(build_dir)
        subprocess.call(self.zip_cmd + " x " + self.source_path + ".tar")        
        shutil.move("boost_1_" + self.version + "_0", self.source)
        libs = "lib" + arch + "-msvc-" + vc
        shutil.copytree(os.path.join(self.source_path, libs), os.path.join(self.source, libs))

        config = "msvc-" + vc + "-" + arch
        replace = {"FILL_VERSION": self.source, "FILL_CONFIG": config}
        with open(os.path.join(self.build_path, "BoostWinInstaller-PyTemplate.iss"), "r") as installer_template:
            stemplate = Template(installer_template.read())
            with open("installer_" + config + ".iss", "w") as installer:
                installer.write(stemplate.safe_substitute(replace))

        subprocess.call('"' + self.inno_cmd + '" /cc installer_' + config + ".iss", shell=True)
        os.chdir(self.build_path)
        installer_file = self.source + "-" + config + ".exe"
        shutil.move(os.path.join(build_dir, installer_file), installer_file)
        shutil.rmtree(build_dir)

    def initialize(self):
        # TODO: Load comamd arguments
        self.make_vars()

    def prepare(self):
        self.make_dirs()
        self.get_source() # Do this in a thread
        os.chdir(self.build_path)
        self.make_dependency_versions()
        self.get_and_extract_deps()
        self.extract_source()       

    def build(self):
        os.chdir(self.source_path)
        self.bootstrap()
        for vc_arch in vc_archs:
            for vc_ver in vc_versions:
                self.build_version(vc_arch, vc_ver)
            self.copy_logs(vc_arch)

        os.chdir(self.build_path)
        self.midway_cleanup()

    def package(self):
        self.make_archive()

        for vc_arch in vc_archs:
            for vc_ver in vc_versions:
                self.make_installer(vc_arch, vc_ver)

    def run_build(self):
        self.initialize()
        self.prepare()
        self.build()
        self.package()

    def run_package(self):
        self.initialize()
        os.chdir(self.build_path)
        self.package()


if __name__ == "__main__":
    b = Builder()
    b.run_build()
