from paho.mqtt.client import Client
from paho.mqtt.enums import CallbackAPIVersion
import json
import time

# Defining the server, port and subject
NATS_SERVER = "demo.nats.io"
MQTT_PORT = 1883
NATS_SUBJECT = "device/temp"

# Defining the sensor data
sensor_data = {
    "id": "sensor-01",
    "temperature": 32
}

# Connecting to the NATS Server via MQTT
client = Client(callback_api_version=CallbackAPIVersion.VERSION2)
print(f"Connecting to NATS via MQTT on port {MQTT_PORT}...")
client.connect(NATS_SERVER, MQTT_PORT, 60)

client.loop_start()

# Dumping the data into json
payload = json.dumps(sensor_data)

# Publishing the data into the topic (subject)
try:
    print(f"Publishing Data to {NATS_SUBJECT}: {payload}")
    info = client.publish(NATS_SUBJECT, payload)
    info.wait_for_publish()
    print("Message published!")
    time.sleep(1)
except Exception as e:
    print(f"Error: {e}")
# Closing the connection
finally:
    client.loop_stop()
    client.disconnect()
    print("Disconnected.")