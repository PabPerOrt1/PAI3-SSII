from socket import *
import sys

direccionServidor = ""
<<<<<<< HEAD
puertoServidor = 2287
=======
puertoServidor = 443
>>>>>>> 3fb1594692bd73910856b91d1e1e6e2fbe3dc390

#Generamos un nuevo socket
socketServidor = socket(AF_INET, SOCK_STREAM)
#Establecemos la conexión
socketServidor.bind( (direccionServidor,puertoServidor) )
socketServidor.listen()

while True:
    #Establecemos la conexión
    socketConexion, addr = socketServidor.accept()
    print("Conectando con un cliente", addr)
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