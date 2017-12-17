import connection
import serial.tools.list_ports

activeConnections = None

def listDevices():
    ports = serial.tools.list_ports.comports()
    print("Ports", ports)
    return ports

def renameConnection(oldname, newname):
    connection = activeConnections[oldname]
    connection.name = newname
    activeConnections[newname] = connection
    del activeConnections[oldname]

def createConnection(devicename, deviceaddress):
    #Create a new connection object
    connection = Connection(devicename, deviceaddress)
    activeConnections[connection.name] = connection

def createVirtualConnection(devicename):
    #Create a new connection object
    connection = Connection(devicename, None, True)


