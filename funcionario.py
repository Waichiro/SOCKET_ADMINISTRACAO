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
                print("\033[31mDigite o formato correto da data!! Ex: (01/02/2022)\033[0;0m")
                return True
            
        else:
            print("\033[31mVocê errou várias vezes, o que deseja fazer?\033[0;0m")
            cond = int(input('''
            Nº \t| OPCAO
            1 \t| Continuar tentando
            2 \t| Sair
            '''))

            if cond == 1:
                return 'C'
            else:
                return 'S'
            
    except ValueError:
        print("\033[31mDigite o formato correto da data!! Ex: (01/02/2022)\033[0;0m")
        return True

HOST = "localhost"
PORT = 9000

func = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serv = (HOST, PORT)

while(True):
    print('''
		Nº \t| Escolha:
		1 \t| Fazer venda
		2 \t| Encerrar funcionario
	''')

    mensagem = input("Digite o número da opção que deseja realizar: ")

    if mensagem == '1':
        
        cod_venda = random.randint(1, 99999)

        id_vendedor = 0
        while id_vendedor <= 0 or id_vendedor > 4:
            print('''
            Nº \t| NOME FUNCIONARIO
            1 \t| Ariane Santos
            2 \t| Gabriel Santos
            3 \t| Joao Pedro
            4 \t| Pedro Queiroz
            ''')

            id_vendedor = int(input("Digite o codigo do vendedor: "))

            if id_vendedor <= 0 or id_vendedor > 4:
                print('\033[31mDigite um valor valido!\033[0;0m')

        vendedor = "Ariane Santos" if id_vendedor == 1 else "Gabriel Santos" if id_vendedor == 2 else "Joao Pedro" if id_vendedor == 3 else "Pedro Queiroz"

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

            id_loja = int(input("Digite o número da loja para completar a venda: "))

            if id_loja <= 0 or id_loja > 5:
                print('\033[31mDigite um valor valido!\033[0;0m')

        loja = "Americansa" if id_loja == 1 else "Amazilviz" if id_loja == 2 else "Burguer" if id_loja == 3 else "McRonalds" if id_loja == 4 else "Cacau Choco"

        res = True
        count = 0
        valor_venda = None
        while(res):
            data_venda = input("Digite a data da venda(Ex: 01/01/2022): ")
            count += 1
            res = data_valida(data_venda)
            if (res == "C"):
                count = 0
                res = True
            elif res == "S":
                res = False
                
            elif type(res) == float:
                valor_venda = res
                res = False

  
        
        
        if valor_venda != None:
            envio = f'{mensagem};0;{cod_venda};{vendedor};{loja};{data_venda};{round(valor_venda, 2)};{id_vendedor}'.encode("UTF-8")


            func.sendto(envio, serv)

            msg, endereco = func.recvfrom(9000)
            resposta = msg.decode("UTF-8")

            print(resposta)

        else:
            print("\033[31mA venda foi cancelada!!\033[0;0m")


    elif mensagem == '2':
        print("Saindo...")
        break

func.close()