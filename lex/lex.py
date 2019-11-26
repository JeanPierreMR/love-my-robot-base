from flask import Flask, request 
import json

app = Flask(__name__)


@app.route("/lex", methods=["POST"])
def postdata():
    print(request.get_json()["lmr"])

@app.route("/", methods=["POST"])
def api():
    print("Lex On")



if __name__ == "__main__":
    app.run(host="0.0.0.0")