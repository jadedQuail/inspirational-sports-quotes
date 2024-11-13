import zmq
import signal

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:9876")

signal.signal(signal.SIGINT, signal.SIG_DFL)

def request_quote(filters=None):
    request = {"filters": filters or {}}

    socket.send_json(request)

    response = socket.recv_json()
    return response

############################################

# Example 1 - No filters
response = request_quote()
print("Response:", response)


# Example 2 - One filter
response = request_quote({
    "sport": "Tennis"
})
print("Response:", response)

# Example 3 - Two filters
response = request_quote({
    "sport": "Hockey",
    "mood": "Motivational"
})
print("Response:", response)
