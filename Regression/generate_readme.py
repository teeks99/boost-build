import json
import re
from string import Template
from collections import OrderedDict

linux_flags = {
    'c++98': '-std=c++98',
    'gnu98': '-std=gnu++98',
    'c++0x': '-std=c++0x',
    'gnu0x': '-std=gnu++0x',
    'c++11': '-std=c++11',
    'gnu11': '-std=gnu++11',
    'c++1y': '-std=c++1y',
    'gnu1y': '-std=gnu++1y',
    'c++14': '-std=c++14',
    'gnu14': '-std=gnu++14',
    'c++1z': '-std=c++1z',
    'gnu1z': '-std=gnu++1z',
    'c++17': '-std=c++17',
    'gnu17': '-std=gnu++17',
    'c++2a': '-std=c++2a',
    'gnu2a': '-std=gnu++2a',
    'c++20': '-std=c++20',
    'gnu20': '-std=gnu++20',
    'lc': '-stdlib=libc++',
    'O2': '-O2',
    'warn': '-Wall -Wextra'
}
    

def make_linux_table():
    configs = None
    with open('linux_docker_configs.json', 'r') as configs_file:
        configs = json.load(configs_file, object_pairs_hook=OrderedDict)

    table = ""
    header = "| Name | Branch | Compiler | Version | Flags | Docker Image |\n"
    h_sepr = "| ---- | ------ | -------- | ------- | ----- | ------------ |\n"

    table = header + h_sepr

    for config_name, data in configs['runs'].items():
        name = config_name
        branch = data["branch"]
        compiler_data = re.split(r'-|~', data['compilers'])
        compiler = compiler_data[0]
        version = compiler_data[1]
        flags = ''

        for flag in compiler_data[2:]:
            flags += linux_flags[flag] + ' '
        flags = flags.rstrip()

        docker_img = data['docker_img']
        
        line = ""
        line += "| " 
        line += config_name
        line += " | " 
        line += branch 
        line += " | " 
        line += compiler
        line += " | " 
        line += version
        line += " | " 
        line += flags
        line += " | " 
        line += docker_img 
        line += " |" 

        table += line + "\n"

    return table

def generate_readme():
    substitutions = {}
    substitutions['linux_table'] = make_linux_table()

    template = None
    with open('README.md.template', 'r') as template_file:
        template = template_file.read()
    
    final_file = Template(template).substitute(substitutions)

    with open('README.md', 'w') as output_file:
        output_file.write(final_file) 

if __name__ == "__main__":
    generate_readme()
