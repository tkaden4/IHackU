#!/usr/bin/env python

from flask import Flask
import os

key = os.environ["IHACKU_KEY"]

app = Flask(__name__)

@app.route("/")
def index():
    return f"""
<!doctype html>
<html>
    <head>
        <title>I Hack U Challenge</title>
    </head>
    <body>
        <!-- The key is {key} --!>
        <form action="#" method="GET">
            Password: <input type="password"></input>
            <br />
            <input type="submit" value="submit"></input>
        </form>
    </body>
</html>
"""
