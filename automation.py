from flask import Flask, render_template
import RPi.GPIO as GPIO 
import time

app = Flask(__name__)

led1 = 2
led2 = 3
led3 = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.output(led1, 0)
GPIO.output(led2, 0)
GPIO.output(led3, 0)

print("Done")

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/led1-on')
def led1on():
    GPIO.output(led1, 1)
    return render_template('index.html')

@app.route('/led1-off')
def led1off():
    GPIO.output(led1, 0)
    return render_template('index.html')

@app.route('/led2-on')
def led2on():
    GPIO.output(led2, 1)
    return render_template('index.html')

@app.route('/led2-off')
def led2off():
    GPIO.output(led2, 0)
    return render_template('index.html')

@app.route('/led3-on')
def led3on():
    GPIO.output(led3, 1)
    return render_template('index.html')

@app.route('/led3-off')
def led3off():
    GPIO.output(led3, 0)
    return render_template('index.html')


if __name__ == "__main__":
    print("Start")
    app.run(host='192.168.0.104', port=5010)