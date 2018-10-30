from flask import Flask, request
import os
import base64
from xor import encrypt

app = Flask(__name__)

key = os.environ["KEY"]

@app.route("/", methods=["POST", "GET"])
def root():
    if request.method == "POST":
        plaintext = request.form["plaintext"]
        encrypted = base64.b64encode(encrypt(plaintext, key))
        return f"""
            <html>
            <head>
                <title>Encryptext</title>
            </head>
            <body>
                {encrypted}
            </body>
            </html>
        """;
    elif request.method == "GET":
        return f"""
            <html>
            <head>
                <title>Encryptext</title>
            </head>
            <body>
                <form action="/" method="POST">
                    Plaintext: <input name="plaintext" type="text"></input>
                    <br/>
                    <button type="submit" value="submit">submit</button>
                </form>
            </body>
            </html>
        """;

if __name__ == "__main__":
    app.run(debug=True)
