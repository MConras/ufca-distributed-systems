import socket

def solicitar_horario():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 8000))
    
    dados = cliente.recv(1024)
    print(f"Horário recebido do servidor: {dados.decode('utf-8')}")
    
    cliente.close()

if __name__ == "__main__":
    solicitar_horario()