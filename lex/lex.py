from flask import Flask, request 
import json
import transpilator
app = Flask(__name__)
transpiler = transpilator.transpilator()


@app.route("/lex", methods=["POST"])
def postdata():
    try:
        code = (request.get_json()["lmr"])
        print(code)
        transpiler.transpile(code)
        transpiler.run()
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    except Exception as e:
        print(e)
        return json.dumps({'success':False}), 400, {'ContentType':'application/json'} 

@app.route("/", methods=["POST"])
def api():
    print("Lex On")



if __name__ == "__main__":
    app.run(host="0.0.0.0")