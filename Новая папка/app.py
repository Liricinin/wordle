from flask import Flask, render_template
import random

app = Flask(__name__)

WORDS = [
    "арбуз", "домик", "маши", "книга", "ручка",
    "школа", "окноо", "рекаа", "мирок", "котик"
]

@app.route("/")
def index():
    word = random.choice(WORDS)
    return render_template("index.html", word=word)

if __name__ == "__main__":
    app.run()

