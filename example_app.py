import click
import meeseeks
from flask import Flask, url_for
from twilio.rest import TwilioRestClient


# Global Variables

app = Flask(__name__)
meeseek = meeseeks.Meeseeks()
meeseek.connect()
twilio_client, twilio_number = None, ""


# Endpoints

@app.route("/")
def api_root():
    return "Hi! I'm Mr. Meeseeks! Look at me!"

@app.route("/start/")
def start():
    meeseek.start()
    return "Start!"

@app.route("/score/<value>/")
def score(value):
    meeseek.send("Score: {0}%".format(str(value)))
    return "SCORE!"

@app.route("/send/<msg>/")
def send(msg):
    meeseek.send("Score: {0}".format(str(msg)))
    return "SENT!"

@app.route("/shoulders/")
def shoulders():
    meeseek.shoulders()
    return "Shoulders!"

@app.route("/choke/")
def choke():
    meeseek.choke()
    return "Choke!"

@app.route("/existence/")
def existence():
    meeseek.existence()
    return "Existence is PAIN!"

@app.route("/frustrating/")
def frustrating():
    meeseek.frustrating()
    return "Arrrgghhhh!"

@app.route("/head/")
def head():
    meeseek.head()
    return "Head!"

@app.route("/follow/")
def follow():
    meeseek.follow()
    return "Follow Through!"

@app.route("/nice/")
def nice():
    meeseek.nice()
    return "NIIICCCCCEEEE!!!"

@app.route("/result/<number>/")
def result(number):
    if twilio_client is not None:
        body = "HELLO"
        message = twilio_client.messages.create(
            to=number,
            from_=twilio_number,
            body=body,
        )
    return "Results sent to {0}".format(str(body))

if __name__ == '__main__':
    _account = click.prompt("Please enter your Twilio account")
    _token = click.prompt("Please enter your Twilio token")
    twilio_number = click.prompt("Please enter a phone number")
    twilio_client = TwilioRestClient(_account, _token)
    app.run(host="0.0.0.0")
