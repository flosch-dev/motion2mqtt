#!/usr/bin/python3
"""
simple python3 script to send motion detect via MQTT
python3 module required:
# apt install python3-gpiozero
# apt install python3-paho-mqtt

run:
# ./motion2mqtt <RPI_GPI> <Sensor#>
i.e.

# ./motion2mqtt 27 Sensor1

in order to use with systemd, place motion2mqtt_1.service into /etc/systemd/system/

# mv motion2mqtt_1.service /etc/systemd/system/
# systemctl daemon-reload
# systemctl start motion2mqtt_1.service
# systemctl enable motion2mqtt_1.service

"""

import time
import sys
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import os
from gpiozero import MotionSensor

""" ---- config -------- """

MQTT_HOST = ''
MQTT_PORT = 1883
MQTT_CLIENT_ID = os.popen('hostname').read().rstrip()

""" ---------------------------------"""

GPIO = sys.argv[1]
SENSOR = sys.argv[2]

auth = {
  'username':"MQTT_USER",
  'password':"MQTT_PASS"
}

def detect_motion(mqttclient):
    """
    function to detect motion and publish via mqtt connection
    loop every 100ms
    """
    pir = MotionSensor(GPIO)
    while True:
        if pir.motion_detected:
            mqttclient.publish("CHANNEL/Motion/" + SENSOR,
                                payload="motion")
            mqttclient.publish("CHANNEL/Motion/state",
                                payload=SENSOR + " motion")
            time.sleep(2)
            mqttclient.publish("CHANNEL/Motion/" + SENSOR,
                                payload="noMotion")
            mqttclient.publish("CHANNEL/Motion/state",
                                payload=SENSOR + " noMotion")
        time.sleep(0.1)

def on_disconnect(client, userdata,rc=0):
    print("DisConnected result code "+str(rc))
    client.loop_stop()
    exit(1)

def main():
    """
    Main function
    """
    mqttclient = mqtt.Client(MQTT_CLIENT_ID)
    try:
        mqttclient.connect(MQTT_HOST, port=MQTT_PORT, keepalive=60)
    except:
        print("MQTT Connection error")
    mqttclient.loop_start()
    mqttclient.on_disconnect = on_disconnect
    detect_motion(mqttclient)

if __name__=="__main__":
   main()
