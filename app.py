import os
from flask import (
    Flask,
    jsonify,
    abort,
    request)

app = Flask(__name__)

@app.route("/test", methods=["POST"])
def send_data():
    data = request.get_json()
    if "string_to_cut" not in data:
        abort(400)
    string = data["string_to_cut"]
    # Slice(start, stop, step) - start:2 for third letter in string, stop : end of string, step:3 for every 3rd letter after
    return_string = {"return_string" : string[2::3]}
    return jsonify(return_string)

if __name__ == "__main__":
    app.run(debug=True)
