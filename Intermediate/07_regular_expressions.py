### Regular Expressions ###

# Entender las expresiones regulares (Herctor de Leon)

import re

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

# match 
# comprobar si existe una coincidencia del string que le pasamos con el string a comparar
match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

# Formas de controlar si no existe un span
match = re.match("Esta es la lección", my_other_string)
#if not(match == None):     Otra forma de comprobar el None
#if match != None:          Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])

'''
# Nos dice si existe una coincidencia en my_string desde el principio
print(re.match("Esta es la lección", my_string))             # True
print(re.match("Esta es la lección", my_other_string))       # False 
print(re.match("Expresiones Regulares", my_string))          # False 

print(re.match("Esta es la lección", my_string, re.I))       # True    
'''

# search
# Nos dice si existe una coincidencia en my_string general      (primera coincidencia)
search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])


# findall
# Nos dice si existe una coincidencia en my_string general      (todas las coincidencias)
findall = re.findall("lección", my_string, re.I)
print(findall)


# split
# dividir por un caracter especifico
print(re.split(":", my_string)) 


# sub
# nos permite sustituir cadenas de texto
print(re.sub("Expresiones Regulares", "RegEx", my_string, re.I))
#print(re.sub("lección|Lección", "LECCION", my_string, re.I))   Es lo mismo que la siguiente linea
print(re.sub("[l|L]ección", "LECCION", my_string, re.I))



# Patterns
# https://regex101.com/

# Busca lección y Lección
pattern = r'[l|L]ección'
print(re.findall(pattern, my_string))

# Busca lección, Lección y Expresiones
pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern, my_string))

# Busca los numeros de 0 a 9
pattern = r'[0-9]'
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

# Busca solo los caracteres numericos
pattern = r'\d'
print(re.findall(pattern, my_string))

# Busca solo los caracteres alfabeticos
pattern = r'\D'
print(re.findall(pattern, my_string))

# me dice todo despues de la primera l
pattern = r'[l].*'
print(re.findall(pattern, my_string))

email = "sebas@sebas.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"   # RegEx para buscar comprobar si existe un email (bastante mejarable)
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))
