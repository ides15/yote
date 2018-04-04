"""
yote init yote.rocks/12345
    in db: /12345
    in config: /12345

yote start
    starts a lobby at yote.rocks:8080/12345
    connects user to that lobby
    port number will increment for each NEW session created up to 8100

yote connect
    connects a user to the lobby at yote.rocks:8080/12345







"""
import socket
# import select
# import sys
# import _thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostbyname("yote.rocks"))
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# if len(sys.argv) != 3:
#     print("Correct usage: script, IP address, port number")
#     exit()

# IP_address = str(sys.argv[1])
# Port = int(sys.argv[2])

# server.bind((IP_address, Port))
# server.listen(100)

# list_of_clients = []


# def clientthread(conn, addr):
#     conn.send(b"Welcome to this chatroom!")

#     while True:
#         try:
#             message = conn.recv(2048)
#             if message:
#                 print("<" + addr[0] + ">" + message)
#                 message_to_send = "<" + addr[0] + "> " + message
#                 broadcast(message_to_send, conn)
#             else:
#                 remove(conn)
#         except:
#             continue


# def broadcast(message, connection):
#     for clients in list_of_clients:
#         if clients != connection:
#             try:
#                 clients.send(message)
#             except:
#                 clients.close()
#                 remove(clients)


# def remove(connection):
#     if connection in list_of_clients:
#         list_of_clients.remove(connection)


# while True:
#     conn, addr = server.accept()
#     list_of_clients.append(conn)

#     print(addr[0] + " connected")

#     _thread.start_new_thread(clientthread, (conn, addr))

# conn.close()
# server.close()
