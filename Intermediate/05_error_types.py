### Error Types ###  (Capturados por defecto por Python)

# SyntaxError
#print "!Hola python¡"   # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("!Hola python¡")


# NameError
# Comentar la linea de abajo para provocar el error
name = "Sebas"  # NameError: name 'name' is not defined
print(name)


# ModuleNotFoundError
#import maths   # Descomentar para Error
import math


# AttributeError
#print(math.PI)  # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)


# IndexError
my_list = ["Python","Swift","Kotlin","Java","JavaScript"]
print(my_list[4])
#print(my_list[15])   # IndexError: list index out of range


# TypeError
#print(my_list["Nombre"])   # TypeError: list indices must be integers or slices, not str
print(my_list[0])


# KeyError
my_dict = {"Nombre":"Sebastian", "Apellido":"Solano", "Edad":28, 1:"Python"}
print(my_dict["Nombre"])
#print(my_dict["Apelido"])   # KeyError: 'Apelido'


# ImportError
#from math import PI # ImportError: cannot import name 'PI' from 'math' (unknown location). Did you mean: 'pi'?
from math import pi
print(pi)


# ValueError
#my_int = int("10 Años") # ValueError: invalid literal for int() with base 10: '10 Años'
my_int = int("10") 
print(type(my_int))

# ZeroDivisionError
#print(5/0)  # ZeroDivisionError: division by zero
print(5/1)

# FileNotFoundError: [Errno 2] No such file or directory: 'my_file.txt'
#open("my_file.txt")    # funcion para abrir ficheros
open("Intermedio/my_file.txt")