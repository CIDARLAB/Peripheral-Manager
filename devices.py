import serial.tools.list_ports

from connection import Connection

ACTIVE_CONNECTIONS = dict()

def list_devices():
    ports = serial.tools.list_ports.comports()
    ret = []
    for port in ports:
        val = {}
        val["device"] = port.device
        val["name"] = port.name
        val["description"]  = port.description
        val["hwid"] = port.hwid
        val["vid"] = port.vid
        val["pid"] = port.pid
        val["serialnumuber"] = port.serial_number
        val["location"] = port.location
        val["maufacturer"] = port.manufacturer
        val["product"] = port.product
        val["interface"] = port.interface
        ret.append(val) 
    print("Devices Connected Now: \n", ret)
    return ret

def list_connections():
    ret = []
    for key in ACTIVE_CONNECTIONS.keys():
        val = {}
        connection = ACTIVE_CONNECTIONS[key]
        val["name"] = connection.name
        val["address"] = connection.address
        ret.append(val)
    return ret

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
    print(connection)
    connection.stop()
    del ACTIVE_CONNECTIONS[devicename]
