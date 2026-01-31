from flask import Flask, render_template
import random

app = Flask(__name__)

WORDS = [
    "домик", "кошка", "лампа", "вилка", "трава",
    "песня", "ручка", "столб", "флага", "комик"
]

SECRET = random.choice(WORDS)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/secret")
def secret():
    return SECRET


@app.route("/check/<word>")
def check(word):
    word = word.lower()

    if word in WORDS:
        return "ok"
    else:
        return "no"

@app.route("/new")
def new():
    global SECRET
    SECRET = random.choice(WORDS)
    return "ok"


if __name__ == "__main__":
    app.run()











