import json
import devices 
import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template

sio = socketio.Server()
app = Flask(__name__)
app.debug = True

# Flask Route
@app.route('/')
def root():
    return render_template('index.html')

# Socket API
@sio.on('connect')
def sioConnect(sid, environ):
    print("conect", sid)

@sio.on('disconnect')
def sioDisconnect(sid):
    print('disconnect', sid)

@sio.on('send-command')
def sendCommand(sid, data):
    # Need to create the binary command out of the data sent here
    pass

@sio.on('send-raw')
def sendRaw(sid, data):
    print('raw data', sid, data)
    pass

@sio.on('list-devices')
def listDevices(sid):
    print('Requesting devices')
    ret = devices.listDevices()
    sio.emit('list-devices', ret)

@sio.on('rename-connection')
def renameConnection(sid, data):
    print(data)
    print('rename-connections')
    print('old name : ', data['old'])
    print('new name : ', data['new'])
    ret = devices.renameConnection(data['old'], data['new'])
    sio.emit('rename-connection', ret)

@sio.on('list-connections')
def listConnections(sid):
    print('Requesting active connections')
    ret = devices.listConnections()
    sio.emit('list-connections', ret)

@sio.on('activate')
def activate(sid, data):
    # Activate teh connection
    pass

@sio.on('deactivate')
def deactivate(sid, data):
    # Deactivate the connection
    pass

if __name__ == '__main__':
    devices.listDevices()
    app = socketio.Middleware(sio,app)
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 3000)), app)

