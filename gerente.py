import socket
from datetime import datetime

from funcionario import data_valida

HOST = "localhost"
PORT = 9000

gerente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serv = (HOST, PORT)

while (True):
    print(f'''
    {"-" * 20} GERENTE {"-" * 20}
    Nº \t| ESCOLHA
    1 \t| Total de Vendas (Vendedor)
    2 \t| Total de Vendas (Loja)
    3 \t| Total de Vendas (Loja/Periodo)
    4 \t| Melhor Vendedor
    5 \t| Melhor Loja
    6 \t| Encerrar gerente
    {"-" * 49}
    ''')

    mensagem = input("Escolha: ")

    if mensagem == '1':

        envio = f'{mensagem};1'.encode("UTF-8")

        gerente.sendto(envio, serv)

        msg, endereco = gerente.recvfrom(9000)
        resposta = msg.decode("UTF-8")

        print(resposta)

    elif mensagem == '2':

        envio = f'{mensagem};1'.encode("UTF-8")

        gerente.sendto(envio, serv)

        msg, endereco = gerente.recvfrom(9000)
        resposta = msg.decode("UTF-8")

        print(resposta)

    elif mensagem == '3':

        id_loja = 0
        while id_loja <= 0 or id_loja > 5:
            print('''
            Nº \t| NOME DA LOJA
            1 \t| Americansa
            2 \t| Amazilviz
            3 \t| Burguer Rei
            4 \t| McRonalds
            5 \t| Cacau Choco
            ''')
        id_loja = int(input("Selecione a loja: "))

        data_inicial = input(
            "Digite a data inicial do período(Ex: 01/01/2022): ")

        envio = f'{[id_loja, ]};1'.encode("UTF-8")

        gerente.sendto(envio, serv)

        msg, endereco = gerente.recvfrom(9000)
        resposta = msg.decode("UTF-8")

        print(resposta)

    elif mensagem == '4':

        envio = f'{mensagem};1'.encode("UTF-8")

        gerente.sendto(envio, serv)

        msg, endereco = gerente.recvfrom(9000)
        resposta = msg.decode("UTF-8")

        print(resposta)

    elif mensagem == '5':

        envio = f'{mensagem};1'.encode("UTF-8")

        gerente.sendto(envio, serv)

        msg, endereco = gerente.recvfrom(9000)
        resposta = msg.decode("UTF-8")

        print(resposta)

    elif mensagem == '6':
        print("Saindo...")
        break

gerente.close()
