import datetime as dt


def validar_data(data):

    data_atual = dt.date.today()
    data_atual = dt.date.strftime(data_atual, "%d/%m/%Y")
    dt.datetime.strptime(data, '%d/%m/%Y')
    try:
        if (data > data_atual):
            raise Exception('Data não pode ultrapassar a data atual')
    except ValueError:
        print('Formato de data inválido, deve ser DD/MM/AAAA \n Favor inserir data correta')
        return False
    except Exception:
        print('Data não pode ultrapassar a data atual')
        return False
    else:
        return True


def informa_valor_venda():
    valor_venda = input('Digite o valor da venda realizada: ')
    if (valor_venda != None):
        print('Valor cadastrada com sucesso!')
        return float(valor_venda)
    else:
        print('Favor informar uma data válida!')
        return None


def informa_data_venda():
    data_venda = input(
        'Digite a data que a venda foi realizada (DD/MM/YYYY): ')
    if (validar_data(data_venda)):
        print('Data cadastrada com sucesso!')
        return data_venda
    else:
        print('Favor informar uma data válida!')


def selecionar_loja():
    id_loja = 0
    while id_loja <= 0 or id_loja > 5:
        print('''
        Nº\t| NOME DA LOJA
        1 \t| Americansa
        2 \t| Amazilviz
        3 \t| Burguer Rei
        4 \t| McRonalds
        5 \t| Cacau Choco
        ''')

        try:
            id_loja = input('Digite o codigo do loja: ')
            if id_loja <= '0' or id_loja > '5':
                raise Exception('Código de loja inválido!')
            if id_loja == '1':
                loja = 'Americansa'
                return loja
            elif id_loja == '2':
                loja = 'Amazilviz'
                return loja
            elif id_loja == '3':
                loja = 'Burguer Rei'
                return loja
            elif id_loja == '4':
                loja = 'McRonalds'
                return loja
            elif id_loja == '5':
                loja = 'Cacau Choco'
                return loja
        except (RuntimeError, ValueError, TypeError, Exception):
            print('Digite um valor válido. Tente novamente')


def selecionar_periodo():
    data_inicial = input('Digite a data inicial do período (DD/MM/YYYY): ')
    data_final = input('Digite a data final do período (DD/MM/YYYY): ')

    if (validar_data(data_inicial) and validar_data(data_final)):
        if (data_final < data_inicial):
            print('Perído informado incorretamente')
        elif (data_final == data_inicial):
            print('Período cadastrado com sucesso')
            return [data_inicial, data_final]
        else:
            print('Período cadastrado com sucesso')
            return [data_inicial, data_final]


def selecionar_vendedor():
    id_vendedor = 0
    while id_vendedor <= 0 or id_vendedor > 4:
        print('''
        Nº\t| NOME FUNCIONÁRIO
        1 \t| Ariane Santos
        2 \t| Gabriel Santos
        3 \t| Joao Pedro
        4 \t| Pedro Queiroz
        ''')

        try:
            id_vendedor = input('Digite o codigo do vendedor: ')
            if id_vendedor <= '0' or id_vendedor > '4':
                raise Exception('Código de vendedor inválido!')
            if id_vendedor == '1':
                vendedor = 'Ariane Santos'
                return [vendedor, id_vendedor]
            elif id_vendedor == '2':
                vendedor = 'Gabriel Santos'
                return [vendedor, id_vendedor]
            elif id_vendedor == '3':
                vendedor = 'Joao Pedro'
                return [vendedor, id_vendedor]
            elif id_vendedor == '4':
                vendedor = 'Pedro Queiroz'
                return [vendedor, id_vendedor]
        except (RuntimeError, ValueError, TypeError, Exception):
            print('Digite um valor válido. Tente novamente')
