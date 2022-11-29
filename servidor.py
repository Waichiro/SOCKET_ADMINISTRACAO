import socket

HOST = "localhost"
PORT = 9000


servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((HOST, PORT))

dados = [{'cod_funcionario': '1', 'cod_venda': '1', 'nome': 'Ariane Santos', 'loja': 'Americansa', 'data_venda': '01/01/2022', 'valor_venda': '1000.0'},
         {'cod_funcionario': '1', 'cod_venda': '2', 'nome': 'Ariane Santos',
             'loja': 'Americansa', 'data_venda': '01/02/2022', 'valor_venda': '1000.0'},
         {'cod_funcionario': '1', 'cod_venda': '3', 'nome': 'Ariane Santos',
             'loja': 'Americansa', 'data_venda': '01/03/2022', 'valor_venda': '1000.0'},
         {'cod_funcionario': '1', 'cod_venda': '4', 'nome': 'Ariane Santos',
             'loja': 'Americansa', 'data_venda': '01/04/2022', 'valor_venda': '1000.0'},
         {'cod_funcionario': '1', 'cod_venda': '5', 'nome': 'Ariane Santos',
             'loja': 'Americansa', 'data_venda': '01/05/2022', 'valor_venda': '1000.0'},
         {'cod_funcionario': '1', 'cod_venda': '6', 'nome': 'Ariane Santos',
             'loja': 'Americansa', 'data_venda': '01/06/2022', 'valor_venda': '1000.0'},
         {'cod_funcionario': '1', 'cod_venda': '7', 'nome': 'Ariane Santos',
             'loja': 'Americansa', 'data_venda': '01/07/2022', 'valor_venda': '1000.0'},
         {'cod_funcionario': '1', 'cod_venda': '8', 'nome': 'Ariane Santos', 'loja': 'Americansa', 'data_venda': '01/08/2022', 'valor_venda': '1000.0'}, {
             'cod_funcionario': '1', 'cod_venda': '9', 'nome': 'Ariane Santos', 'loja': 'Americansa', 'data_venda': '01/09/2022', 'valor_venda': '1000.0'},
         {'cod_funcionario': '1', 'cod_venda': '10', 'nome': 'Ariane Santos',
             'loja': 'Americansa', 'data_venda': '01/10/2022', 'valor_venda': '1000.0'},
         {'cod_funcionario': '1', 'cod_venda': '11', 'nome': 'Ariane Santos',
             'loja': 'Americansa', 'data_venda': '01/11/2022', 'valor_venda': '1000.0'}, ]

while (True):
    print("Servidor Rodando...")

    msg, endCliente = servidor.recvfrom(9000)

    print(f'Cliente {endCliente} enviou mensagem')
    mensagem = msg.decode("UTF-8")

    comando = mensagem.split(';')

    if comando[1] == '0':
        check_pessoa = 'funcionario'
    elif comando[1] == '1':
        check_pessoa = 'gerente'
    else:
        check_pessoa = 'desconhecido'

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
                print(dados)

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

        total_americansa_periodo = 0.0
        total_amazilviz_periodo = 0.0
        total_burguer_rei_periodo = 0.0
        total_mcronalds_periodo = 0.0
        total_cacau_choco_periodo = 0.0

        data = {
            'data_inicial': comando[2],
            'data_final': comando[3]
        }

        for x in range(len(dados)):
            if dados[x]['data_venda'] >= data['data_inicial'] and dados[x]['data_venda'] <= data['data_final']:
                if dados[x]['loja'] == 'Americansa':
                    valor = float(dados[x]['valor_venda'])
                    total_americansa_periodo += valor

                elif dados[x]['loja'] == 'Amazilviz':
                    valor = float(dados[x]['valor_venda'])
                    total_amazilviz_periodo += valor

                elif dados[x]['loja'] == 'Burguer Rei':
                    valor = float(dados[x]['valor_venda'])
                    total_burguer_rei_periodo += valor

                elif dados[x]['loja'] == 'McRonalds':
                    valor = float(dados[x]['valor_venda'])
                    total_mcronalds_periodo += valor

                elif dados[x]['loja'] == 'Cacau Choco':
                    valor = float(dados[x]['valor_venda'])
                    total_cacau_choco_periodo += valor

        resposta = f'''
        PERIODO \t| {data['data_inicial']} - {data['data_final']}
        Americansa \t| {round(total_americansa_periodo, 2)}
        Amazilviz \t| {round(total_amazilviz_periodo, 2)}
        Burguer Rei \t| {round(total_burguer_rei_periodo, 2)}
        McRonalds \t| {round(total_mcronalds_periodo, 2)}
        Cacau Choco \t| {round(total_cacau_choco_periodo, 2)}
        '''.encode("UTF-8")
        servidor.sendto(resposta, endCliente)

    elif comando[0] == '4':

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

        maior = total_ariane
        vendedor = 'Ariane Gomes'

        if (total_gabriel > maior):
            maior = total_gabriel
            vendedor = 'Gabriel Santos'
        elif (total_joao > maior):
            maior = total_joao
            vendedor = 'João Pedro'
        elif (total_pedro > maior):
            maior = total_pedro
            vendedor = 'Pedro Queiroz'

        resposta = f'O melhor vendedor é {vendedor}'.encode("UTF-8")
        servidor.sendto(resposta, endCliente)

    elif comando[0] == '5':

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

        maior = total_americansa
        loja = 'Americansa'

        if (total_amazilviz > maior):
            maior = total_amazilviz
            loja = 'Amazilviz'
        elif (total_burguer_rei > maior):
            maior = total_burguer_rei
            loja = 'Burguer Rei'
        elif (total_mcronalds > maior):
            maior = total_mcronalds
            loja = 'McRonalds'
        elif (total_cacau_choco > maior):
            maior = total_cacau_choco
            loja = 'Cacau Choco'

        resposta = f'A melhor loja é {loja}'.encode("UTF-8")
        servidor.sendto(resposta, endCliente)

    else:
        resposta = f'ERRO'.encode("UTF-8")
        servidor.sendto(resposta, endCliente)
        break

print("Saindo...")
servidor.close()
