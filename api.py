import uuid
import sys
import json
import urllib.parse as urlparse
import sqlite3

from flask import Flask, request
from flask_cors import CORS

from lobby.server import Server
from lobby.client import Client

app = Flask(__name__)
CORS(app)

# connects to db and causes sqlite to run on multithreaded system (supporting Flask)
conn = sqlite3.connect("yote.db", check_same_thread=False)
c = conn.cursor()


@app.route("/lobby", methods=["GET", "POST"])
def lobby():
    if request.method == "GET":
        Client("127.0.0.1", 10000)

        return "lobby - get"

    if request.method == "POST":
        server = Server("127.0.0.1", 10000)
        server.run()

        return "lobby - post"


# for session initialization [, between users]
@app.route("/session", methods=["GET", "POST"])
def session():
    # creates the session URL for the frontend link
    if request.method == "GET":
        # returning a uuid for the session_url
        return "yote.rocks/" + str(uuid.uuid4())

    # persists the session information (session_url, port, user_id)
    if request.method == "POST":
        # response.data (encoded string) decoded and loaded into dict
        res = json.loads(request.data.decode())

        # TODO make not hardcoded
        # port should increment every time
        # a post request is fired up to 8100
        port = 8081

        # res (dict) loaded into a (session_url, port) 2-tuple
        data = (res["session_url"], port)
        print("initializing sessiong with data", data)

        c.execute(
            "INSERT INTO sessions(session_url, port) VALUES (?, ?)", data)
        conn.commit()

        # sending session_url back to the client
        return res["session_url"]


# for file transfers between users
@app.route("/file", methods=["GET", "POST"])
def file():
    # gets file in DB based on session URL
    if request.method == "GET":
        # getting the url and parsing it to work with
        parsed_url = urlparse.urlparse(request.url)

        # getting the value for the url paramater key "session_url"
        requested_url = urlparse.parse_qs(parsed_url.query)["session_url"]

        # turning the requested_url variable into a 1-tuple for insertion into db
        requested_url = (requested_url[0],)

        c.execute("SELECT * FROM files WHERE session_url=?",
                  requested_url)
        sql_res = c.fetchall()

        # makes list of file objects
        # [
        #   {
        #       "name": <filename 1>,
        #       "data": <file 1 contents>
        #   },
        #   {
        #       "name": <filename 2>,
        #       "data": <file 2 contents>
        #   },
        #   ...
        # ]
        files = []
        for file in sql_res:
            files.append({
                "name": file[0],
                "data": file[2]
            })

        # sending that info back to client
        return json.dumps(files)

    # sends file to DB with session URL
    if request.method == "POST":
        # response.data (encoded string) decoded and loaded into dict
        res = json.loads(request.data.decode())

        # res (dict) loaded into a (name, data) 2-tuple
        data = (res["name"], res["data"], res["session_url"])

        # schema is (file_id (AI, PK), name, data)
        c.execute(
            "INSERT INTO files(name, data, session_url) VALUES (?, ?, ?)", data)
        # commiting changes to DB
        conn.commit()

        # returning the response.data as JSON to browser
        return json.dumps(res)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
