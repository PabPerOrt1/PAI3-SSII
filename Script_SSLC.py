from socket import *
import ssl,sys


context = ssl.create_default_context()
#context.load_verify_locations('path/to/cabundle.pem')

IPServidor = "10.100.224.222"
puertoServidor = 8443
socketCliente=socket(AF_INET, SOCK_STREAM, 0)

conex_wrap = context.wrap_socket(socketCliente, server_hostname=IPServidor)
conex_wrap.connect((IPServidor,puertoServidor))
while True:
    #escribimos el mensaje
    mensaje = input()
    if mensaje != 'adios':
        #enviamos mensaje
        conex_wrap.send(mensaje.encode())
        #recibimos el mensaje
        respuesta = conex_wrap.recv(4096).decode()
        print(respuesta)
    else:
        conex_wrap.send(mensaje.encode())
        #cerramos socket
        conex_wrap.close()
        sys.exit()