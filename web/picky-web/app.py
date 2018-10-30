from flask import Flask, request
import os

app = Flask(__name__)

key = os.environ["KEY"]

@app.route("/")
def index():
    if "Chrome/v1.0.0" in request.user_agent.string:
        return key
    else:
        return "I only give out keys to people who used chrome on september 2nd, 2008"
        
