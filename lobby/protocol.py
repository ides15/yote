import json
import sqlite3

from autobahn.asyncio.websocket import WebSocketServerProtocol

# connects to db and causes sqlite to run on multithreaded system (supporting Flask)
conn = sqlite3.connect("yote.db", check_same_thread=False)
c = conn.cursor()


class YoteServerProtocol(WebSocketServerProtocol):
    # When the socket is opened, register the user
    # and broadcast the list of connections to all
    # currently connected users.
    def onOpen(self):
        c.execute(
            "INSERT INTO clients(client) VALUES (?)", (self.peer, ))
        conn.commit()

        self.factory.register(self)
        self.factory.broadcast(self, None)

    # When the socket receives a message, broadcast
    # the message to all clients connected to the server.
    def onMessage(self, payload, isBinary):
        if not isBinary:
            self.factory.broadcast(self, payload)

    # When the socket connection is closed, unregister that
    # client and broadcast the list of connections to all
    # currently connected users.
    def onClose(self, wasClean, code, reason):
        self.factory.unregister(self)
        self.factory.broadcast(self, None)
