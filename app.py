from flask import Flask, render_template, redirect, url_for
from data_utils import locations
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("/home.html")

@app.route("/map", methods=['POST'])
def map():
    loc_array = locations
    return render_template("/map.html", locations=loc_array)

@app.route("/crime_map", methods=['POST'])
def crime_map():
    return render_template("/crime_map.html")

if __name__ == "__main__":
    app.run(debug=True)
