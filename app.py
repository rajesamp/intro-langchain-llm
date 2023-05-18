from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "this is from flask app, unable to show a fastapi yet"