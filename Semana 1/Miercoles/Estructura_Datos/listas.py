#   ESTRUCTURA DE DATOS
##  LISTAS -> Estructura de datos 'mutable', nos ayuda a almacear mas de un valor

# La forma tradicional y no intuitiva
#persona_uno = "Carlos"
#persona_dos = "Luis"
#persona_tres = "Cesar"

# La forma intuitiva
## Valores:
personas = ["Carlos", "Luis", "Cesar"]
# n - 1

print(personas)
print(personas[2])

##Funciones:
#   *Append -> agregar un valor al final de una lista
personas.append("Edgar")
print(f'append -> {personas}')

#  *Insert -> agrega un valor en una lista segun la posición o índice mencionado
personas.insert(0, "David")
print(f'insert -> {personas}')

#   *Index -> retorna el índice del valor mencionado o a buscar
indice_luis = personas.index("Luis") #-> Busca el index (ubicacion) de Luis en la lista (array)
print(f'index Luis -> {indice_luis}')

#   *Extend -> unir dos listas
personas_nuevas = ["Andres", "Daniel", "Arturo"]
personas.extend(personas_nuevas)
print(f'extend -> {personas}')

#   *Remove -> elimina un valor de una lista
personas.remove("Edgar") 
print(f'remove -> {personas}')

#   *Pop -> eliminar un valor segun la posición o índice
personas.pop(3) #Ultimo valor puede tomar sin argumento 'pop()' o indicar 'pop(-1)' 
print(f'pop -> {personas}')

#   *Sort -> ordena los valores de una lista, menor a mayor
#Argumento 'reverse=False' -> menor a mayor  (default)
#Argumento 'reverse=True' -> mayor a menor
personas.sort() 
print(f'sort -> {personas}')

#   *Count -> retorna las veces que existe un elemento
personas.append("Daniel")
daniel_contador = personas.count("Daniel")
print(f'count -> {daniel_contador}')

#   *Len -> cuenta los elementos de una estructura de datos | length
print(f'Total de personas: {len(personas)}')