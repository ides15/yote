import sys
import os
import urllib.parse as urlparse
import json

import fire
import requests

cwd = os.getcwd()
yote_dir_path = cwd + "/.yote"
yote_config_file = yote_dir_path + "/config.json"

# TODO make a login command
# saves user info to the config file
# persists to user table in DB


def send(path):
    data = {}
    with open(path, "r") as file:
        data["name"] = path
        data["data"] = file.read()

    with open(yote_config_file, "r") as config:
        config_info = json.loads(config.read())
        data["session_url"] = config_info["session_url"]

    data = json.dumps(data)

    try:
        requests.post("http://localhost:8080/file", data=data)
    except requests.exceptions.ConnectionError:
        print("API is down, try again later.")


def recv():
    with open(yote_config_file, "r") as config:
        config_info = json.loads(config.read())

    payload = {"session_url": config_info["session_url"]}
    r = requests.get("http://localhost:8080/file", params=payload)
    data = r.json()

    with open(data["name"], "w") as file:
        file.write(data["data"])


def init(url):
    parsed_url = urlparse.urlparse("http://" + url)

    data = {}
    data["session_url"] = parsed_url.path

    if os.path.exists(yote_dir_path):
        print('Yote session already initialized')
        print('Run "yote reinit <url>" with new URL to create a new session (not implemented yet)')
        return

    try:
        requests.post("http://localhost:8080/session", data=json.dumps(data))
    except requests.exceptions.ConnectionError:
        print("API is down, try again later.")
        return

    os.mkdir(yote_dir_path)
    print('Yote session initialized')

    with open(yote_config_file, "wb") as file:
        file.write(json.dumps(data).encode())


if __name__ == "__main__":
    fire.Fire({
        "init": init,
        "send": send,
        "recv": recv
    })
