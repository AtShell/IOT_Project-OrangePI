from asyncio import constants
import OPi.GPIO as GPIO
from time import sleep
from flask import Flask,render_template
app = Flask(__name__)
PIN=7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN,GPIO.OUT)
GPIO.output(PIN,GPIO.LOW)

wsgi_app = app.wsgi_app

@app.route('/')
@app.route('/home')
def home():
    ledStat=GPIO.input(PIN)
    return render_template(
        'index.html', ledStat
        )
@app.route("/<action>")
def action(action):
    if action == "on":
        GPIO.output(PIN,GPIO.HIGH)
    if action == "off":
        GPIO.output(PIN,GPIO.LOW)
    ledStat=GPIO.input(PIN)
    return render_template(
        'index.html',**ledStat)
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
