import socket
import sys
import struct

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 51515  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um soquete TCP/IP
dest = (HOST, PORT)  # Conecta o soquete na porque onde o server esta escutando
tcp.connect(dest)

print 'Para sair use CTRL+X\n'
caracter = raw_input()  # Le 'inc' ou 'dec' do teclado
tcp.send(caracter)
# if caracter == 'dec':
#     tcp.send('-')  # Envia comando para decrementar o contador
# elif caracter == 'inc':
#     tcp.send('+')  # Envia comando para incrementar o contador
# else:
#     sys.exit('Error!')  # Exibe erro caso usuario nao digite 'inc' ou 'dec'

contadorCodificado = tcp.recv(1024)
print contadorCodificado

contadorTupla = struct.unpack('!i', contadorCodificado)

contador = contadorTupla[0]

print contador

if contador >= 0 and contador < 10:
    contadorEnviar = '00' + str(contador)
elif contador > 9 and contador < 100:
    contadorEnviar = '0' + str(contador)
else:
    contadorEnviar = str(contador)

tcp.send(contadorEnviar[0])
tcp.send(contadorEnviar[1])
tcp.send(contadorEnviar[2])

tcp.close()