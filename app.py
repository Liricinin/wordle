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


@app.route("/new")
def new():
    global SECRET
    SECRET = random.choice(WORDS)
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)




