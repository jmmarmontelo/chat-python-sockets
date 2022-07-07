
# Autor Joao Marcos Marmontelo.
# Trabalho para disciplina Sistemas Distribuidos-2022-01-GCC129.
# Codigo que represnta o cliente, possui as seguintes funcoes:
# Primeira conectar ao servidor.
# Segunda enviar mensagens ao servidor.
# Terceira receber mensagens do servidor em paraleo com a segunda funcao.

import socket
import threading


def main(): 
    # Objeto do tipo socket TCP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectando ao servidor
        cliente.connect(('127.0.0.1',5555))
    except:
        return print('Nao foi possivel conectar ao servidor')
    
    nome = input('Digite seu nome: ')

    # Thread que recebe as mensagens do servidor.
    thread_receber = threading.Thread(target=receberMensagens,args=[cliente]).start()
    # Thread que envia as mensagens ao servidor.
    thread_enviar = threading.Thread(target=enviarMensagens, args=[cliente,nome]).start()

# Metodo que recebe as mensagens e printa na tela.
def receberMensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(2048).decode('utf-8')
            print(mensagem +'\n')
        except:
            print('Nao foi possivel estabelecer conexao')
            cliente.close()
            break
# Metodo que envia as mensagens ao servidor.
def enviarMensagens(cliente, nome):
    while True:
        try:
            mensagem = input()
            cliente.send(f'{nome}> {mensagem}'.encode('utf-8'))
        except:
            return

main()