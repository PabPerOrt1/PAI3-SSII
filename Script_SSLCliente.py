from socket import *
import ssl,sys

IPServidor = "10.100.225.22"
puertoServidor = 8443

def client_conect():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations('Keys/new.pem')


    soc=socket()
    conex_wrap = context.wrap_socket(soc, server_hostname=IPServidor)
    conex_wrap.connect((IPServidor,puertoServidor))
    print("Conexión exitosa...")
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