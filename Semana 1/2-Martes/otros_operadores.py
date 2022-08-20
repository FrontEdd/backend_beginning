n_uno, n_dos = 10, 20


#   Operadores de comparación
##  '===no existe, =='
##  '!=, diferente'
##  '< menor a'
##  '> mayor a'
##  '<= menor o igual a'
##  '>= mayor o igual a'
print(
    f'Los números {n_uno} y {n_dos}, '
    f'son iguales? {n_uno == n_dos}'
)

#   Operadores Lógicos
##  Para validar mas de un resultado si es parecido
##  'and'
##  'or'
##  'not'
print((n_uno > 11) or (n_dos < 21))

#   Operadores de identidad
## 'is' -> igual
## 'is not' -> diferente
fruta_uno = 'Manzana'
fruta_dos = fruta_uno

print(fruta_uno is fruta_dos)