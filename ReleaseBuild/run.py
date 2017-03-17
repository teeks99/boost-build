# Runs the Visual Studio Build for a python version
import os
import shutil
import subprocess
import itertools
import threading
import multiprocessing
import datetime
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

class Archive(object):
    def __init__(self, zip_cmd, base_url, package, extensions=[], local_file=None):
        self.zip_cmd = zip_cmd
        self.base_url = base_url
        self.package = package
        self.extensions = extensions
        if not self.extensions:
            base, ext = os.path.splitext(self.package)
            while ext in [".tar", ".bz2", ".xz", ".gz", ".7z", ".zip"]:
                self.package = base
                self.extensions.append(ext)
                base, ext = os.path.splitext(self.package)
            self.extensions.reverse()
            
        if local_file:
            self.local_file = local_file
        else:
            self.local_file = self.package
        self.download_name = self.package

        for extension in extensions:
            self.download_name += extension
            self.local_file += extension

    def download(self):
        url = self.base_url + self.download_name
        print("Downloading: " + url)
        urlretrieve(url, self.local_file)
        with open(self.local_file, "r") as f:
            pass

    def extract(self):
        unzip_name = self.local_file
        for extension in reversed(self.extensions):
            subprocess.call(self.zip_cmd + " x " + unzip_name)
            unzip_name = unzip_name[:-len(extension)]        

    def get(self):
        self.download()
        self.extract()

    def params(self):
        return [
            self.zip_cmd, self.base_url, self.package, self.extensions,
            self.local_file, self.download_name
        ]


class RemoteArchive(Archive):
    def __init__(self, params):
        self.zip_cmd = params[0]
        self.base_url = params[1]
        self.package = params[2]
        self.extensions = params[3]
        self.local_file = params[4]
        self.download_name = params[5]


def run_remote_archive(params):
    a = RemoteArchive(params)
    a.get()


class Builder(object):
    def __init__(self):
        self.version = "64"
        self.type = "master-snapshot"
        self.repo = "bintray"
        self.url = None
        self.file = None
        self.build_drive = "D:" + os.sep
        self.build_dir = "ReleaseBuild"
        self.lib_check_dir = "LibraryCheck"
        self.archives = []

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

    def make_user_config(self):
        usrcfg_file = os.path.expanduser("~/user-config.jam")
        if not os.path.exists(usrcfg_file):
            self.py_config_replace = {}
            for version, arch, end in itertools.product(
                    ["27", "36"], ["32", "64"], ["include", "libs"]):
                self.make_python_config_path(version, arch, end)

            with open("user-config.jam.template", "r") as uctemp:
                stemplate = Template(uctemp.read())
                with open(usrcfg_file, "w") as usrcfg:
                    usrcfg.write(stemplate.safe_substitute(self.py_config_replace))            

    def make_python_config_path(self, version, arch, end):
        key = "PY" + version + "_" + arch + end
        path = os.path.join(self.build_path, "Python" + version + "-" + arch, end)
        escaped = os.path.normpath(path).replace("\\", "\\\\")
        self.py_config_replace[key] = escaped

    def make_dirs(self):
        shutil.copytree("../ReleaseBuild", self.build_path)
        shutil.copytree("../LibraryCheck", self.lib_check_path)
 
    def make_source_archive(self):
        # https://dl.bintray.com/boostorg/master/boost_1_64_0-snapshot.tar.bz2
        if not self.url:
            if self.repo == "bintray":
                if self.type == "master-snapshot":
                    self.url = "https://dl.bintray.com/boostorg/master/"

        if not self.file:
            if self.type == "master-snapshot":
                self.file = "boost_1_" + self.version + "_0-snapshot.tar.bz2"

        self.archives.append(Archive(self.zip_cmd, self.url, self.file, local_file=self.source))        

    def make_dep_archives(self):
        z = self.zip_cmd
        a = self.archives
        a.append(Archive(z, tk_boost_deps, "Python" + python2_ver + "-32", [".7z"]))
        a.append(Archive(z, tk_boost_deps, "Python" + python2_ver + "-64", [".7z"]))
        a.append(Archive(z, tk_boost_deps, "Python" + python3_ver + "-32", [".7z"]))
        a.append(Archive(z, tk_boost_deps, "Python" + python3_ver + "-64", [".7z"]))
        a.append(Archive(z, zlib_base_path, "zlib-" + zlib_ver, [".tar", ".gz"]))
        a.append(Archive(z, bzip2_base_path + bzip2_ver + "/", "bzip2-" + bzip2_ver, [".tar", ".gz"]))
        a.append(Archive(z, tk_boost_deps, "InnoSetup-" + inno_ver, [".7z"]))

    def get_and_extract_archives(self):
        for a in self.archives:
            a.get()

    def get_and_extract_archives_threaded(self):
        workers = [ threading.Thread(target=a.get) for a in self.archives ]
        for worker in workers: worker.start()
        for worker in workers: worker.join()

    def get_and_extract_archives_process(self):
        workers = [ multiprocessing.Process(target=run_remote_archive, args=(a.params(),)) for a in self.archives ]
        for worker in workers: worker.start()
        for worker in workers: worker.join()

    def move_source(self):
        shutil.move("boost_1_" + self.version + "_0", self.source)

    def set_env_vars(self):
        zlib = os.path.join(self.build_path, "zlib-" + zlib_ver)
        os.environ["ZLIB_SOURCE"] = os.path.normalize(zlib)

        bzip2 = os.path.join(self.build_path, "bzip2-" + bzip2_ver)
        os.environ["BZIP2_SOURCE"] = os.path.normalize(bzip2)

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
        subprocess.call(cmd, shell=True)

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
        self.prepare_start = datetime.datetime.now()
        self.make_user_config()
        self.make_dirs()
        os.chdir(self.build_path)
        self.make_source_archive()
        self.make_dep_archives()
        #self.get_and_extract_archives()
        #self.get_and_extract_archives_threaded()
        self.get_and_extract_archives_process()
        self.move_source()       
        self.prepare_stop = datetime.datetime.now()

    def build(self):
        self.build_start = datetime.datetime.now()
        os.chdir(self.source_path)
        self.bootstrap()
        for vc_arch in vc_archs:
            for vc_ver in vc_versions:
                self.build_version(vc_arch, vc_ver)
            self.copy_logs(vc_arch)

        os.chdir(self.build_path)
        self.midway_cleanup()
        self.build_stop = datetime.datetime.now()

    def package(self):
        self.package_start = datetime.datetime.now()
        self.make_archive()

        for vc_arch, vc_ver in itertools.product(vc_archs, vc_versions):
            self.make_installer(vc_arch, vc_ver)
        self.package_stop = datetime.datetime.now()

    def package_threaded(self):
        self.package_start = datetime.datetime.now()
        workers = []
        workers.append(threading.Thread(target=self.make_archive))

        for vc_arch, vc_ver in itertools.product(vc_archs, vc_versions):
            workers.append(threading.Thread(target=self.make_installer, args=(vc_arch, vc_ver)))

        for worker in workers: worker.start()
        for worker in workers: worker.join()
        self.package_stop = datetime.datetime.now()

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
