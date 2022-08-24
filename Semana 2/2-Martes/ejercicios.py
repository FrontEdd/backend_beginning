##  1° Crear una función que permita ingresar la altura y el ancho de un rectangulo
##  y que este mismo lo dibuje con el signo *

#anc = int(input("Anchura del rectángulo: "))
#alt = int(input("Altura del rectángulo: "))
#def rectangulo(alt, anc):
#    for _ in range(alt):
#        print('*' * anc)
#    return
#
#rectangulo(anc,alt)

##  2° Crear una funcion que reciba la altura del triangulo
##  este mismo va a pintar un triangulo pero invertido 

#anch = int(input("Anchura del triángulo: "))
#
#for i in range(1, anch + 1):
#    for _ in range(i):
#        print("* ", end="")
#    print()
#
#for i in range(1, anch):
#    for _ in range(anch - i):
#        print("* ", end="")
#    print()

##  3° Crear una funación que reciba un numero entero
##  ese mismo número debemos de hacer que llegue hasta 1, con la serie de collats

numero = int(input("Ingresa un numero: "))

while numero != 1:
    print("%d," % (numero), end = "")
    if numero % 2 == 0:
        numero /= 2
    else:
        numero = (numero * 3) + 1

    if numero == 1:
        print("1")