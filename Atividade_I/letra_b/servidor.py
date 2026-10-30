import socket

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 8001))
    servidor.listen()
    print("Servidor de reversão de string escutando na porta 8001...")

    while True:
        conexao, endereco = servidor.accept()
        dados = conexao.recv(1024)
        
        if dados:
            texto = dados.decode('utf-8')
            texto_revertido = texto[::-1]
            conexao.sendall(texto_revertido.encode('utf-8'))
            
        conexao.close()

if __name__ == "__main__":
    iniciar_servidor()