#!/usr/bin/python

import paho.mqtt.client as mqtt

from settings import mq_host, queue_topic

import datetime

import pytz


def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")))
    amsterdam = pytz.timezone("Europe/Amsterdam")
    local_time = datetime.datetime.now()
    timestampStr = amsterdam.localize(local_time).strftime("%d-%b-%Y (%H:%M:%S)")

    f = open("hue_logs.txt", "a")
    f.write(timestampStr + " " +  str(message.payload.decode("utf-8")) + "\n")
    f.close()
    f.close()

client = mqtt.Client()
client.connect(mq_host)
client.loop_start()
client.subscribe(queue_topic)

while True:
    client.on_message = on_message

# time.sleep(5)
# client.loop_stop()

