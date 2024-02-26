### Python Package Manager ###

# PIP Python
# https://pypi.org/

# instalar modulos  ("pip install nom_modulo")

import numpy    # pip install numpy

print(numpy.version.version)    # version del numpy

numpy_array = numpy.array([25,12,34,29,25,21,18,23,30,34,26,30])    # array en numpy

print(type(numpy_array))  # <class 'numpy.ndarray'>

print(numpy_array * 2)


import pandas   # pip install pandas

# pip list  --> listado de los modulos instalados
# pip uninstall pandas --> eliminar el modulo "pandas"
# pip show numpy

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
#print(response.json())     # descomentar y veras los 151 primeros pokemon en json

# Arithmetics Package
from mypackage import arithmetics

print(arithmetics.sum_two_values(2, 5))
