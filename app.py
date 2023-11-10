import OPi.GPIO as GPIO
from flask import Flask, render_template
from time import sleep

app = Flask(__name__)
PIN = 7 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.LOW)

wsgi_app = app.wsgi_app


@app.route("/")
def home():
    ledStat = GPIO.input(PIN)
    data = {"led": ledStat}
    return render_template("index.html", **data)


@app.route("/<action>")
def action(action):
    if action == "on":
        GPIO.output(PIN, GPIO.HIGH)
    if action == "off":
        GPIO.output(PIN, GPIO.LOW)
    ledStat = GPIO.input(PIN)
    data = {"led": ledStat}
    return render_template("index.html", **data)


app.run(host="0.0.0.0", port=8500)
