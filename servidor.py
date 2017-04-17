# Aluno: Victor Vilaca de Freitas
# Matricula: 2012055332

import socket
import sys
import struct

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 51515  # Porta que o Servidor esta

contador = 0  # Inicializando o contador

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    tcp.settimeout(10)

    caracter = con.recv(3)  # Recebe o caracter do cliente

    if caracter == 'inc':
        if contador == 999:  # Caso o contador seja 999 e receba um incremento, ele volta pra 0
            contador = 0
        else:
            contador += 1  # Incrementa um digito no contador
    elif caracter == 'dec':
        if contador == 0:  # Caso o contador seja 0 e receba um decremento, ele sobe pra 999
            contador = 999
        else:
            contador -= 1  # Decrementa um digito no contador
    else:
        print contador  # Imprime o valor atual do contador, caso receba um parametro invalido
        sys.exit('Erro! Parametro invalido.\n')  # Exibe mensagem de erro

    con.send(struct.pack('!i', contador))  # Envia o valor do contador codificado

    # Recebe tres caracteres (na ordem: centena, dezena, unidade) confirmando o valor do contador
    contadorFinal = con.recv(1)
    contadorFinal = contadorFinal+con.recv(1)
    contadorFinal = contadorFinal+con.recv(1)

    # Imprime o novo valor do contador
    print contadorFinal

    # Fecha a conexao
    con.close()