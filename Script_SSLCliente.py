from socket import *
import ssl,sys

cipher = "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384"
with open("Config.config") as configfile:
        ip_elegido =  configfile.readline().rstrip()
        puerto_elegido = configfile.readline().rstrip()
        cipherPack_seleccionado = configfile.readline().rstrip()
IPServidor = ip_elegido.replace("ip_cliente=","")
puertoServidor = puerto_elegido.replace("Puerto_elegido=","")
cipherPack_elegido = cipherPack_seleccionado.replace("cipherPack_A_Eleccion=","")


def client_conect():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations('Keys/new.pem')
    if cipherPack_elegido !='0':
        context.set_ciphers(cipher)
    print("Los CipherSuite elegidos son los siguientes:",context.get_ciphers())

    soc=socket()
    conex_wrap = context.wrap_socket(soc, server_hostname=IPServidor)
    conex_wrap.connect((IPServidor,int(puertoServidor)))
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

if __name__ == "__main__":
    client_conect()