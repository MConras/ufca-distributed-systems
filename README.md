# Atividades de Laboratório - Sistemas Distribuídos

Resoluções das atividades práticas de Sistemas Distribuídos (Ciência da Computação - UFCA).

## Estrutura do Repositório
```text
ufca-distributed-systems/
├── Atividade_I/
│   ├── letra_a/
│   │   ├── cliente.py
│   │   └── servidor.py
│   └── letra_b/
│       ├── cliente.py
│       └── servidor.py
├── Atividade_II/
│   ├── cliente.py
│   ├── servidor.py
│   └── requirements.txt
├── Atividade_III/
│   ├── cliente.py
│   └── servidor.py
├── .gitignore
├── LICENSE
└── README.md
```

## Pré-requisitos

Python 3.x instalado.\
Para a Atividade II, é necessário instalar a biblioteca rpyc executando o seguinte comando:
pip install rpyc\
Ou instalando via arquivo de requisitos:
pip install -r Atividade_II/requirements.txt

## Como Executar

Abra terminais separados para o servidor e para o(s) cliente(s).

### Atividade I - Letra A (Consulta de Horário)

1. Navegue para a pasta da atividade e inicie o servidor:
```python
cd Atividade_I/letra_a
python servidor.py
```
2. Abra um novo terminal, navegue para a pasta e inicie o cliente:
```python
cd Atividade_I/letra_a
python cliente.py
```

### Atividade I - Letra B (Inversão de String)

1. Navegue para a pasta da atividade e inicie o servidor:
```python
cd Atividade_I/letra_b
python servidor.py
```
2. Abra um novo terminal, navegue para a pasta e inicie o cliente:
```python
cd Atividade_I/letra_b
python cliente.py
```
### Atividade II (RPC com RPyC)

1. Navegue para a pasta da atividade e inicie o servidor:
```python
cd Atividade_II
python servidor.py
```
2. Abra um novo terminal, navegue para a pasta e inicie o cliente:
```python
cd Atividade_II
python cliente.py
```

### Atividade III (Chat em Tempo Real)

1. Navegue para a pasta da atividade e inicie o servidor do chat:
```python
cd Atividade_III
python servidor.py
```
2. Para simular múltiplos utilizadores, abra dois ou mais terminais adicionais e inicie o cliente em cada um deles:
```python
cd Atividade_III
python cliente.py
```