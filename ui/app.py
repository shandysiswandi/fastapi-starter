from flask import Flask, render_template
import requests

API_URL = "http://localhost:8000/products"

app = Flask(__name__)


@app.route("/")
def index():
    products = requests.get(API_URL).json()
    return render_template("index.html", products=products)


if __name__ == "__main__":
    app.run(debug=True)
