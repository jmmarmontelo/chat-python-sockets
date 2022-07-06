
#Servidor responsável por receber as mensagens dos clientes
#e reenvia-las para todos os clientes

import socket
import threading

# Variaveis ip e porta para a conexao com os clientes
IP = '127.0.0.1'
PORT = 3001

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((IP, PORT))
servidor.listen(10)

clientes = []
nomes = []

def transmissor (mensagem):
    for cliente in clientes:
        cliente.send(mensagem)

def lidar(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            transmissor(mensagem)
        except:
            index = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            nome = nomes[index]
            transmissor(f'{nome} saiu do grupo'.encode('utf-8'))
            nomes.remove(nome)
            break

def receber():
    while True:
        cliente, endereco = servidor.accept()
        print(f"Conectou: {str(endereco)}")
        cliente.send('NOME'.encode('utf-8'))
        nome = cliente.recv(1024).decode('utf8')
        nomes.append(nome)
        clientes.append(cliente)
        transmissor(f'{nome} entrou no grupo'.encode('utf-8'))
        thread_lidar = threading.Thread(target=lidar, args=(cliente,)).start()


print('Servidor online')
receber()