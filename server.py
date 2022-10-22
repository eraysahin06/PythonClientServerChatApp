import socket
import time

host_name = "localhost"
port = 7777
internet_socket = socket.socket()
#localhost = 7777
internet_socket.bind((host_name, port))
internet_socket.listen(1)

connection, address = internet_socket.accept()
print(str(address) + "Connection Successful.")

while True:
    while True:
        try:
            incoming_data = str(connection.recv(1024).decode())
            print("Client Message: " + incoming_data)
            break
        except ConnectionResetError:
            time.sleep(2)
            connection, address = internet_socket.accept()
            print(str(address) + "Connection Successful.")
        if incoming_data == "END":
            break
        else:
            message = input("----::")
            print("waiting for client...")
            connection.send(message.encode())


connection.close()  