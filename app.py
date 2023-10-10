from flask import Flask, request

from constants import HOST, PORT

app = Flask(__name__)

# Simple status endpoint showing how to implement a GET-style route
@app.route("/status", methods=["GET"])
def status():
    return "ok"

# Simple endpoint showing how to implement a POST-style route
@app.route("/echo", methods=["POST"])
def echo():

    # Grab the json data sent in as the request payload/data. As this is an
    # echo route, we will just return with whatever was received.
    data = request.json
    return data

if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=int(PORT))