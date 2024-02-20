# Variables en Python (en minusculas y con snikestyle)

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Print para mostrar el valor de cada una pero tambien concatena con el uso de ,

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Mirar mas a fondo las built in funtions que se cargan en el sistema Ej: len() type() etc.

# Declaracion de variables multiples en una sola linea

first_name, last_name, country, age, is_married = 'Sebastian', 'Solano', 'Colombia', 28, False

print("Mi nombre es", first_name, last_name, ",  tengo ", age, " años y soy de ", country)

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# Inputs y su uso
"""
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')

print(name)
print(age)
"""

# Tambien puedes cambiar su tipo
name = 123
age = "sebas"

print(name)
print(age)

# ¿Forzamos el tipo? No
address: str = "Mi direccion"
address = 32
address = False
address = 1.2
print(type(address))