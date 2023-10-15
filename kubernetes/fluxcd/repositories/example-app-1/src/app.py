from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! hongphuc5497/example-app-1:0.0.1"
