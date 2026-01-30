from flask import Flask, render_template
import random

app = Flask(__name__)

WORDS = [
    "домик", "комик", "кошка", "вилка", "фляга",
    "песня", "ручка", "лампа", "столб", "трава"
]

SECRET = random.choice(WORDS)


@app.route("/")
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"ERROR: {e}"


@app.route("/secret")
def get_secret():
    return SECRET


@app.route("/new")
def new_game():
    global SECRET
    SECRET = random.choice(WORDS)
    return "ok"


if name == "__main__":
    app.run(host="0.0.0.0", port=5000)



