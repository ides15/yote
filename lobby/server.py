import socket
import threading
import sys


class Server:
    # create socket using TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # create list of connections, consists
    # of 3-tuple of (socket object, address, session_url)
    connections = []

    # on server class init, bind socket
    # to the ip address and port and listen
    def __init__(self, ip, port):
        self.sock.bind((ip, port))
        self.sock.listen(1)

    # handles connected socket data
    def handler(self, c, a, session_url):
        while True:
            # a socket sends data to the server
            data = c.recv(1024)

            for connection in self.connections:
                # if the socket sending data matches the current
                # connection, don't send that data back to that socket
                if connection[0] != c:

                    # if the session_url of the socket sending data
                    # matches the session_url of the current connection,
                    # send the data to that socket. Otherwise, don't send
                    # the data to that socket.

                    # This ensures that users with unique session_urls
                    # only send data to and receive data from users
                    # with matching session_urls
                    if connection[2] == session_url:
                        connection[0].send(data)

            # if the socket sends a disconnect signal
            if not data:
                print(str(a[0]) + ":" + str(a[1]),
                      " disconnected from session", session_url)

                # remove the 3-tuple from the connections list
                self.connections.remove((c, a, session_url))

                # close the connection
                c.close()

                # stop the thread
                break

    def run(self):
        while True:
            # accepts a socket connection
            c, a = self.sock.accept()

            # on connection acceptance, the new socket
            # sends the server the client's session_url
            session_url = c.recv(1024)

            # server starts a thread for the client
            cThread = threading.Thread(
                target=self.handler, args=(c, a, session_url))
            cThread.daemon = True
            cThread.start()

            # appends the 3-tuple (socket object, address, session_url)
            # to the connections list
            self.connections.append((c, a, session_url))
            print(str(a[0]) + ":" + str(a[1]),
                  "connected to session", session_url)


if __name__ == "__main__":
    server = Server("localhost", 10000)
    server.run()
