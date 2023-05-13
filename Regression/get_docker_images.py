import json
import subprocess

def find_images(config_file):
    cfg = {}
    images = set()
    with open(config_file, "r") as f:
        cfg = json.load(f)

    for cfg in cfg["runs"].values():
        if "docker_img" in cfg:
            images.add(cfg["docker_img"])

    return images

def pull_image(image):
    cmd = f"docker pull {image}"
    print(cmd)
    subprocess.check_call(cmd, shell=True)

def main():
    images = find_images("linux_docker_configs.json")
    for image in images:
        pull_image(image)

if __name__ == "__main__":
    main()
