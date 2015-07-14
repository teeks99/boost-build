import os
import shutil
import string

versions = [
    {'type':'gcc', 'number':'5.1', 'os':'trusty', 'pkg_num':'5', 'ppa':'ubuntu-toolchain-r/test'},
    {'type':'clang', 'number':'3.6', 'os':'trusty'}
]

def make_versions(vers=versions):
    for version in vers:
        tag = version['type'] + '-' + version['number']
        fresh_dir(tag)
        make_dockerfile(version, tag)
        make_user_config(version, tag)

def fresh_dir(tag):
    if os.path.isdir(tag):
        shutil.rmtree(tag)
    os.mkdir(tag)

def make_dockerfile(version, tag):
    template = ""
    with open('Dockerfile.' + version['os'] + '.template', 'r') as template_file:
        template = string.Template(template_file.read())

    mapping = {
        'packages': packages(version),
        'PPA_line': ppa_line(version),
        'symlink_cmd': symlink(version)
    }

    df_str = template.substitute(mapping)
    with open(os.path.join(tag, 'Dockerfile'), 'w') as df:
        df.write(df_str)

def packages(version):
    packages = ''
    if version['type'] == 'gcc':
        number = version['number']
        if 'pkg_num' in version:
            number = version['pkg_num']
        packages+= 'gcc-' + number + ' '
        packages+= 'g++-' + number + ' '
    elif version['type'] == 'clang':
        packages+= 'clang-' + version['number'] + ' '
    return packages

def ppa_line(version):
    line = ''
    if 'ppa' in version:
        line += 'RUN apt-get update && apt-get install -y software-properties-common &&'
        line += ' add-apt-repository -y ppa:'
        line += version['ppa']
    return line

def symlink(version):
    cmd = ''
    if 'symlink' in version:
        info = version['symlink']
        cmd += 'RUN '
        cmd += 'cd ' + info['dir'] + ' && '
        cmd += 'ln -s ' + info['src'] + ' ' + info['dest']
    return cmd

def make_user_config(version, tag):
    template = ""
    with open('user-config.jam.' + version['os'] + '.template', 'r') as template_file:
        template = string.Template(template_file.read())

    mapping = {
        'toolsets': toolsets(version)
    }

    df_str = template.substitute(mapping)
    with open(os.path.join(tag, 'user-config.jam'), 'w') as df:
        df.write(df_str)

def toolsets(version):
    ts = ''
    # TODO: Support other configs
    if version['type'] == 'gcc':
        pkg_num = version['number']
        if 'pkg_num' in version:
            pkg_num = version['pkg_num']
        ts += 'using gcc : ' + version['number'] + ' : g++-' + pkg_num + ' : ; \n'
    elif version['type'] == 'clang':
        ts += 'using clang : ' + version['number'] + ' : clang++-' + version['number'] + ' : '
        ts += '<cxxflags>-Wno-c99-extensions ; \n'
    return ts

if __name__ == '__main__':
    make_versions()
