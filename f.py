import Adafruit_DHT
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
  h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
  t=('TEMPERATURE :{0:0.1f}'.format(t))
  return render_template('t.html' , temp=t)
