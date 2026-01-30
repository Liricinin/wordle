@app.route("/wordle")
def wordle():
    return render_template("wordle.html")
