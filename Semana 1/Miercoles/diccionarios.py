#   ESTRUCTURA DE DATOS
##  DICCIONARIO -> 
##  Conformado por -> { key: valor }

persona = {
    "nombres": "José",
    "apellido": "Velarde",
    "especialidades": [
        {
            "nombre": "Frontend",
        },
        {
            "nombre": "Backend",
        }
    ]
}

#print(f'Obtener el nombre -> {persona["nombres"]}')
#print(f'Obtener la 2da especialdad -> {persona["especialidades"][1]["nombre"]}')

#   *Items -> retorna una lista de tuplas (clave, valor)
print(f'items -> {persona.items()}')

#   *Keys -> retorna una lista con todas las clases
print(f'keys -> {persona.keys()}')

#   *Values -> retorna una lista con todos los valores
print(f'values -> {persona.values()}')

#   *Get -> busca la clave en mención, si no la encuentra retorna 'None'
print(f'get -> {persona.get("edad")}')
print(f'get -> {persona.get("apellido")}')

#   *Agregar una clave - valor
persona['edad'] = 28
print(f'get -> {persona.get("edad")}')

#   *Pop -> eliminar una clave con su valor
persona.pop('especialidades')
print(f'pop -> {persona}')