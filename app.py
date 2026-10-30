from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/catalog")
def catalog():
    return render_template("catalog.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


if __name__ == "__main__":
    app.run(debug=True)