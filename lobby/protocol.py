import json

from autobahn.asyncio.websocket import WebSocketServerProtocol


class YoteServerProtocol(WebSocketServerProtocol):
    def onOpen(self):
        self.factory.register(self)
        self.factory.broadcast(self, None)

    def onMessage(self, payload, isBinary):
        if not isBinary:
            self.factory.broadcast(self, payload)

    def onClose(self, wasClean, code, reason):
        self.factory.unregister(self)
        self.factory.broadcast(self, None)