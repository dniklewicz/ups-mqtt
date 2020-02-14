#!/usr/bin/python3
# ups-mqtt.py

import os
import subprocess
import paho.mqtt.publish as mqtt
import time
from time import sleep, localtime, strftime
import datetime

cached_values = {}
base_topic = os.environ['MQTT_TOPIC']
if not base_topic.endswith('/'):
    base_topic += '/'

ups_host = os.environ['UPS_HOST']
mqtt_host = os.environ['MQTT_HOST']
mqtt_user = os.environ['MQTT_USERNAME']
mqtt_password = os.environ['MQTT_PASSWORD']
interval = int(os.environ['INTERVAL'])

def process():
    ups = subprocess.run(["upsc", "ups@" + ups_host], stdout=subprocess.PIPE)
    lines = ups.stdout.decode('utf-8').split('\n')

    msgs = []

    for line in lines:
        fields = line.split(':')
        if len(fields) < 2:
            continue

        key = fields[0].strip()
        value = fields[1].strip()

        if cached_values.get(key, None) != value:
            cached_values[key] = value
            topic = base_topic + key.replace('.', '/').replace(' ', '_')
            msgs.append((topic, value, 0, True))
        
        timestamp = time.time()
        msgs.append((base_topic + 'timestamp', timestamp, 0, True))
        msgs.append((base_topic + 'lastUpdate', datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'), 0, True))
        mqtt.multiple(msgs, hostname=mqtt_host, auth={'username': mqtt_user, 'password': mqtt_password})



while True:
    process()
    sleep(interval)