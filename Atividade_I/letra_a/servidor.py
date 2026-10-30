import socket
import threading
from datetime import datetime

def lidar_cliente(conexao, endereco):
    try:
        horario_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conexao.sendall(horario_atual.encode('utf-8'))
    finally:
        conexao.close()

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 8000))
    servidor.listen()
    print("Servidor de horário multithread escutando na porta 8000...")

    while True:
        conexao, endereco = servidor.accept()
        thread = threading.Thread(target=lidar_cliente, args=(conexao, endereco))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()