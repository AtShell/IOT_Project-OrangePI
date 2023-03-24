from flask import Flask,render_template
app = Flask(__name__)
wsgi_app = app.wsgi_app
ledStat=0

@app.route("/")
def home():
    global ledStat
    data={
        'led' : ledStat
        }
    return render_template('index.html', **data)
@app.route("/<action>")
def action(action):
    global ledStat
    if action == "on":
        ledStat=1
    if action == "off":
        ledStat=0
    data={
        'led' : ledStat
        }
    return render_template('index.html',**data)

app.run (host="0.0.0.0", port=8500)
