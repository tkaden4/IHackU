from flask import Flask, request

CHALLENGE_KEY = "ihacku{challenge-completed}"

USER_NAME="jbob1975"
USER_PW="hunter2"

app = Flask(__name__)

@app.route("/login")
def login():
    auth = request.authorization
    if auth and auth.username == USER_NAME and auth.password == USER_PW:
        return CHALLENGE_KEY
    else:
        return "Not Authenticated"

