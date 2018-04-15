import asyncio
import websockets
from pprint import pprint


class Server:
    def __init__(self, address, port):
        self.start_server = websockets.serve(
            self.connection_handler, address, port)
        self.connections = set()

    def run(self):
        asyncio.get_event_loop().run_until_complete(self.start_server)
        asyncio.get_event_loop().run_forever()

    async def connection_handler(self, websocket, path):
        self.connections.add(websocket)

        for connection in self.connections:
            await connection.send("async test")


if __name__ == "__main__":
    server = Server("localhost", 10000)
    server.run()
