from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index_page():
	return render_template('index.html')

@app.route('/sockets')
def sockets_page():
	return render_template('sockets.html')

@socketio.on('connect')
def on_connect():
	print('connected!')
	emit('message', {'data': 'Connected!'})

@socketio.on('disconnect')
def on_disconnect():
	print('disconnected...')

@socketio.on('message')
def on_message(message):
	print('received:', message)

if __name__ == '__main__':
	socketio.run(app)