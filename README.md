# motion2mqtt
simple python3 script to send motion detect via MQTT
python3 module required:
```bash
# apt install python3-gpiozero
# apt install python3-paho-mqtt
```
run:
./motion2mqtt <RPI_GPI> <Sensor#>
i.e.
```bash
# ./motion2mqtt 27 Sensor1
```
in order to use with systemd, place motion2mqtt_1.service into /etc/systemd/system/
```bash
# mv motion2mqtt_1.service /etc/systemd/system/
# systemctl daemon-reload
# systemctl start motion2mqtt_1.service
# systemctl enable motion2mqtt_1.service
```
