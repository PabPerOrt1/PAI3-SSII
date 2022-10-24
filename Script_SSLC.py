from socket import *
import ssl,sys

hostname = 'localhost'
context = ssl.create_default_context()
#context.load_verify_locations('path/to/cabundle.pem')

IPServidor = "localhost"
puertoServidor = 8443
socketCliente=socket(AF_INET, SOCK_STREAM, 0)

with socketCliente as sock:
    with context.wrap_socket(sock, server_hostname=IPServidor) as ssock:
        
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