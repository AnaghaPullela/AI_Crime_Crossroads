from flask import Flask, render_template, redirect, url_for
from data_utils import locations
from stats import crimes
import os

app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:5000'

@app.route("/")
@app.route("/home", methods=['POST'])
def home():
    return render_template("/home.html")

@app.route("/map", methods=['POST'])
def map():
    loc_array = locations
    return render_template("/map.html", locations=loc_array)

@app.route("/crime_map", methods=['POST'])
def crime_map():
    return render_template("/crime_map.html")

@app.route("/stats", methods=['POST'])
def stats():
    return render_template("/stats.html", crimes=crimes)

if __name__ == "__main__":
    app.run(debug=True)
