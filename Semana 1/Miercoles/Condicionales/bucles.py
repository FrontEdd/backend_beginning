##  BUCLES 
##  foreach - for

meses = ["Enero", "Febrero", "Marzo"]

#for mes in meses:
#    print(mes)

#print(mes) #Muestra el ultimo valor de la lista

#   *Obtener el indice y el valor
#for index, value in enumerate(meses):
#    print(index, value)

#  *Comparación de listas
lista_uno = [1, 2, 3]
lista_dos = [5, 3, 1]

#for uno in lista_uno:
#    for dos in lista_dos:
#        if uno == dos:
#            print(uno)
#            break

#   *Range -> recibe 3 argumentos
##  1- donde empieza
##  2- hasta donde finaliza (n-1)
##  3- de cuanto en cuanto incrementa
#for numero in range(1, 10, 2):
#    print(numero)


persona = {
    "nombre": "Luis",
    "apellidos": "Mora",
    "cursos": ["aritmetica", "geometria"],
}

#for key, value in persona.items():
#    print(key, value)

#   *While -> condicion

edad = 34
#while edad > 18:
#    print(f'actual -> {edad}')
#    edad -= 1
#    
#    if edad == 21:
#        break

## Ejercicio Palidromo:
#word = input('Ingresa una palabra: ')
#if str(word) == str(word)[::-1] :
#    print("Si es palindromo")
#else:
#    print("No es palindromo")

## Ejercicio solictar año en que nacimos para mostrar año | edad

#año_nac = int(input('Ingresa tu año de nacimiento: '))
#año_act = 2023
#
#for año in range(año_nac, año_act):
#    print(f'En el año {año} tenias {año-año_nac} año(s)')


year = int(input('Ingresa tu año de nacimiento: '))
age = 0
while year <=2022:
    print(f'En el año {year} tenia {age}')
    year +=1
    age +=1
