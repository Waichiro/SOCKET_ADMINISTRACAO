import random
import socket

from functions import *

HOST = "localhost"
PORT = 9000

func = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serv = (HOST, PORT)

while (True):
    print(f'''
    {"-" * 18} FUNCIONARIO {"-" * 18} 
    | Nº\t| Escolha
    | 1 \t| Fazer venda
    | 2 \t| Encerrar funcionario
    {"-" * 49}
	''')

    mensagem = input("Digite o número da opção que deseja realizar: ")

    if mensagem == '1':

        cod_venda = random.randint(13, 99999)

        retornoVendedor = selecionar_vendedor()

        vendedor = retornoVendedor[0]
        id_vendedor = retornoVendedor[1]

        loja = selecionar_loja()

        data_venda = informa_data_venda()

        valor_venda = informa_valor_venda()

        if valor_venda != None:
            envio = f'{mensagem};0;{cod_venda};{vendedor};{loja};{data_venda};{round(valor_venda, 2)};{id_vendedor}'.encode(
                "UTF-8")

            func.sendto(envio, serv)

            msg, endereco = func.recvfrom(9000)
            resposta = msg.decode("UTF-8")

            print(resposta)

        else:
            print('A venda foi cancelada!!')

    elif mensagem == '2':
        print("Saindo...")
        break

func.close()
