import socket
import threading
from time import sleep

HOST = "0.0.0.0"
PORT = 9002

LETRA = ''
CEP = [" " , " "]
NOME = [" " , " "]

semaforo = threading.Semaphore(0)

def atender_cliente (conn,addr,tid):
    global CEP
    global NOME

    semaforo.acquire()
 #envia as letras sorteadas aos clientes
    conn.sendall(LETRA.encode())

    #Envia a mensagem para o cliente 
    conn.sendall("CEP:".encode())

    #Aguarada a resposta

    resposta = conn.recv(1024).decode()
    print(f"Cliente {tid} respondeu: {resposta}")
    CEP(tid) = resposta

    conn.sendall("NOME:".encode())

    #Aguarada a resposta

    resposta = conn.recv(1024).decode()
    print(f"Cliente {tid} respondeu: {resposta}")
    NOME(tid) = resposta



    pass


def iniciar_servidor():
    global LETRA
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print(f"Servidor ouvindo em {HOST}:{PORT}")

         # while True:
         # Aguardar o jogador 1 
        conn1, addr1 = server.accept()

        thread1 = threading.Thread(target=atender_cliente, args=(conn1, addr1 , 0),daemon=True)
        thread1.start()
        

         # Aguardar o jogador 2
        conn2, addr2 = server.accept()

        thread2 = threading.Thread(target=atender_cliente, args=(conn2, addr2, 1),daemon=True)
        thread2.start()
        
        #sorteia uma letra
        LETRA = 'T'
        #libera o semaforo
        semaforo.release()
        semaforo.release()
        


            #Aguarda os clientes jogarem
        thread1.join()
        thread2.join()

#Observa as respostas
#Envia pontuação aos clientes




if __name__ == "__main__":
    iniciar_servidor()