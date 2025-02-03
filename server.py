import socket
import DES

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost',5000))
    server_socket.listen(1)
    print("Server is listening...")
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'exit':
            break
        decrypted = DES.aes_decrypt(data)
        print("Client:", decrypted)
        reply = input("Reply: ")
        conn.send(DES.aes_encrypt(reply).encode())

    conn.close()
    server_socket.close() 