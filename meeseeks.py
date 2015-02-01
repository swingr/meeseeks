import pebble as p
import audio

class Meeseeks():
    def __init__(self, id="464F", name="Mr. Meeseeks"):
        self.id = id
        self.name = name
        self.pebble = None

    def connect(self):
        self.pebble = p.Pebble(self.id)

    def send(self, msg):
        self.pebble.notification_sms(self.name, msg)

    def start(self):
        self.send("Are you ready to take two strokes off your game! Ohhhhh yeah!")
        audio.start()

    def shoulders(self):
        self.send("Remember to square your shoulders!")
        audio.shoulders()

    def choke(self):
        self.send("Don't choke!")
        audio.choke()

    def existence(self):
        self.send("Existence is pain!")
        audio.existence()

    def frustrating(self):
        self.send("Arrgghhhhhhh!")
        audio.frustrating()

    def head(self):
        self.send("Keep your head down!")
        audio.head()

if __name__ == "__main__":
    meeseeks = Meeseeks()
    meeseeks.connect()
    meeseeks.choke()
