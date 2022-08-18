#   ESTRUCTURA DE DATOS
##  CONJUNTOS (Sets) -> Tipo de datos inalterables
##  Es una estructura desordenada y no indexada (indice)

estaciones = {"Verano", "Otoño", "Primavera", "Invierno"}
print(estaciones)

#   *Add -> agregar un valor al conjunto
estaciones.add("Eder")
print(f'add -> {estaciones}')

#   *Remove -> eliminar un valor del conjunto
estaciones.remove("Otoño")
print(f'remove -> {estaciones}')

##  funciones para los conjuntos (sets)
##  otra estructura de datos (frozenset)