from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

# Variable to hold the state of the toggle button
toggle_state = False

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('toggle_button')
def handle_toggle(data):
    global toggle_state
    toggle_state = data['state']  # Update the toggle state
    emit('update_toggle', {'state': toggle_state}, broadcast=True)  # Broadcast to all clients

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=False, use_reloader=False)
