from flask import Flask, render_template, redirect, url_for
from data_utils import get_data
import os

app = Flask(__name__)

@app.route("/")
def home():
    print("Current working directory: ", os.getcwd())
    print("Files in the current directory:", os.listdir())
    return render_template("/home.html")

@app.route("/hello")
def print_data():
    value = get_data()
    return f"{value}"

if __name__ == "__main__":
    app.run(debug=True)
