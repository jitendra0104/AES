import socket
import DES

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost',5000))


    while True:
        message = input("Message: ")
        client_socket.send(DES.aes_encrypt(message).encode())
        if message.lower() == 'exit':
            break
        response = client_socket.recv(1024).decode()
        print("Server:", DES.aes_decrypt(response))

    client_socket.close() 