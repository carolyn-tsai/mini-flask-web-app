import os
from flask import (
    Flask,
    render_template,
    request,
    abort,
    redirect)

asset_folder = os.path.join("static", "images")

app = Flask(__name__)

app.config["image"] = asset_folder

@app.route("/")
def home_page():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def send_data():
    string_to_cut = request.form["string_to_cut"]   

    if string_to_cut == "":
        return_string = "Invald Input. You didn't enter anything!"
    else:  
        # Slice(start, stop, step) - start:2 for third letter in string, stop : end of string, step:3 for every 3rd letter afte
        return_string = string_to_cut[2::3]
    return render_template("result.html", return_string=return_string)

if __name__ == "__main__":
    app.run(debug=True)
