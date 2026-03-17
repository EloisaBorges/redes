# Cliente
import socket

HOST = "192.168.246.42"
PORT = 9006

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    while True:
        msg = input("Cliente: ")
        s.sendall(msg.encode)
   
        msg_recv =s.recv(1024).decode()
        print("Servidor:" ,msg_recv)