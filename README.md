# Peripheral Manager

The peripheral manager is a daemon that runs on the workstation that allows cloud based applications to connect to the workstation and acts as the middleware that allows tools to control the hardware connected to the workstation. This communication link is achieved using web-sockets and and then transferred to a serial communication link.

## Dev Dependencies

This project uses `poetry` to manage dependencies and the runtime (Python 3.8 and above). The following commands will can be used to set up the development environment. You can follow one of the many installation options shown one the poetry [website](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) (https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions). We recommend installing pyenv to manage your python environments (https://github.com/pyenv/pyenv)

```
# This assumes you clone the repo and have python installed on your machine

cd <project directory>
poetry install              #Creates sandbox runtime env and downloads all dependencies
pipenv shell                #Changes the terminal environment into the sandbox env, <ctrl + D> to exit
python server.py            #Runs the primary application
``` 

## HTTP Endpoint

The HTTP and SocketIO endpoint is available on port `3000`. To check if the server is working correctly, type `localhost:3000` in the browser address bar. 

## SocketIO Events

The API for managing the peripheral manager uses the SocketIO events to communicate with the peripheral manager

### send-command

Sends the command and the list of arguments that go with the command to be converted to the standard command frame.

#### Expected data
- `device name`
- `command id`
- `list of command arguments`

#### Example

```
{
    "name" : STRING,
    "command-id": INT
    "args" : [ INT ]
}
```

**Note ! - Not yet implemented**

### send-raw

Sends the raw binary command that is sent to the hardware device.

#### Expected data
- `device name`
- `binary command`

#### Example

```
{
    "name" : STRING,
    "payload": Buffer()
}
```

### list-devices

Returns the list of devices that are connected to the workstation on which the peripheral manager is running.

#### Expected data
`nil`

### rename-reference

Changes the name of the device/connection reference that is in the memory of the peripheral manager.

#### Expected data
- `old`
- `new`

#### Example

```
{
    "old" : STRING,
    "new": STRING
}
```

### list-connections

Returns the list of active connections in the peripheral manager.

#### Expected data
`nil`

### activate-connection

Creates the serial-socketio connection.

#### Expected data
- `device name`
- `device address`

#### Example

```
{
    "name" : STRING,
    "address": STRING
}
```

### deactivate-connection

Ends the serial-socketio connection. 

#### Expected data
- `device name`

#### Example

```
{
    "name" : STRING
}
```

## rx

The `rx` channels (identified by the name of the connection `<name>`) allow the user to monitor the outputs from the peripherals that are generated in the device. 

#### Example

```
socket.on('<name>', function(data){
    console.log(data);
})
```

# LICENSCE
BSD-3
