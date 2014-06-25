import subprocess
import os

def get_path(version_num):
    p = os.getenv('VS' + str(version_num) + 'COMNTOOLS')
    if p:
        return p[:-15] # Strip off '\Common7\Tools\'

def make_default(number, id):
    versions = []
    pad = ""
    if len(id) == 3:
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
    return versions    

def make_vc8():
    return make_default('80','vc8')
    
def make_vc9():
    return make_default('90','vc9')
    
def make_vc10():
    return make_default('100','vc10')

def make_vc11():
    return make_default('110','vc11')

def make_vc12():
    number = '120'
    id = 'vc12'
    
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
    return versions    
    
def make_versions():
    versions = []
    versions += make_vc8()
    versions += make_vc9()
    versions += make_vc10()
    versions += make_vc11()
    versions += make_vc12()
    return versions
    
def parse_version_output(ver):
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

def get_version_info():    
    versions = make_versions()
    for v in versions:
        existing_path = os.getenv('PATH')
        os.environ['PATH'] = v['sys_path_add'] + ";" + existing_path
        p = subprocess.Popen(v['command'], stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE)
        out, err = p.communicate()
        v['full'], v['number'], v['arch'] = parse_version_output(err)
    return versions

def print_version_info():
    versions = get_version_info()
    for version in versions:
        print(version['version'] + " - " + version['number'] + " - " + 
            version['arch'])
        #print(version['full'])

if __name__ == "__main__":
    print_version_info()