from socket import socket, AF_INET, SOCK_DGRAM

server_name = 'localhost'
server_port = 12001

client_socket = socket(AF_INET, SOCK_DGRAM)

msg = input('Entre minúsculas \n')

client_socket.sendto(msg.encode(), (server_name, server_port))
msg_modificada, server_adddress = client_socket.recvfrom(2048)

print(msg_modificada.decode())
client_socket.close()