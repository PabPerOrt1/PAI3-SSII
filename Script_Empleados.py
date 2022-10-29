import os, secrets, random, requests

from random import randint

url = 'https://svnweb.freebsd.org/csrg/share/dict/propernames?view=co'
datos = requests.get(url)
texto = datos.text
palabras = texto.split("\n")

with open('.\passwords.txt', 'r') as pass_file:
        lista_pass = pass_file.readlines()

def main():
    print(len(palabras))
    for i in range(1,301):
        
        file = open('./BDD.txt', "a")
        file.write(f'{palabras[i]}' + ':' + lista_pass[i-1])
        file.close()
        pass_file.close()

if __name__ == '__main__':
    main()