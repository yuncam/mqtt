#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import config as conf

# This is the Subscriber

sub_topic = "topic/test"

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe(sub_topic)
  print(f"Listening to topic: {sub_topic} @ {conf.broker_ip}")

def on_message(client, userdata, msg):
#   if msg.payload.decode() == "Hello world!":
#     print("Received message:", msg.payload.decode())
#     client.disconnect()
    print("Received message:", msg.payload.decode())
    # client.disconnect()

    
client = mqtt.Client()
client.connect(conf.broker_ip,1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()