import subprocess
import os
import collections

tools = {
    'msvc': collections.OrderedDict([
        ('8.0', {'dir_type': 'default', 'number': '80'}),
        ('9.0', {'dir_type': 'default', 'number': '90'}),
        ('10.0', {'dir_type': 'default', 'number': '100'}),
        ('11.0', {'dir_type': 'default', 'number': '110'}),
        ('12.0', {'dir_type': 'modern', 'number': '120'}),
        ('14.0', {'dir_type': 'modern', 'number': '140'}),
        ('14.1', {'dir_type': 'modern', 'number': '141'}),
        ('15.0', {'dir_type': 'modern', 'number': '150'}),
    ]),
    'gcc': {
        '4.4': {},
        '4.5': {},
        '4.6': {},
        '4.7': {},
        '4.8': {},
        '4.9': {},
        '5': {},
        '6': {},
        '7': {},
    },
    'clang': {
        '2.8': {},
        '2.9': {},
        '3.0': {},
        '3.1': {},
        '3.2': {},
        '3.3': {},
        '3.4': {},
        '3.5': {},
        '3.6': {},
        '3.7': {},
        '3.8': {},
        '3.9': {},
        '4.0': {}
        '5.0': {},
    },
}
def parse_msvc_version_output(ver):
    #example: b'Microsoft (R) 32-bit C/C++ Optimizing Compiler Version 14.00.50727.762 for 80x86\r\nCopyright (C) Microsoft Corporation.  All rights reserved.\r\n\r\n'
    full = ver.decode('utf-8')
    words = full.split()
    num_index = 0
    for w in words:
        if w == "Version":
            break
        num_index += 1

    num_index += 1 # Word after "Version"

    number = words[num_index]
    arch = words[num_index + 2]

    return full, number, arch

