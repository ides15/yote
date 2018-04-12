import socket
import threading
import sys
import os
import json


class Client:
    # creates socket using TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # on client class init, connect to the ip address
    # and port and send the session_url to the server
    # to be added to the connections list
    def __init__(self, address, port, session_url):
        self.address = address
        self.port = port
        self.session_url = session_url

    def run(self):
        self.sock.connect((self.address, self.port))
        print("Connected to socket lobby.")
        self.sock.send(self.session_url.encode())

        # start a thread for the client to broadcast over the lobby
        iThread = threading.Thread(target=self.send_msg)
        iThread.daemon = True
        iThread.start()

        # receives information from server and prints
        # it to stdin
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data, "utf-8"))

    def send_msg(self):
        while True:
            # sends stdin to lobby to be broadcasted
            self.sock.send(bytes(input(""), "utf-8"))


# if __name__ == "__main__":
    # Client("localhost", 10000)
