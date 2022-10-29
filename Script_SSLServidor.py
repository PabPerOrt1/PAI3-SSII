import ssl,sys
from socket import *

with open("Config.config") as configfile:
        puerto_elegido = configfile.readlines()[1]
Puerto = puerto_elegido.replace("Puerto_elegido=","")

def get_conection():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('Keys/new.pem', 'Keys/private.key')

    soc = socket()
    soc.bind(("", int(Puerto)))
    print(f"El servidor está corriendo en el puerto '{int(Puerto)}'")
    print("Escuchando conexiones...")
    soc.listen(5)
    
    ssock = context.wrap_socket(soc, server_side=True)
    conn, addr = ssock.accept()
    print("Conectando con un cliente", addr)
    mensajeRecibido = conn.recv(4096).decode()
    print(mensajeRecibido)
    #AQUI IRIA LA COMPROBACION
    ##
    conn.send("Se ha recibido el mensaje")
    ##COMPROBACION COMPROBACION
    ##
    print("Desconectado el cliente", addr)
    #cerramos conexion
    conn.close()
    sys.exit()
if __name__ == "__main__":
    get_conection()