#!/usr/bin/env python3
"""a basic flask app"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    """a function to return the index page"""
    return render_template("templates/index.html")

if __name__ == '__main__':
    app.run()
