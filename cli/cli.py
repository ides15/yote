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


def start():
    requests.post("http://localhost:8080/lobby")
    pass

def connect():
    requests.get("http://localhost:8080/lobby")
    pass

# sends the file at <path> to DB as JSON object
def send(path):
    data = {}

    # data dict looks like
    # {
    #   "name": "<filename>",
    #   "data": "<file data>"
    # }
    with open(path, "r") as file:
        data["name"] = path
        data["data"] = file.read()

    # get info from config file
    # after, data dicts looks like
    # {
    #   ...
    #   "session_url": <session_url>
    # }
    with open(yote_config_file, "r") as config:
        config_info = json.loads(config.read())
        data["session_url"] = config_info["session_url"]

    # serializes data dict
    data = json.dumps(data)

    # attempt to POST data to DB
    try:
        requests.post("http://localhost:8080/file", data=data)
    except requests.exceptions.ConnectionError:
        print("API is down, try again later.")


# receives file stored in DB at <session_url> of the current user's config file
def recv():
    # loads the config file info into config_info dict
    with open(yote_config_file, "r") as config:
        config_info = json.loads(config.read())

    # fires GET request asking for file data relating to the matching session url
    payload = {"session_url": config_info["session_url"]}
    r = requests.get("http://localhost:8080/file", params=payload)
    data = r.json()

    # replicates files from DB in the current user's directory
    for file in data:
        with open(file["name"], "w") as source:
            source.write(file["data"])


# initializes a yote workspace in current directory
# param url: from yote frontend > Generate Session
def init(url):
    parsed_url = urlparse.urlparse("http://" + url)

    # creates data dict with session_url key
    # {
    #   "session_url": "/<unique url path>"
    # }
    data = {}
    data["session_url"] = parsed_url.path

    # if a yote workspace exists don't create a new one
    if os.path.exists(yote_dir_path):
        print('Yote session already initialized')
        print('Run "yote reinit <url>" with new URL to create a new session (not implemented yet)')
        return

    # inserts data dict into DB, along with a port for the lobby
    try:
        requests.post("http://localhost:8080/session", data=json.dumps(data))
    except requests.exceptions.ConnectionError:
        print("API is down, try again later.")
        return

    # create yote workspace in current directory
    os.mkdir(yote_dir_path)
    print('Yote session initialized')

    # creates yote config file and writes data dict to it
    with open(yote_config_file, "wb") as file:
        file.write(json.dumps(data).encode())


if __name__ == "__main__":
    # makes each function callable on command line
    fire.Fire({
        "init": init,
        "send": send,
        "recv": recv,
        "start": start,
        "connect": connect
    })
