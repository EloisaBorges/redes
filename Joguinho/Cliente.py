# Cliente
import socket

HOST = "192.168.246.41"
PORT = 9006

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   #Conecta com o servidor
    s.connect((HOST, PORT))

    #Recebe mensagem do servidor
    msg = s.recv(1024).decode()
    print(msg)
    msg = s.recv(1024).decode()
    print(msg)

    msg1 = input("pedra")
    print (msg1)
    msg2 = input("papel")
    print (msg2)
    msg3 = input("tesoura")
    print (msg3)