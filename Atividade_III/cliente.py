import socket
import threading
import sys

def receber_mensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024).decode('utf-8')
            print(f"\n{mensagem}")
        except:
            print("\nConexão com o servidor encerrada.")
            cliente.close()
            break

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect(('localhost', 5000))
    except:
        print("Não foi possível conectar ao servidor.")
        return

    nome = input("Digite seu nome de usuário: ")
    cliente.send(f"{nome} entrou no chat!".encode('utf-8'))

    thread_receber = threading.Thread(target=receber_mensagens, args=(cliente,))
    thread_receber.start()

    print("Você está conectado! Digite 'sair' para encerrar.")
    
    while True:
        mensagem = input("")
        if mensagem.lower() == 'sair':
            cliente.send(f"{nome} saiu do chat.".encode('utf-8'))
            cliente.close()
            sys.exit(0)
            
        mensagem_formatada = f"[{nome}]: {mensagem}"
        cliente.send(mensagem_formatada.encode('utf-8'))

if __name__ == "__main__":
    iniciar_cliente()