import socket
import threading
from multiprocessing import context
import ssl,sys,time
from socket import *

with open("Config.config") as configfile:
        puerto_elegido = configfile.readlines()[1]
Puerto = puerto_elegido.replace("Puerto_elegido=","")

userPass = dict()

def comprobarCredenciales(mensajeRecibido):
    string_separado = mensajeRecibido.split(",")
    username = string_separado[0]
    passw = string_separado[1]
    mensaje = string_separado[2]
    SSLversion = string_separado[3]
    with open('BDD.txt','r') as usuariosFiles:
        lineas = usuariosFiles.readlines()
        for i in range(len(lineas)):
            spliteao = lineas[i].split(':')
            password_documento=spliteao[1].replace("\n","")
            userPass[spliteao[0]] = password_documento

    if username in userPass and userPass[username] == passw:
        with open('Mensajes_Almacenados.txt','a+') as afile:
            afile.write(f"El usuario '{username}' escribio el mensaje: " + mensaje + f". Con protocolo '{SSLversion}'"+ "\n" )
        return "Comprobación exitosa"
    else:
        return "Comprobación errónea"


context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('Keys/new.pem', 'Keys/private.key')
soc = socket()
soc.bind(("", int(Puerto)))
print(f"El servidor está corriendo en el puerto '{int(Puerto)}'")
print("Escuchando conexiones...")
soc.listen(1)
ssock = context.wrap_socket(soc, server_side=True)

#Para inputs mediante CMD o Prueba 300 para mensajes almacenados
def worker(*args):
    conn = args[0]
    addr = args[1]
    print("Conectando con un cliente", addr)
    mensajeRecibido = conn.recv(4096).decode()
    print(mensajeRecibido)
    if comprobarCredenciales(mensajeRecibido)=="Comprobación exitosa":
        conn.send(("La comprobación ha sido exitosa, estamos guardando su mensaje").encode())
    else: 
        conn.send(("La comprobación ha sido errónea. Inténtelo de nuevo").encode())

    print("Desconectado el cliente", addr)
    conn.close()

#Para prueba de 300 empleados a la vez
def worker_Test(*args):
    conn = args[0]
    addr = args[1]
    print("Conectando con un cliente", addr)

acc=1
while 1:
    conn, addr = ssock.accept()
    #Cambiar worker o worker_Test depende lo que se quiera hacer
    threading.Thread(target=worker, args=(conn, addr)).start()
    #print ("Hay " + str(acc) + " clientes conectados")
    acc+=1
        
