import json
from pprint import pprint

from autobahn.asyncio.websocket import WebSocketServerProtocol


class YoteServerProtocol(WebSocketServerProtocol):
    def onOpen(self):
        print("protocol onOpen")
        self.factory.register(self)

    def onMessage(self, payload, isBinary):
        print("protocol onMessage")
        if not isBinary:
            msg = payload.decode("utf8")
            msg = json.loads(msg)
            pprint(msg)
            self.factory.broadcast(json.dumps(msg, ensure_ascii=False))

    def connectionLost(self, reason):
        print("protocol connectionLost")
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)
