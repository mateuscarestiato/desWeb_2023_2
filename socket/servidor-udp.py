from socket import socket, AF_INET, SOCK_DGRAM

server_port = 12000

server_socket = socket(AF_INET, SOCK_DGRAM)

server_socket.bind(('', server_port))

print("Servidor pronto!")

while True:
 msg, client_address = server_socket.recvfrom(2048)
 msg_modificada = msg.decode().upper()
 server_socket.sendto(msg_modificada.encode(), client_address)