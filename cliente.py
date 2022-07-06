import socket
import threading

PORT = 3001
IP = '127.0.0.1'
nome = input('Digite seu nome: ')

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((IP, PORT))

def receber():
    while True:
        try:
            mensagem = cliente.recv(1024).decode('utf-8')
            if mensagem == 'NOME':
                cliente.send(nome.encode('utf-8'))
            else:
                print(mensagem)
        except:
            print('erro')
            cliente.close()
            break

def escrever():
    while True:
        mensagem = f'{nome} : {input()}'
        cliente.send(mensagem.encode('utf-8'))

receber_thread = threading.Thread(target=receber).start()
escrever_thread = threading.Thread(target=escrever).start()

