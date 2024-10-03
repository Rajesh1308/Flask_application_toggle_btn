// Connect to the Flask-SocketIO server
var socket = io();

// Get reference to the toggle button
var toggleBtn = document.getElementById('toggle-btn');

// Listen for the 'update_toggle' event from the server
socket.on('update_toggle', function(data) {
    toggleBtn.checked = data.state;  // Update the button state based on server data
});

// Emit the 'toggle_button' event when the button is clicked
toggleBtn.addEventListener('change', function() {
    socket.emit('toggle_button', { state: toggleBtn.checked });
});