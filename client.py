import socket
import time

host_name = "localhost"
port = 7777

internet_socket = socket.socket()
internet_socket.connect((host_name, port))

print("Connection Successful! Host Name: {}:{}".format(host_name, port))

message = input("----::")
print("Waiting for server...")

while message != "END":
    internet_socket.send(message.encode())
    incoming_data = internet_socket.recv(1024).decode()

    print("SERVER: " + incoming_data)
    
    message = input("---::")    
    print("Waiting for server...")

internet_socket.close()