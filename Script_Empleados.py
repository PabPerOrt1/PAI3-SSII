import os, secrets, random 
import requests

from random import randint

url = requests.get('https://svnweb.freebsd.org/csrg/share/dict/propernames?view=co')
datos = requests.get(url)
texto = datos.text
palabras = texto.split()
num_aleatorio = randint(0,len(palabras))
#print(palabras[num_aleatorio])

url_c = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
datos_c = requests.get(url)
texto_c = datos.text
passwords = texto.split()
num_rand_c = randint(0,len(passwords))
#print(passwords[num_rand_c])

def main():
    i = 1
    while i < 301:
        file = open('./Empleados/Empleado' + str(i) + '.txt', "w")
        file.write((palabras[i]), passwords[i])
        file.close()
        i +=1
if __name__ == '__main__':
    main()