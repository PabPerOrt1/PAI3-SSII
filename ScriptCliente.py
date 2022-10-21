from socket import *
import sys

with open("Config.config") as configfile:
        ip_elegido =  configfile.readline().rstrip()
IPServidor = ip_elegido.replace("ip_cliente=","")

puertoServidor = 10000

#se decaran e inicializaran los valores del socket del cliente
socketCliente = socket(AF_INET, SOCK_STREAM)
socketCliente.connect((IPServidor,puertoServidor))

while True:
    #escribimos el mensaje
    mensaje = input()
    if mensaje != 'adios' :

        #enviamos mensaje
        socketCliente.send(mensaje.encode())
        #recibimos el mensaje
        respuesta = socketCliente.recv(4096).decode()
        print(respuesta)
    else:
        socketCliente.send(mensaje.encode())
        #cerramos socket
        socketCliente.close()
        sys.exit()