from time import sleep
from gpiozero import LED
from twython import TwythonStreamer
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

red = LED(22)
amber = LED(27)
green = LED(17)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            print("@{}: {}".format(username, tweet))
            # do something
            red.on()
            sleep(0.1)
            red.off()
            sleep(0.1)
            red.off()


stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
stream.statuses.filter(track='#python')
