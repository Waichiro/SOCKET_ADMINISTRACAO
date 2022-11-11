import socket 
import random
from datetime import datetime


def data_valida(data):
    try:
        if(count < 5):
            val_data = bool(datetime.strptime(data, '%d/%m/%Y'))
            if(val_data == True):
                valor_venda = input("Digite o valor da venda: R$")
                retorno = valor_venda.replace(",", ".")
                return float(retorno)
            else:
                return True
            
        else:
            cond = int(input('''
            Nº \t\t| OPCAO
            1 \t\t| Continuar tentando
            2 \t\t| Sair
            '''))

            if cond == 1:
                return 'C'
            else:
                return False
            
    except ValueError:

        return True

HOST = "localhost"
PORT = 9000

func = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serv = (HOST, PORT)

while(True):
    print('''
		Escolha:
		1. Fazer venda
		2. Encerrar funcionario
	''')

    mensagem = input("Escolha: ")

    if mensagem == '1':
        
        cod_venda = random.randint(1, 99999)

        nome_vendedor = input("Digite o nome do vendedor: ")

        id_loja = 0
        while id_loja <= 0 or id_loja > 5:
            print('''
            Nº \t\t| NOME DA LOJA
            1 \t\t| Americansa
            2 \t\t| Amazilviz
            3 \t\t| Burguer Rei
            4 \t\t| McRonalds
            5 \t\t| Cacau Choco
            ''')

            id_loja = int(input("Digite o número da loja para completar a venda: "))

        loja = "Americansa" if id_loja == 1 else "Amazilviz" if id_loja == 2 else "Burguer" if id_loja == 3 else "McRonalds" if id_loja == 4 else "Cacau Choco"

        res = True
        count = 0

        while(res):
            data_venda = input("Digite a data da venda(Ex: 01/01/2022): ")
            count += 1
            res = data_valida(data_venda)
            if (res == "C"):
                count = 0
                res = True

                
            elif type(res) == float:
                valor_venda = res
                res = False

  
        
        

        envio = f'{mensagem};0;{cod_venda};{nome_vendedor};{id_loja};{data_venda};{round(valor_venda, 2)}'.encode("UTF-8")


        func.sendto(envio, serv)

        msg, endereco = func.recvfrom(9000)
        resposta = msg.decode("UTF-8")

        print(resposta)


    elif mensagem == '2':
        print("Saindo...")
        break

func.close()