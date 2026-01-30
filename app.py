from flask import Flask, render_template
import random

app = Flask(__name__)

WORDS = [
    "домик", "комик", "кошка", "вилка", "рекаа",
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


if name == "__main__":
    app.run()
