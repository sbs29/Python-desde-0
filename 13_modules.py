### Modules ###

# No podemos importar un fichero que empiece por numero
# Usamos los imports para reutilizar funciones de otro archivo

import module

module.sum_three_values(5,6,4)

# Tambien podemos importar una funcion especifica
from module import sum_three_values

sum_three_values(2,5,9)

# Python trae muchos modulos propios cuando lo instalamos
import math

print("Numero PI",math.pi)
print("Raiz Cuadrada",math.sqrt(25))
print("Exponente",math.pow(5,2))
print("Logaritmo",math.log(25,5))