import os

KEY_STR = "gitdir: "

def relative_submodules(repo_dir=os.getcwd()):
    original_path = os.getcwd()
    try:
        os.chdir(repo_dir)
        if not os.path.isfile(".gitmodules"):
            print("No submodules to update")
        else:
            for submodule in get_submodules():
                replace_git_path(submodule)
    finally:
        os.chdir(original_path)
    
def get_submodules():
    with open(".gitmodules", "r") as mods:
        lines = mods.readlines()
    submodules = []
    
    for line in lines:
        line = line.lstrip()
        if "path = " == line[:7]:
            submodules.append(line[7:])

    return submodules

def replace_git_path(submodule):
    submodule = submodule.rstrip()
    gitfile = os.path.join(submodule, ".git")
    print("replacing: " + gitfile)
    if not os.path.isfile(gitfile):
        print("No git file, not a submodule?")
        return

    with open(gitfile, 'r+') as f:
        lines = []
        for l in f.readlines():           
            if l.startswith(KEY_STR):
                l = get_dir_line(l, get_rel_reverse(submodule))
            lines.append(l)

        f.seek(0)
        f.truncate()

        for l in lines:
            f.write(l)

def get_dir_line(line, relative_up):
    original = line[len(KEY_STR):]
    if not os.path.isabs(original):
        return KEY_STR + original

    inside_git = original[original.find(".git"):]
    return KEY_STR + os.path.join(relative_up, inside_git)

def get_rel_reverse(submodule_path):
    path = ""
    for _ in range(get_path_depth(submodule_path)):
        path = os.path.join(path, "..")
    return path

def get_path_depth(path):
    dirs = []
    while 1:
        path, end = os.path.split(path)

        if end != "":
            dirs.append(end)
        else:
            if path != "":
                folders.append(path) # Get the start
                folders.reverse()
            break

    return len(dirs)

if __name__ == "__main__":
    relative_submodules()
