import serial.tools.list_ports

from connection import Connection

ACTIVE_CONNECTIONS = dict()

def list_devices():
    ports = serial.tools.list_ports.comports()
    print("Ports", ports)
    return ports

def list_connections():
    return ACTIVE_CONNECTIONS.values()

def rename_connection(oldname, newname):
    connection = ACTIVE_CONNECTIONS[oldname]
    connection.name = newname
    ACTIVE_CONNECTIONS[newname] = connection
    del ACTIVE_CONNECTIONS[oldname]
    #TODO - Check for errors and return false if there are errors
    return True

def create_connection(devicename, deviceaddress, socketio):
    #Create a new connection object
    connection = Connection(devicename, deviceaddress, socketio)
    ACTIVE_CONNECTIONS[connection.name] = connection
    #TODO - Check for errors and return false if there are errors
    return True

def create_virtualconnection(devicename):
    #Create a new connection object
    connection = Connection(devicename, None, True)
    ACTIVE_CONNECTIONS[connection.name] = connection

def send_rawdata(devicename, rawdata):
    #Send the raw data on the connection
    connection = ACTIVE_CONNECTIONS[devicename]
    connection.send_data(rawdata)  

def close_connection(devicename):
    connection = ACTIVE_CONNECTIONS[devicename]
    connection.close_connection()
    del ACTIVE_CONNECTIONS[devicename]
