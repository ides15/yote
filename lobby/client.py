import socket
import threading
import sys


class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, address, port):
        self.sock.connect((address, port))

        iThread = threading.Thread(target=self.send_msg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data, "utf-8"))

    def send_msg(self):
        while True:
            self.sock.send(bytes(input(""), "utf-8"))


if __name__ == "__main__":
    Client(sys.argv[1], 10000)