from multiprocessing import context
import ssl,sys
from socket import *

Puerto = 8443

def get_conection():
    #context = ssl.create_default_context()
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('Keys/new.pem', 'Keys/private.key')

    soc = socket()
    soc.bind(("10.100.225.22", Puerto))
    print(f"El servidor está corriendo en el puerto '{Puerto}'")
    print("Escuchando conexiones...")
    soc.listen(5)
    while True:
        ssock = context.wrap_socket(soc, server_side=True)
        conn, addr = ssock.accept()
        print("Conectando con un cliente", addr)
        while True:
        #recibimos el mensaje del 
            mensajeRecibido = conn.recv(4096).decode()
            print(mensajeRecibido)

        #esta condicion no se cumplira hasta que la cadena sea adios
            if mensajeRecibido == 'adios':
                break
        #mandamos mensaje al 
            conn.send(input().encode())

        print("Desconectado el cliente", addr)
        #cerramos conexion
        conn.close()
        sys.exit()
if __name__ == "__main__":
    get_conection()