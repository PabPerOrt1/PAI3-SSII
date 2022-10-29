from multiprocessing import context
import ssl,sys
from socket import *

with open("Config.config") as configfile:
        puerto_elegido = configfile.readlines()[1]
Puerto = puerto_elegido.replace("Puerto_elegido=","")

def get_conection():
    #context = ssl.create_default_context()
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('Keys/new.pem', 'Keys/private.key')

    soc = socket()
<<<<<<< HEAD
    soc.bind(("10.100.225.22", Puerto))
    print(f"El servidor está corriendo en el puerto '{Puerto}'")
=======
    soc.bind(("", int(Puerto)))
    print(f"El servidor está corriendo en el puerto '{int(Puerto)}'")
>>>>>>> 2efd785425e37df18c2aecfbaefb16c7c04d69eb
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