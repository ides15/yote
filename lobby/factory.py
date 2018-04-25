import json
from pprint import pprint

from autobahn.asyncio.websocket import WebSocketServerFactory


class YoteServerFactory(WebSocketServerFactory):
    def __init__(self, url):
        WebSocketServerFactory.__init__(self, url)
        self.clients = []

    # Handles the registration of clients requesting access
    # to the server.
    def register(self, client):
        if client not in self.clients:
            print("registered client {}".format(client.peer))
            self.clients.append(client)

    # Handles the unregistration of clients that have lost
    # connection to the server.
    def unregister(self, client):
        if client in self.clients:
            print("unregistered client {}".format(client.peer))
            self.clients.remove(client)

    # Handles sending messages to all clients connected to the server.
    def broadcast(self, origin, msg):
        # If the msg parameter is None, send the list of connections to 
        # all users connected to the server.
        if msg is None:
            msg = json.dumps({
                "connections": [client.peer for client in self.clients]
            }).encode()

            for c in self.clients:
                c.sendMessage(msg)
        
        # If the msg parameter is not None, send the msg parameter
        # to all the clients that are not the origin client (sender).
        for c in self.clients:
            if c is not origin:
                c.sendMessage(msg)
