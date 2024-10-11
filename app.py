from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import paho.mqtt.client as paho
from paho import mqtt

app = Flask(__name__)
socketio = SocketIO(app)

# Variable to hold the state of the toggle button
toggle_state = False
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("YOUR_USERNAME", "YOUR_PASSWORD")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("YOUR_CLUSTER_URL", 8883)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('toggle_button')
def handle_toggle(data):
    global toggle_state
    toggle_state = data['state']  # Update the toggle state
    client.publish("sensor/data", payload=toggle_state, qos=1)
    emit('update_toggle', {'state': toggle_state}, broadcast=True)  # Broadcast to all clients

if __name__ == '__main__':
    socketio.run(app, port=5000, debug=False)
