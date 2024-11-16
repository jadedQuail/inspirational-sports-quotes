# Inspirational Quotes Microservice

This is a microservice that provides the consumer with a random sports quote based on specifications given via a filters object argument.

**NOTE:** All example code below is done in Python.

## How to requst data

A client program can request data by first constructing a ZMQ Context object and then creating a socket from this context. Then, the socket must connect to the same port that the service is running on (by default, this port is `9876`):

```
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:9876")
```

From there, the client must construct a request to send via the socket's `send_json()` method. The request can include a `filters` argument, if desired, or this can be left empty:

```
filters = {
    "sport": "Hockey",
    "mood": "Motivational"
}

request = {"filters": filters or {}}

socket.send_json(request)
```
