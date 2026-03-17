#Servidor
import socket

HOST = "0.0.0.0"
PORT = 9008

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    #Aguardando jogadores entrarem
    print("Aguardando Jogador 1.")
    conn_1, addr_1 = s.accept()
    conn_1.sendall("[Server] Ok. Você é o Jogador 1.".encode)
    conn_1.sendall("[Server] Aguardando Jogador 2.".encode)

    print("Aguardando jogador 2.")
    conn_2, addr_2 = s.accept()
    conn_2.sendall("[Server] Ok. Você é o Jogador 2".encode)
    conn_2.sendall("Vez do Jogador 1: ".encode)
    jogador_2 : (encode)


    conn_1.close()
    conn_2.close()