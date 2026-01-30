from flask import Flask, render_template
import random
import os

app = Flask(__name__, template_folder="templates")

WORDS = [
    "домик", "комик", "кошка", "вилка", "флага",
    "песня", "ручка", "лампа", "столб", "трава"
]

SECRET = random.choice(WORDS)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/secret")
def get_secret():
    return SECRET


@app.route("/new")
def new_game():
    global SECRET
    SECRET = random.choice(WORDS)
    return "ok"


@app.route("/debug")
def debug():
    files = os.listdir("templates") if os.path.exists("templates") else "NO TEMPLATES DIR"
    return str(files)


if name == "__main__":
    app.run(host="0.0.0.0", port=5000)





