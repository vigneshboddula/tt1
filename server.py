from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Dew Drop Service!"

if _name_ == "__main__":
    app.run(host='0.0.0.0')
    
