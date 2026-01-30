from flask import Flask, render_template
import random

app = Flask(__name__, template_folder="templates")

WORDS = [
    "домик", "кошка", "лампа", "вилка", "трава",
    "песня", "ручка", "столб", "флага", "комик"
]

SECRET = random.choice(WORDS)


@app.route("/")
def index():
    return "<h1>TEST</h1>"


@app.route("/secret")
def secret():
    return SECRET


@app.route("/new")
def new():
    global SECRET
    SECRET = random.choice(WORDS)
    return "ok"


if __name__ == "__main__":
    app.run()







