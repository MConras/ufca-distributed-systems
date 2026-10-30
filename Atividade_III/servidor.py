import socket
import threading

clientes = []

def transmitir(mensagem, conexao_origem):
    for cliente in clientes:
        if cliente != conexao_origem:
            try:
                cliente.send(mensagem)
            except:
                remover_cliente(cliente)

def remover_cliente(cliente):
    if cliente in clientes:
        clientes.remove(cliente)
        cliente.close()

def lidar_cliente(cliente, endereco):
    while True:
        try:
            mensagem = cliente.recv(1024)
            if mensagem:
                transmitir(mensagem, cliente)
            else:
                remover_cliente(cliente)
                break
        except:
            remover_cliente(cliente)
            break

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 5000))
    servidor.listen()
    print("Servidor de Chat iniciado na porta 5000...")

    while True:
        cliente, endereco = servidor.accept()
        clientes.append(cliente)
        print(f"Nova conexão de: {endereco}")
        
        thread = threading.Thread(target=lidar_cliente, args=(cliente, endereco))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()