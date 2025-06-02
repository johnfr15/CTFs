# pip install "python-socketio[client]" requests websocket-client
import socketio

sio = socketio.Client()

@sio.event
def connect():
	pass


@sio.event
def message(msg_type, data):
	pass


@sio.event
def disconnect():
	pass

# to send a message:
# sio.emit("message", "game_start")

sio.connect('http://URL/')
sio.wait()
