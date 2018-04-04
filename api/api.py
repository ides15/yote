import uuid
import json
import urllib.parse as urlparse
import sqlite3

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = sqlite3.connect("yote.db", check_same_thread=False)
c = conn.cursor()

@app.route("/session", methods=["GET", "POST"])
def begin_session():
    if request.method == "GET":
        # getting the url and parsing it to work with
        parsed_url = urlparse.urlparse(request.url)

        # getting the value for the paramater key "session_url"
        requested_url = urlparse.parse_qs(parsed_url.query)["session_url"]

        # turning the requested_url variable into a 1-tuple for insertion into db
        requested_url = (requested_url[0],)

        c.execute("SELECT name, data FROM files WHERE session_url=?", requested_url)
        sql_res = c.fetchone()

        data = {
            "name": sql_res[0],
            "data": sql_res[1]
        }

        # sending that info back to client
        return json.dumps(data)

    if request.method == "POST":
        # response.data (encoded string) decoded and loaded into dict
        res = json.loads(request.data.decode())

        # res (dict) loaded into a (name, data) 2-tuple
        data = (res["name"], res["data"], res["session_url"])

        # schema is (file_id (AI, PK), name, data)
        c.execute("INSERT INTO files(name, data, session_url) VALUES (?, ?, ?)", data)
        # commiting changes to DB
        conn.commit()

        # returning the response.data as JSON to browser
        return json.dumps(res)

if __name__ == "__main__":
    app.run(port=8080, debug=True)