import sys
import os
import json

import fire

cwd = os.getcwd()
yote_dir_path = cwd + "/.yote"
yote_config_file = yote_dir_path + "/config"

def send(path):
    data = {}
    with open(path, "r") as file:
        data["name"] = path
        data["data"] = file.read()
    
    print(data)

def init(url):
    if os.path.exists(yote_dir_path):
        print('Yote session already initialized')
    else:
        os.mkdir(yote_dir_path)
        print('Yote session initialized')
    
    with open(yote_config_file, "wb") as file:
        data = {
            "session_id": url
        }

        file.write(json.dumps(data).encode())

if __name__ == "__main__":
    fire.Fire({
        "init": init,
        "send": send
    })