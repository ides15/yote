import uuid
import json
import pickle
from pprint import pprint

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/session", methods=["GET", "POST"])
def begin_session():
    if request.method == "GET":
        # temporary static file data store
        with open("temp-file.pkl", "rb") as file:
            data = pickle.load(file)

        return data

    if request.method == "POST":
        data = request.data.decode()

        # temporary static file data store
        with open("temp-file.pkl", "wb") as file:
            pickle.dump(data, file)

        return data

if __name__ == "__main__":
    app.run(port=8080, debug=True)