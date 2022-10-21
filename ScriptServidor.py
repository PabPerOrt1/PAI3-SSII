import os,sys
from socket import *

#Generamos un nuevo socket
IPServidor = "localhost"
puertoServidor = 9899

socketServidor = socket(AF_INET, SOCK_STREAM)
#Establecemos la conexión
socketServidor.bind((IPServidor,puertoServidor))
print("empezando a levantar el puerto")
socketServidor.listen()
prueba="Mensaje recibido"
while True:
    print >>sys.stderr, 'Esperando para realizar conexión'
    socketConexion, addr = socketServidor.accept()
    mensajeRecibido = socketConexion.recv(4096).decode()
    print(mensajeRecibido)
    socketConexion.send(prueba.encode())
#cerramos conexion
print("Desconectado el cliente", addr)
socketConexion.close()