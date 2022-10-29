import os, secrets, random, requests

from random import randint

url = 'https://svnweb.freebsd.org/csrg/share/dict/propernames?view=co'
datos = requests.get(url)
texto = datos.text
palabras = texto.split("\n")


def main():
    print(len(palabras))
    for i in range(1,301):
        #num_aleatorio = randint(1,300)
        #lista_name.append(palabras[i])
        #num_rand_c = randint(1,300)
        #lista_contraseñas.append(passwords[i])
        
        file = open('./Empleados/Empleado' + str(i) + '.txt', "w")
        file.write(f'{palabras[i]}')
        file.write(f'\n{palabras[i]}1234')
        file.close()

if __name__ == '__main__':
    main()