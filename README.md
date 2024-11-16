# Inspirational Quotes Microservice

This is a microservice that provides the consumer with a random sports quote based on specifications given via a filters object argument.

**NOTE:** All example code below is done in Python.

## How to request data

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

## How to receive data

The client program can then receive data by calling the socket's `recv_json()` method to receive a JSON object response that will contain a quote object with a status code, a message (on whether or not the request was successful) and the actual data. The JSON object received will be transposed into the closest equivalent object in the client's programming language (in the case of Python, this would be a dictionary):

```
response = socket.recv_json()
print(response)

# Expected result:
{
    'code': 200,
    'data':
    {
        'quote': "You miss 100% of the shots you don't take.",
        'author': 'Wayne Gretzky',
        'sport': 'Hockey',
        'mood': 'Motivational'
    },
    'message': 'Quote successfully returned.'
}
```

## Filter Values

| Filtering Option  | Possible Values                                                                                     |
|-------------------|-----------------------------------------------------------------------------------------------------|
| Sport             | Basketball, Hockey, Tennis, Track and Field, Boxing, Football, Baseball, Swimming, Golf, Soccer     |
| Mood              | Motivational, Overcoming Failure, Funny, Dealing with Anxiety, Teamwork                             |

## UML Diagram










