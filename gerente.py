import socket 

HOST = "localhost"
PORT = 9000

gerente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serv = (HOST, PORT)

while(True):
    print(f'''
    {"=" * 20}GERENTE{"=" * 20}
    Escolha:
    1. Total de Vendas (Vendedor) 
    2. Total de Vendas (Loja)
    3. Total de Vendas (Loja/Periodo)
    4. Melhor Vendedor
    5. Melhor Loja
    6. Encerrar gerente
    {"-" * 47}
	''')

    mensagem = input("Escolha: ")

    if mensagem == '1':
        
        envio = f'{mensagem};1'.encode("UTF-8")

        gerente.sendto(envio, serv)

        msg, endereco = gerente.recvfrom(9000)
        resposta = msg.decode("UTF-8")

        print(resposta)

    elif mensagem == '2':
        
        envio = f'{mensagem}'.encode("UTF-8")

        gerente.sendto(envio, serv)

        msg, endereco = gerente.recvfrom(9000)
        resposta = msg.decode("UTF-8")

        print(resposta)

    elif mensagem == '3':
        
        envio = f'{mensagem}'.encode("UTF-8")

        gerente.sendto(envio, serv)

        msg, endereco = gerente.recvfrom(9000)
        resposta = msg.decode("UTF-8")

        print(resposta)

    elif mensagem == '4':
        
        envio = f'{mensagem}'.encode("UTF-8")

        gerente.sendto(envio, serv)

        msg, endereco = gerente.recvfrom(9000)
        resposta = msg.decode("UTF-8")

        print(resposta)

    elif mensagem == '5':
        
        envio = f'{mensagem}'.encode("UTF-8")

        gerente.sendto(envio, serv)

        msg, endereco = gerente.recvfrom(9000)
        resposta = msg.decode("UTF-8")

        print(resposta)

    elif mensagem == '6':
        print("Saindo...")
        break

gerente.close()