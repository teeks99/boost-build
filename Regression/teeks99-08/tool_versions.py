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
        ('14.0', {'dir_type': 'modern', 'number': '140'})
    ]),
    'gcc': {
        '4.4': None,
        '4.5': None,
        '4.6': None,
        '4.7': None,
        '4.8': None,
        '4.9': None,
        '5.0': None
    },
    'clang': {
        '2.8': None,
        '2.9': None,
        '3.0': None,
        '3.1': None,
        '3.2': None,
        '3.3': None,
        '3.4': None,
        '3.5': None,
        '3.6': None
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
    p = subprocess.Popen(version['command'], stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    out, err = p.communicate()
    version['full'], version['number'], version['arch'] = \
        parse_msvc_version_output(err)       

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

def make_versions():
    versions = []
    versions += make_msvc_versions()
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

def python_version():
    p = subprocess.Popen('python --version', stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    out, err = p.communicate()
    return err
    
def git_version():
    p = subprocess.Popen('git --version', stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
    
def print_all():
    print_version_info()
    print(python_version())
    print(git_version())
    
if __name__ == "__main__":
    print_all()