def get_msvc_info(version):
    existing_path = os.getenv('PATH')
    os.environ['PATH'] = version['sys_path_add'] + ";" + existing_path
    try:
        p = subprocess.Popen(version['command'], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = p.communicate()
        version['full'], version['number'], version['arch'] = \
            parse_msvc_version_output(err)
    finally:
        os.environ['PATH'] = existing_path

def get_path(version_num):
    p = os.getenv('VS' + str(version_num) + 'COMNTOOLS')
    if p:
        return p[:-15] # Strip off '\Common7\Tools\'

def make_default(number, id):
    versions = []
    pad = ""
    if len(id) == 8:
        pad = " "

    base_path = get_path(number)
    if base_path:
        versions.append({'version':id+'      '+pad,'command':
            base_path + "\\VC\\bin\\cl.exe", 'sys_path_add':
            base_path + "\\Common7\\IDE"})
        versions.append({'version':id+'-64   '+pad,'command':
            base_path + "\\VC\\bin\\amd64\\cl.exe",
            'sys_path_add':
            base_path + "\\Common7\\IDE"})
        versions.append({'version':id+'-32-64'+pad,'command':
            base_path + "\\VC\\bin\\x86_amd64\\cl.exe",
            'sys_path_add':
            base_path + "\\Common7\\IDE"})

    for v in versions:
        get_msvc_info(v)
    return versions

def make_modern(number, id):
    versions = []

    base_path = get_path(number)
    if base_path:
        versions.append({'version':id+'      ','command':
            base_path + "\\VC\\bin\\cl.exe", 'sys_path_add':
            base_path + "\\VC\\bin\\"})
        versions.append({'version':id+'-64   ','command':
            base_path + "\\VC\\bin\\amd64\\cl.exe",
            'sys_path_add':
            base_path + "\\VC\\bin\\"})
        versions.append({'version':id+'-32-64','command':
            base_path + "\\VC\\bin\\x86_amd64\\cl.exe",
            'sys_path_add':
            base_path + "\\VC\\bin\\"})

    for v in versions:
        get_msvc_info(v)
    return versions

def make_msvc_versions():
    versions = []
    for name, data in tools['msvc'].items():
        if data['dir_type'] == 'default':
            versions += make_default(data['number'], 'msvc-' + name)
        elif data['dir_type'] == 'modern':
            versions += make_modern(data['number'], 'msvc-' + name)
    return versions

def get_parse_gcc_output(output):
    return output.split('\n')[0]

def make_gcc_versions():
    versions = []
    for name, data in tools['gcc'].items():
        exe = 'g++-' + name
        if 'exe' in data:
            exe = data['exe']
        cmd = exe + ' --version'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        if not out:
            continue
        v = {'version':'gcc-'+name, 'arch':''}
        v['number'] = get_parse_gcc_output(out)
        versions.append(v)
    return versions

def get_parse_clang_output(output):
    lines = output.split('\n')
    return lines[0], lines[1] + ' ' + lines[2]

def make_clang_versions():
    versions = []
    for name, data in tools['clang'].items():
        exe = 'clang-' + name
        if 'exe' in data:
            exe = data['exe']
        cmd = exe + ' --version'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        if not out:
            continue
        v = {'version':'clang-'+name}
        v['number'], v['arch'] = get_parse_clang_output(out)
        versions.append(v)
    return versions

def make_versions():
    versions = []
    versions += make_msvc_versions()
    versions += make_gcc_versions()
    versions += make_clang_versions()
    return versions

def build_version_string():
    versions = make_versions()
    output = ""
    for version in versions:
        output += version['version'] + " - " + version['number'] + " - " + \
            version['arch'] + "\n"
    return output

def print_version_info():
    print(build_version_string())

class ConfigFinder(object):
    def __init__(self):
        pass

    def try_read(self, fname):
        if os.path.isfile(fname):
            with open(fname, 'r') as f:
                self.value += f.read()

    def user_config(self):
        fn = 'user-config.jam'
        self.value = ''

        # Since the boost-build isn't clear on which one is used if multiple are present, 
        # just going to concatenate all of them.
        if os.environ.get('HOME'):
            self.try_read(os.path.join(os.environ.get('HOME'), fn))
        if os.environ.get('HOMEDRIVE') and os.environ.get('HOMEPATH'):
            home = os.path.join(os.environ.get('HOMEDRIVE'), os.environ.get('HOMEPATH'))
            self.try_read(os.path.join(home, fn))
        if os.environ.get('BOOST_BUILD_PATH'):
             self.try_read(os.path.join(os.environ.get('BOOST_BUILD_PATH'), fn))

        if not self.value:
            self.value = 'user-config.jam not found in search path'

        return self.value


    def site_config(self):
        fn = 'site-config.jam'
        self.value = ''

        # Since the boost-build isn't clear on which one is used if multiple are present, 
        # just going to concatenate all of them.
        self.try_read(os.path.join('/etc', fn))
        if os.environ.get('SystemRoot'):
            self.try_read(os.path.join(os.environ.get('SystemRoot'), fn))
        if os.environ.get('HOME'):
            self.try_read(os.path.join(os.environ.get('HOME'), fn))
        if os.environ.get('HOMEDRIVE') and os.environ.get('HOMEPATH'):
            home = os.path.join(os.environ.get('HOMEDRIVE'), os.environ.get('HOMEPATH'))
            self.try_read(os.path.join(home, fn))
        if os.environ.get('BOOST_BUILD_PATH'):
             self.try_read(os.path.join(os.environ.get('BOOST_BUILD_PATH'), fn))

        if not self.value:
            self.value = 'site-config.jam not found in search path'

        return self.value


def user_config():
    return ConfigFinder().user_config()

def site_config():
    return ConfigFinder().site_config()

def python_version():
    p = subprocess.Popen('python --version', stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    return err

def git_version():
    p = subprocess.Popen('git --version', stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    return out

def print_all():
    print_version_info()
    print(python_version())
    print(git_version())

if __name__ == "__main__":
    print_all()

