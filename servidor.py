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
            resposta = str(dados).encode("UTF-8")
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

                resposta = '\033[32mVenda feita com sucesso!\033[0;0m'.encode("UTF-8")
                servidor.sendto(resposta, endCliente)
            
            except: 
                resposta =  "\033[31mAlgo deu errado na venda!\033[0;0m".encode("UTF-8")
                servidor.sendto(resposta, endCliente)

        else:
            resposta = "\033[31mAlgo deu errado!\033[0;0m".encode("UTF-8")
            servidor.sendto(resposta, endCliente)

    elif comando[0] == '2':
        resposta = f'Esta é uma resposta do 2'.encode("UTF-8")
        servidor.sendto(resposta, endCliente)

    
    elif comando[0] == '3':
        resposta = f'Esta é uma resposta do 3'.encode("UTF-8")
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
    

