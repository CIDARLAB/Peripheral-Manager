import datetime
import threading
from threading import Thread
import serial


class Connection:


    def __init__(self, name:str = "", address:str = "", socketio = None, isvirtual: bool=False):
        self.name = name
        self.address = address
        self.isvirtual = isvirtual
        self.socketio_reference = socketio
        self.serialconnection = None
        self.logfile = None
        self.rxthread = None
        self.rx_buffer = []
        self._stopevent = threading.Event()

        if isvirtual:
            #This is a dummy connection instantiate a new file
            self.logfile = open(name+'.log','w') 
        else:
            #This is a real connection do the serial connection
            self.connect_serial()

    def connect_serial(self):
        #instatntiate the socket object
        self.serialconnection = serial.Serial(port=self.address, baudrate=1152000)
        #TODO - Need to create a async serial read/flush system
        self.rxthread = Thread(target=self.serial_rx_thread)
        self.rxthread.start()
    
    def send_data(self, data):
        #send data through the socket object
        if self.isvirtual:
            #Write to the file
            ts = datetime.datetime.now().timestamp()
            self.logfile.write(ts, ' - ')
            self.logfile.write(data, '\n')
        else:
            #Check if connection is open
            if not self.serialconnection.isOpen():
                print(self.serialconnection.isOpen())
                print("Error - ", self.address, " - Connection is closed")
                return False
            
            #Send the serial data
            #TODO - Check to see if the write is happening correctly with an arudino echo script
            self.serialconnection.write(data)

    def stop(self):
        #Clean up the object
        if self.isvirtual:
            self.logfile.close()
        else:
            self._stopevent.set()

    def serial_rx_thread(self):
        if self._stopevent.is_set():
            print("Stopping the RX thread")
            self.serialconnection.close()
            self.rxthread.join()
        else:
            buf = self.serialconnection.read(100)
            self.socketio_reference.emit(self.name, buf)