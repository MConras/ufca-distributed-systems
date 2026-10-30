import rpyc

def solicitar_horario():
    conexao = rpyc.connect("localhost", 18861)
    horario = conexao.root.obter_horario()
    print(f"Horário recebido via RPyC: {horario}")
    conexao.close()

if __name__ == "__main__":
    solicitar_horario()