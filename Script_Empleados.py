import os, secrets, random

from random import randint



url = 'https://svnweb.freebsd.org/csrg/share/dict/propernames?view=co'
palabras = url.split()

url_c = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
passwords = url_c.split()

def main():
    i = 1

    for i in range(1,301):
        lista_name = []
        lista_contraseñas = []
        num_aleatorio = randint(1,len(palabras)-1)
        lista_name.append(palabras[num_aleatorio] )
        num_rand_c = randint(1,len(passwords)-1)
        lista_contraseñas.append(passwords[num_rand_c])
        
        file = open('./Empleados/Empleado' + str(i) + '.txt', "w")
        file.write("{}, {}".format(lista_name[0], lista_contraseñas[0]))
        file.close()
        i +=1

if __name__ == '__main__':
    main()