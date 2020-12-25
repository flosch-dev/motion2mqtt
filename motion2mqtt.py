#!/usr/bin/python3
"""
simple python3 script to send motion detect via MQTT
python3 module required:
# apt install python3-gpiozero
# apt install python3-paho-mqtt

to run every 5 min via cron, add the following cronjob:
*/5 * * * * /<path-to-file>/sysmon2mqtt.py
"""

import time
import sys
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import os
from gpiozero import MotionSensor

""" ---- config -------- """

MQTT_HOST = ''
MQTT_CLIENT_ID = os.popen('hostname').read().rstrip()

""" ---------------------------------"""

GPIO = sys.argv[1]
SENSOR = sys.argv[2]

auth = {
  'username':"MQTT_USER",
  'password':"MQTT_PASS"
}

def mqtt_publish(state):
    """ function to send MQTT message """
    try:
        mqttclient.publish("CHANNEL/Motion/" + SENSOR,
                    payload=state,
                    qos=0,
                    retain=False)
    except:
        pass

    try:
        mqttclient.publish("CHANNEL/Motion/state",
                    payload=SENSOR + " " + state,
                    qos=0,
                    retain=False)
    except:
        pass

pir = MotionSensor(GPIO)
mqttclient = mqtt.Client(MQTT_CLIENT_ID)
try:
    mqttclient.connect(MQTT_HOST, port=MQTT_PORT, keepalive=60)
except:
    print("Connection error - retrying...")

while True:
    if pir.motion_detected:
        mqtt_publish("motion")
        time.sleep(2)
        mqtt_publish("noMotion")
    time.sleep(0.1)
