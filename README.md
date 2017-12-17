# Peripheral Manager

The peripheral manager is a daemon that runs on the workstation that allows cloud based applications to connect to the workstation and acts as the middleware that allows tools to control the hardware connected to the workstation. This communication link is achieved using websockets and and then transferred to a serial communication link.

## Dev Dependencies

This project uses `pipenv` to manage dependencies and the runtime (Python 3.6). The following commands will can be used to set up the development envionment.

```
# This assumes you clone the repo and have python installed on your machine

pip install pipenv          #Install pipenv 
cd <project directory>
pipenv install              #Creates sandbox runtime env and downloads all dependencies
pipenv shell                #Changes the terminal environment into the sandbox env, <ctrl + D> to exit
pip freeze                  #Ensures the runtime python interpreter finds all modules
python server.py            #Runs the primary application
``` 

## SocketIO Events

The API for managing the peripheral manager uses the SocketIO events to communicate witht the perpheral manager

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

### send-raw

Sends the raw bindary command that is sent to the hardware device.

#### Expected data
- `device name`
- `binary command`

#### Example

```
{
    "name" : STRING,
    "command": Buffer()
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
- `device address`

#### Example

```
{
    "name" : STRING
}
```

## rx

The `rx` channels allow the user to monitor the outputs from the peripherals that are generated in the device. 

## TODOS:

1. Testing of Socket-Serial interface
1. Integration of command generation from David's project
1. HTML Management UI
1. Error catching and failure reporting
1. Packaging/Porting Test