simple python3 script to send motion detect via MQTT
python3 module required:
```bash
# apt install python3-gpiozero
# apt install python3-paho-mqtt
```

to run every 5 min via cron, add the following cronjob:
```bash
*/5 * * * * /<path-to-file>/sysmon2mqtt.py
```
