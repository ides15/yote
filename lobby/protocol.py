from autobahn.asyncio.websocket import WebSocketServerProtocol


class YoteServerProtocol(WebSocketServerProtocol):
    def onOpen(self):
        print("protocol onOpen")
        self.factory.register(self)

    def onMessage(self, payload, isBinary):
        print("protocol onMessage")
        if not isBinary:
            msg = "{} from {}".format(payload.decode("utf8"), self.peer)
            self.factory.broadcast(msg)

    def connectionLost(self, reason):
        print("protocol connectionLost")
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)
