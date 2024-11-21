import time
import paho.mqtt.client as paho
from paho import mqtt
import csv


# setting callbacks for different events to see if it works, print the message etc.
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    # Decode the message payload
    message = msg.payload.decode()
    print(msg.topic + " " + str(msg.qos) + " " + message)

    # Write message data into CSV file
    with open('mqtt_messages.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            [time.strftime('%Y-%m-%d %H:%M:%S'), msg.topic, message])


# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

# Set username and password
client.username_pw_set("YOUR_USERNAME", "YOUR_PASSWORD")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("YOUR_CLUSTER_URL", 8883)

# Set callback functions
client.on_subscribe = on_subscribe
client.on_message = on_message

# Subscribe to the topic
client.subscribe("sensor/data", qos=1)

# Loop forever to keep the connection alive and receiving messages
client.loop_forever()
