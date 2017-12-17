import serial
import datetime

class Connection:

    name = ""
    isvirtual = False
    address = ""
    serialconnection = None
    logfile = None

    def __init__(self, name, address, isvirtual=False):
        self.name = name
        self.address = address
        self.isvirtual = isvirtual
        if isvirtual:
            #This is a dummy connection instantiate a new file
            self.logfile = open(name+'.log','w') 
        else:
            #This is a real connection do the serial connection
            self.connectSerial()

    def connectSerial(self):
        #instatntiate the socket object
        self.serialconnection = serial.Serial(self.address)
    
    def sendData(self, data):
        #send data through the socket object
        if self.isvirtual:
            #Write to the file
            ts = datetime.datetime.now().timestamp()
            self.logfile.write(ts, ' - ')
            self.logfile.write(data, '\n')
        else:
            #Check if connection is open
            if False != self.serialconnection.is_open():
                print("Error - ", self.address, " - Connection is closed")
                return
            
            #Send the serial data
            #TODO - Check to see if the write is happening correctly with an arudino echo script
            self.serialconnection.write(data)

    def stop(self):
        #Clean up the object
        if self.isvirtual:
            self.logfile.close()
        else:
            self.serialconnection.close()

