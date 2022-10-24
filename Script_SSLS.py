import ssl,sys
from socket import *

def deal_with_client(wrap):
    mensajeRecibido = socketConexion.recv(4096).decode()
    print(mensajeRecibido)
    while True:
        #recibimos el mensaje del cliente
        mensajeRecibido = socketConexion.recv(4096).decode()
        print(mensajeRecibido)

        #esta condicion no se cumplira hasta que la cadena sea adios
        if mensajeRecibido == 'adios':
            break
        #mandamos mensaje al cliente
        socketConexion.send(input().encode())

    print("Desconectado el cliente", addr)
    #cerramos conexion
    socketConexion.close()
    sys.exit()

context = ssl.create_default_context()

# context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# context.load_cert_chain(certfile="mycertfile", keyfile="mykeyfile")

socketServidor = socket(AF_INET,SOCK_STREAM, 0)
socketServidor.bind(("", 8443))
socketServidor.listen(5)
while True:
    socketConexion, addr = socketServidor.accept()
    ssock = context.wrap_socket(socketConexion, server_side=True)
    print("Conectando con un cliente", addr)
    try:
        deal_with_client(ssock)
    finally:
        ssock.shutdown(socket.SHUT_RDWR)
        ssock.close()
