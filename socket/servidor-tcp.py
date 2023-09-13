from socket import socket, AF_INET, SOCK_STREAM

server_port = 12001

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(('', server_port))

server_socket.listen(1)

print("Servidor pronto!")

while True:
    connection_socket, addr = server_socket.accept()
    msg = connection_socket.recv(1024).decode()
    msg_modificada = msg.upper()
    connection_socket.send(msg_modificada.encode())
    connection_socket.close()