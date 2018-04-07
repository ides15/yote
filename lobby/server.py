"""
yote init yote.rocks/12345
    in db: /12345
    in config: /12345

yote start
    starts a lobby at yote.rocks:8080/12345
    connects user to that lobby

yote connect
    connects a user to the lobby at yote.rocks:8080/12345

"""

import socket
import threading
import sys


class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    def __init__(self):
        self.sock.bind(("0.0.0.0", 10000))
        self.sock.listen(1)

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                print(str(a[0]) + ":" + str(a[1]), "disconnected")
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0]) + ":" + str(a[1]), "connected")


if __name__ == "__main__":
    server = Server()
    server.run()
