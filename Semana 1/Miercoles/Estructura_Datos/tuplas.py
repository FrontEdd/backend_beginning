#   ESTRUCTURA DE DATOS
##  TUPLAS -> Colección de datos cuyo orden es inalterable, o sea, son elementos ordenados en una secuencia específica y que posee importancia.

#Inmutable
personas = ("Alan", "Andres", "Cesar", "David")

#   *Index -> retorna el indice del valor mencionado
indice_cesar = personas.index("Cesar")
print(f'index Cesar -> {indice_cesar}')

#   *Count -> retorna las veces que existe un elemento
david_contador = personas.count("David")
print(f'David count -> {david_contador}')

#################################################

#   ?List -> convertir o crear una lista
personas_lista = list(personas)
personas_lista.append("Eder")
print(type(personas_lista))
print(f'append -> {personas_lista}')

#   ?Tuple -> convertir o crear una tupla
personas = tuple(personas_lista)
print(type(personas))
print(f'nueva tupla -> {personas}')