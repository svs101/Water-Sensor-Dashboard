import paho.mqtt.client as mqtt
import json
import time
from WaterSensor import WaterSensorMQTT
import threading

def run_sensor(device_id, location, interval):
    sensor = WaterSensorMQTT(device_id=device_id, location=location)
    sensor.run_continuous(interval)

devices = [
    {"device_id": "GM-HYDROLOGIC-01", "location": "main-building"},
    {"device_id": "GM-HYDROLOGIC-02", "location": "pool-wing"},
    {"device_id": "GM-HYDROLOGIC-03", "location": "kitchen"},
]

threads = []
for d in devices:
    t = threading.Thread(target=run_sensor, args=(d["device_id"], d["location"], 2), daemon=True)
    t.start()
    threads.append(t)

print("All sensors running. Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping all sensors...")

