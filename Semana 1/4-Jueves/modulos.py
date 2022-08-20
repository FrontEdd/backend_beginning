from camelcase import CamelCase as ClaseCamel

instancia = ClaseCamel()
texto = "hola gente"
print(instancia.hump(texto))