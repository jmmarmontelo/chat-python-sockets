# Autor Joao Marcos Marmontelo
# Trabalho para disciplina Sistemas Distribuidos-2022-01-GCC129
# Codigo responssavel pelo servidor, ele faz duas funções em paralelo.
# Primeira é receber mensagens dos clientes.
# Segunda enviar transmitir as mensagens para todos os clientes.


import socket
import threading

# Varavel que armazena todos os sockets dos clientes.
clientes = []

def main():
    # Objeto do tipo Socket TCP 
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Metodo bind, representa a interface de concexao, caso necessario basta apenas mudar os parametros.
        servidor.bind(('127.0.0.1',5555))
        # Metodo listen, escuta as conexoes, onde o parametro limita a quantiade de conexoes.
        servidor.listen(20)
        print('Servidor online')
    except:
        return print('Nao foi possivel iniciar o servidor')
    # While aceita as novas conexoes e abre uma thread para cada cliente e adiciona o cliente ao vetor de clientes.
    while True:
        cliente, endereco = servidor.accept()
        clientes.append(cliente)
        threadLidar = threading.Thread(target=lidarMensagens, args=[cliente]).start()
 
# Metodo responsavel por receber as mensagens, enviar para todos os clientes e remover os clientes offline.
def lidarMensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(2018)
            transmissor(mensagem,cliente)
        except:
            deletarCliente(cliente)
            break

# Metodo responsavel por enviar a mensagem ao cliente.
def transmissor(mensagem, cliente):
    for clienteI in clientes:
        try:
            clienteI.send(mensagem)
        except:
            deletarCliente(clienteI)

# Metodo responsavel por remover o cliente da lista de clientes ativos.
def deletarCliente(cliente):
    clientes.remove(cliente)

main()