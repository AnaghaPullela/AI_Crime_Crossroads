from flask import Flask, render_template, redirect, url_for
from data_utils import locations
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("/home.html")

@app.route("/map/<int:id>")
def map(id):
    latitude = locations[id][0]
    longitude = locations[id][1]
    return render_template("/map.html", lat=latitude, lon=longitude)

if __name__ == "__main__":
    app.run(debug=True)
