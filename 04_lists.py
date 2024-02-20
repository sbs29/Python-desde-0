### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [25,30,22,24,28,25,18,30,29]

print(my_list)
print(len(my_list))

my_other_list = [28, 1.80, "Sebastian", "Solano"]

print(type(my_list))        # result: <class 'list'>
print(type(my_other_list))  # result: <class 'list'>

print(len(my_other_list))   # result: 4 (0,1,2,3)

print(my_other_list[0])     # primer elemento
print(my_other_list[-1])    # ultimo elemento
print(my_other_list[1])     # segundo elemento
print(my_other_list[-3])    # segundo elemento

print(my_list.count(30))    # cuenta las veces que aparece en la lista

print(my_other_list.index("Sebastian"))     # Nos dice el indice de lo que le pasemos(Tiene que estar en la lista)

#print(my_other_list[-4])   # IndexError

# necesita el mismo numero de variables que elementos en la lista      !!!!! EVITAR SU USO ¡¡¡¡¡       posibles ERRORES
age, height, name, surname = my_other_list
print(name)

print(my_list, my_other_list)   # Muestra las 2 listas
print(my_list + my_other_list)  # Muestra 1 lista pero con las concatenacion de las 2

# añade un nuevo dato al final de la lista 
my_other_list.append("Sbs")
print(my_other_list)

# añade un nuevo dato en un indice especifico en la lista
my_other_list.insert(1,"Negro")
print(my_other_list)

# elimina un dato de la lista
my_other_list.remove("Negro")
print(my_other_list)
# solo elimina la primera coincidencia que encuentre
my_list.remove(30)
print(my_list)

# elimina el ultimo elemento
my_list.pop()
print(my_list)

# elimina el elemento que tenga ese indice y lo puedes !!!GUARDAR¡¡¡ en una variable
my_pop_variable = my_list.pop(2)
print(my_pop_variable)
print(my_list)

# elminar por indice
del my_list[2]
print(my_list)

# copiar lista
my_new_list = my_list.copy()

# vaciar la lista por completo
my_list.clear()
print(my_list)

# lista nueva con la copia de la otra
print(my_new_list)

# iniverte el orden de la lista
my_new_list.reverse()
print(my_new_list)

# ordena de menor a mayor la lista
my_new_list.sort()
print(my_new_list)

# hacer sublistas de una lista (no cuenta el indice limite)
my_mini_list = my_new_list[1:3]
print(my_mini_list)

# Ejemplo de que python es de tipado dinamico           !!!!CUIDADO¡¡¡¡¡¡
my_list = "Hola Python"
print(my_list)
print(type(my_list))