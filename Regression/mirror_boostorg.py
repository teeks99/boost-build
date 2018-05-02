import json
import sys
import os
import stat
import urllib.request
import subprocess
import shutil
import re

orginization = "boostorg"


def find_next(link):
    match = re.findall('<(.*?)>; rel="(.*?)"', link)
    for pair in match:
        if pair[1] == "next":
            return pair[0]

def get_all_repos(orginization):
    next_url = "https://api.github.com/orgs/" + orginization + "/repos"

    repos = []

    while next_url:
        resp = urllib.request.urlopen(next_url)
        batch = json.loads(resp.read().decode())
        repos.extend(batch)

        next_url = find_next(resp.getheader("Link"))

    return repos

def create_and_update(repo):
    bare_name = repo["name"] + ".git"
    if not os.path.isdir(bare_name):
        cmd = "git clone --bare " + repo["ssh_url"]
        print(cmd)
        subprocess.call(cmd, shell=True)

        # Set the repo to update the server data after an update
        with open(bare_name + "/hooks/post-update", "w") as f:
            f.write("# Prepare the packed repo for use over dumb transport\n")
            f.write("exec git update-server-info\n")

        os.chmod(bare_name + "/hooks/post-update", 0o775)

    os.chdir(bare_name)
    cmd = "git fetch"
    print(cmd)
    try:
        subprocess.call(cmd, shell=True, timeout=120)
    except subprocess.TimeoutExpired:
        print("Error: Could not update repo - " + bare_name)
    
    cmd = "git --bare update-server-info"
    subprocess.call(cmd, shell=True)
    os.chdir(root_dir)

root_dir = os.getcwd()
save_boost = None
repos = get_all_repos(orginization)
print("number of repos: " + str(len(repos)))
for repo in repos:
    # Do the boost repo last, so its dependencies will already be there
    if repo["name"] == "boost":
        save_boost = repo
    else:
        create_and_update(repo)

create_and_update(save_boost)

