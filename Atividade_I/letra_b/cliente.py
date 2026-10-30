import socket

def enviar_string():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 8001))
    
    mensagem = "Olá, Mundo Distribuído"
    print(f"Enviando: {mensagem}")
    cliente.sendall(mensagem.encode('utf-8'))
    
    dados = cliente.recv(1024)
    print(f"Resposta revertida: {dados.decode('utf-8')}")
    
    cliente.close()

if __name__ == "__main__":
    enviar_string()