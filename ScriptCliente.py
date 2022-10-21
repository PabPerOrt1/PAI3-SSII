import sys
from socket import *
IPServidor = "localhost"
puertoServidor = 9899

#se decaran e inicializaran los valores del socket del cliente
socketCliente = socket(socket.AF_INET, socket.SOCK_STREAM)
print(sys.stderr("conectando a %s puerto %s" %IPServidor))
socketCliente.connect((IPServidor,puertoServidor))
#escribimos el mensaje
mensaje = "mensaje"
#enviamos mensaje
socketCliente.send(mensaje.encode())
#recibimos el mensaje
respuesta = socketCliente.recv(4096).decode()
print(respuesta)
socketCliente.close()
sys.exit()