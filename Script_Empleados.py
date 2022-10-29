import os, secrets, random, requests

from random import randint

url = 'https://svnweb.freebsd.org/csrg/share/dict/propernames?view=co'
datos = requests.get(url)
texto = datos.text
palabras = texto.split("\n")

with open('.\passwords.txt', 'r') as pass_file:
        lista_pass = pass_file.readlines()

def main():
    for i in range(1,301):
        file = open('./Ficheros_de_Prueba/Prueba' + str(i) + '.txt', "w")
        file.write(palabras[i] + "\n")
        file.write(lista_pass[i-1])
        file.write("Hola soy " + palabras[i] + " y me encanta este servidor!")
        file.close()
        pass_file.close()

if __name__ == '__main__':
    main()