from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello from Flask!"

@app.route("/compile", methods = ['GET', 'POST'])
def compilation():
    request.form.get('subir')
    pass

@app.route("/execute", methods = ['GET', 'POST'])
def compilation():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0")