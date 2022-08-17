#   Ejercicio 1
#Solicitar 2 numeros enteros y realizar una calculadora
#Mostrando linea por linea el resultado con los operadores matematicos

num_uno = int(input('Ingresa el primer numero entero: '))
num_dos = int(input('Ingresa el segundo numero entero: '))

suma = num_uno + num_dos
resta = num_uno - num_dos
division = num_uno / num_dos
division_exacta = num_uno // num_dos
multiplicación = num_uno * num_dos
potencia = num_uno ** num_dos

print(
    f'La suma de {num_uno} y {num_dos} es {num_uno + num_dos} '
    f'La resta de {num_uno} y {num_dos} es {num_uno - num_dos} '
    f'La division_exacta de {num_uno} y {num_dos} es {division_exacta} '
    f'La division de {num_uno} y {num_dos} es {num_uno / num_dos} '
    f'La potencia de {num_uno} y {num_dos} es {potencia} '
)

#   Ejercicio 2
#Solicitar un numero y validar si es un numero par o impar

num_tres = int(input('Ingresa un tercer num para ver si es par o inpar: '))
print(f'El numero {num_tres} es par? {num_tres %2 == 0}')