import uuid
import json

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/session")
def generate_session():
    data = {
        "session_id": str(uuid.uuid4())
    }

    return json.dumps(data).encode()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)