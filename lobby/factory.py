import json
from pprint import pprint

from autobahn.asyncio.websocket import WebSocketServerFactory


class YoteServerFactory(WebSocketServerFactory):
    def __init__(self, url):
        WebSocketServerFactory.__init__(self, url)
        self.clients = []

    def register(self, client):
        if client not in self.clients:
            print("registered client {}".format(client.peer))
            self.clients.append(client)

    def unregister(self, client):
        if client in self.clients:
            print("unregistered client {}".format(client.peer))
            self.clients.remove(client)

    def broadcast(self, origin, msg):
        for c in self.clients:
            if c is not origin:
                c.sendMessage(msg)
