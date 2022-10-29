from multiprocessing import context
import ssl,sys
from socket import *

with open("Config.config") as configfile:
        puerto_elegido = configfile.readlines()[1]
Puerto = puerto_elegido.replace("Puerto_elegido=","")


def comprobarCredenciales(mensajeRecibido):
    string_separado = mensajeRecibido.split()
    #datos_mensaje = string_separado[0]+" "+ string_separado[1]+ " " +string_separado[2]+" " + string_separado[3]
    usuario = string_separado[0]
    password = string_separado[1]
    mensaje = string_separado[2]
    SSLversion = string_separado[3]
    with open('.txt','r') as usuariosFiles:
            lineas_usuario = usuariosFiles.readlines()
    with open('.txt','r') as passwordFiles:
            lineas_password = passwordFiles.readlines()
    if usuario in lineas_usuario and password in lineas_password:
        with open('Mensajes_Almacenados.txt','a') as afile:
            afile.write(f"El usuario '{usuario}' escribió el mensaje:" + mensaje)

def get_conection():
    #context = ssl.create_default_context()
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
    conn.send(("Se ha recibido el mensaje").encode())
    ##COMPROBACION COMPROBACION
    ##
    print("Desconectado el cliente", addr)
    #cerramos conexion
    conn.close()
    sys.exit()
if __name__ == "__main__":
    get_conection()