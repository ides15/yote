import uuid
import json
from pprint import pprint

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/session", methods=['GET', 'POST'])
def generate_session():
    if request.method == 'GET':
        data = {
            "session_id": str(uuid.uuid4())
        }

        return json.dumps(data).encode()
    else:
        pprint(request)
        pprint(dir(request))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)