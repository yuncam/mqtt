#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("192.0.1.10",1883,60)
client.publish("topic/test", "Hello world!");
client.disconnect();