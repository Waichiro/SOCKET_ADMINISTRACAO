import socket

HOST = "localhost"
PORT = 9000


servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((HOST, PORT))

dados = []

while (True):
    print("Servidor Rodando...")

    msg, endCliente = servidor.recvfrom(9000)

    print(f'Cliente {endCliente} enviou mensagem')
    mensagem = msg.decode("UTF-8")

    comando = mensagem.split(';')
    check_pessoa = "gerente" if comando[1] == '1' else "funcionario" if comando[1] == '0' else "Desconhecido"

    if comando[0] == '1':
        if check_pessoa == 'gerente':
            total_ariane = 0.0
            total_gabriel = 0.0
            total_joao = 0.0
            total_pedro = 0.0

            for x in range(len(dados)):
                if dados[x]['cod_funcionario'] == '1':
                    valor = float(dados[x]['valor_venda'])
                    total_ariane += valor

                elif dados[x]['cod_funcionario'] == '2':
                    valor = float(dados[x]['valor_venda'])
                    total_gabriel += valor

                elif dados[x]['cod_funcionario'] == '3':
                    valor = float(dados[x]['valor_venda'])
                    total_joao += valor

                elif dados[x]['cod_funcionario'] == '4':
                    valor = float(dados[x]['valor_venda'])
                    total_pedro += valor

            resposta = f'''
            FUNCIONARIO \t| TOTAL
            Ariane Santos \t| {round(total_ariane, 2)}
            Gabriel Santos \t| {round(total_gabriel, 2)}
            João Pedro \t\t| {round(total_joao, 2)}
            Pedro Queiroz \t| {round(total_pedro, 2)}
            '''.encode("UTF-8")
            servidor.sendto(resposta, endCliente)

        elif check_pessoa == 'funcionario':

            try:
                data = {
                    'cod_funcionario': comando[7],
                    'cod_venda': comando[2],
                    'nome': comando[3],
                    'loja': comando[4],
                    'data_venda': comando[5],
                    'valor_venda': comando[6]
                }

                dados.append(data)

                resposta = '\033[32mVenda feita com sucesso!\033[0;0m'.encode(
                    "UTF-8")
                servidor.sendto(resposta, endCliente)

            except:
                resposta = "\033[31mAlgo deu errado na venda!\033[0;0m".encode(
                    "UTF-8")
                servidor.sendto(resposta, endCliente)

        else:
            resposta = "\033[31mAlgo deu errado!\033[0;0m".encode("UTF-8")
            servidor.sendto(resposta, endCliente)

    elif comando[0] == '2':

        total_americansa = 0.0
        total_amazilviz = 0.0
        total_burguer_rei = 0.0
        total_mcronalds = 0.0
        total_cacau_choco = 0.0

        for x in range(len(dados)):
            if dados[x]['loja'] == 'Americansa':
                valor = float(dados[x]['valor_venda'])
                total_americansa += valor

            elif dados[x]['loja'] == 'Amazilviz':
                valor = float(dados[x]['valor_venda'])
                total_amazilviz += valor

            elif dados[x]['loja'] == 'Burguer Rei':
                valor = float(dados[x]['valor_venda'])
                total_burguer_rei += valor

            elif dados[x]['loja'] == 'McRonalds':
                valor = float(dados[x]['valor_venda'])
                total_mcronalds += valor

            elif dados[x]['loja'] == 'Cacau Choco':
                valor = float(dados[x]['valor_venda'])
                total_cacau_choco += valor

        resposta = f'''
        LOJA \t\t| TOTAL
        Americansa \t| {round(total_americansa, 2)}
        Amazilviz \t| {round(total_amazilviz, 2)}
        Burguer Rei \t| {round(total_burguer_rei, 2)}
        McRonalds \t| {round(total_mcronalds, 2)}
        Cacau Choco \t| {round(total_cacau_choco, 2)}
        '''.encode("UTF-8")
        servidor.sendto(resposta, endCliente)

    elif comando[0] == '3':
        resposta = str(dados).encode("UTF-8")
        servidor.sendto(resposta, endCliente)

    elif comando[0] == '4':
        resposta = f'Esta é uma resposta do 4'.encode("UTF-8")
        servidor.sendto(resposta, endCliente)

    elif comando[0] == '5':
        resposta = f'Esta é uma resposta do 5'.encode("UTF-8")
        servidor.sendto(resposta, endCliente)

    else:
        resposta = f'ERRO'.encode("UTF-8")
        servidor.sendto(resposta, endCliente)
        break

print("Saindo...")
servidor.close()
