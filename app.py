from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/googlef630b9d133a5c2af.html")
def google_verification():
    return send_from_directory(".", "googlef630b9d133a5c2af.html")

if __name__ == "__main__":
    app.run(debug=True)
