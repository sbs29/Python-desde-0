### String ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string, my_other_string)
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_space_string = "\tEste es un String \n escapado"
print(my_space_string)

# \\ para evitar que se utilice su funcion (\\t, \\n ...)

# Formateo

name, surname, age = "Sebastian", "Solano", 28

# Con format {}
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))

# Con %
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))

# Evitar los (+)           (NO NO NO NO NO NO)
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))

# Usando f para inferir en la interpolacion de los datos   (MEJOR OPCION)
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a, b, c, d, e, f)

# División

language_slice = language[0:4]
print(language_slice)

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

# forma para invertir los caracteres
reversed_language = language[::-1]
print(reversed_language)

# Funciones

# Convierte la primera letra en mayuscula
print(language.capitalize())

# Convierte la cadena a mayusculas
print(language.upper())

# Convierte la cadena a minusculas
print(language.lower())

# Cuenta el caracter que le pongas entre comillas
print(language.count("t"))

# Funciones booleanas (isxxxxxxx)
# Nos dice si es un numero
print(language.isnumeric()) # False
print("1".isnumeric())      # True

# Comprueba si la cadena esta en mayusculas
print(language.upper().isupper())   # True

# Comprueba si la cadena empieza por lo que le pasamos
print(language.startswith("py"))   # True (Diferencia las mayusculas)