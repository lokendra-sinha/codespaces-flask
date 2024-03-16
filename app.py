from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/name")

def name():

    return "Mithanshu"

@app.route("/age")

def age():

    return "21"

@app.route("/hello")

def hello():

    return "hello"

@app.route("/goodbye")

def goodbye():

    return "goodbye"
