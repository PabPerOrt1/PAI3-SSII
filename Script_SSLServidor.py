from multiprocessing import context
import ssl,sys
from socket import *

with open("Config.config") as configfile:
        puerto_elegido = configfile.readlines()[1]
Puerto = puerto_elegido.replace("Puerto_elegido=","")


def comprobarCredenciales(mensajeRecibido):
    string_separado = mensajeRecibido.split()
    usuario = string_separado[0]
    password = string_separado[1]
    mensaje = string_separado[2]
    SSLversion = string_separado[3]
    with open('BDD.txt','r') as usuariosFiles:
        lineas = usuariosFiles.readlines()
        for i in range(len(lineas)):
            spliteao = lineas[i].split(':')
            limpiar_password=spliteao[1].replace("\n","")
            if usuario == spliteao[0] and password == limpiar_password :
                with open('Mensajes_Almacenados.txt','a') as afile:
                    afile.write(f"El usuario '{usuario}' escribió el mensaje: " + mensaje + f" con protocolo '{SSLversion}'")
                    return "Comprobación exitosa"
            else:
                return "Comprobación errónea"

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
    if comprobarCredenciales(mensajeRecibido)=="Comprobación exitosa":
        conn.send(("La comprobación ha sido exitosa, estamos guardando su mensaje").encode())
    else: 
        conn.send(("La comprobación ha sido errónea. Inténtelo de nuevo").encode())

    print("Desconectado el cliente", addr)
    conn.close()
    sys.exit()
if __name__ == "__main__":
    get_conection()