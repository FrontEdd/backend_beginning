## Las Variables solo pueden ser nombrados con letras, no alfanumericos ni numericos
### Formato: Snakecase $$$$_$$$$_$$$$
    #nombre_de_variable
    #No utilizar nombres de variables reservadas, para el uso general


#   Variables de texto (string)
nombre = 'Edgar'
apellido = 'Razuri'
texto = """
Buenos días:
    La carta redactada...
    .......
"""
texto_en_linea = (
    "Hola, como estas?"
    "es tarde por alla?"
    "buenas noches"
)

##  Operadores de salida -> 'print'
#print(nombre)
#print(texto)
#print(texto_en_linea)


#   Variables numericos
numero_entero = 10
numero_decimal = 10.50

##  Concatenación
#print(nombre + apellido)
#print(nombre, apellido)
#print(f"{nombre} {apellido}") #f-string

##  Tipos -> 'type' nos va a retornar el tipo de variable
#print(type(nombre))
#print(type(numero_entero))
#print(type(numero_decimal))

nombre = 1500
#print(type(nombre))

#   función nombre() -> salida
##  funcion nombre_completo(nombre, apellido) -> str { return `${nombre} ${apellido}` }


#   Variables booleanas
##  true y false -> 1 y 0
verdadero = True
falso = False

#   Variables definidas con valor nulo 'null'
variable_nulo = None

#   Asignación multiple
#persona = 'Juan'
#nacionalidad = 'peruano'

nombre, apellido = 'Edgar', 'peruano'
print(nombre, apellido)