import socket
from datetime import datetime

from functions import selecionar_loja, selecionar_periodo

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

        retornoPeriodo = selecionar_periodo()
        data_inicial = retornoPeriodo[0]
        data_final = retornoPeriodo[1]

        envio = f'{mensagem};1;{data_inicial};{data_final}'.encode(
            "UTF-8")

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
