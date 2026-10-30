import rpyc
from rpyc.utils.server import ThreadedServer
from datetime import datetime

class ServicoHorario(rpyc.Service):
    def exposed_obter_horario(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    print("Servidor RPyC escutando na porta 18861...")
    servidor = ThreadedServer(ServicoHorario, port=18861)
    servidor.start()