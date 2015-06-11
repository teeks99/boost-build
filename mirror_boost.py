#!/usr/bin/env python

import os

canonical_root = 'https://github.com/boostorg/'
#canonical_root = 'git@github.com:boostorg/'

mirror_dir = os.getcwd()


unpacked_repo = 'boost'

def print_and_run(command):
    print(command)
    os.system(command)

def update_unpacked_repo():
    if not os.path.isdir(unpacked_repo):
        print_and_run('git clone ' + canonical_root + 'boost ' + unpacked_repo)
    
    print('cd ' + unpacked_repo)
    os.chdir(unpacked_repo)
    print_and_run('git checkout master')
    print_and_run('git pull')
    print_and_run('git checkout develop')
    print_and_run('git pull')
    print('cd ' + mirror_dir)
    os.chdir(mirror_dir)

def add_modules(repos):
    with open('.gitmodules', 'r') as gitmodules:
        for line in gitmodules:
            if line.strip()[:6] == 'url = ':
                if line.strip()[6:9] == '../':
                    repos.append(line.strip()[9:])
                else:
                    print('not a valid relative path: ' + line)
    
def get_repos_list():
    repos = ['boost.git']
    
    print('cd ' + unpacked_repo)
    os.chdir(unpacked_repo)

    print_and_run('git checkout master')
    add_modules(repos)

    print_and_run('git checkout develop')
    add_modules(repos)

    print('cd ' + mirror_dir)
    os.chdir(mirror_dir)

    return set(repos)

def update_all(repos):
    for repo in repos:
        if not os.path.isdir(repo):
            print_and_run('git clone --bare ' + canonical_root + repo)
  
        print('cd ' + repo)
        os.chdir(repo)

        print_and_run('git fetch --prune')

        print('cd ' + mirror_dir)
        os.chdir(mirror_dir)


print('creating mirror of: ' + canonical_root + ' in: ' + mirror_dir)
update_unpacked_repo()
update_all(get_repos_list())
print('mirror updated')

