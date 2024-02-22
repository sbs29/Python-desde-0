### Sets ###

my_set = set()
my_other_set = {}   # Se utiliza para set y diccionario

print(type(my_set))
print(type(my_other_set))   # Inicialmente es un diccionario

my_other_set = {"Sebastian", "Solano", 28}
print(type(my_other_set))   # Pasa a tratarse como set

print(len(my_other_set))

# print(my_other_set[0]) TypeError: 'set' object is not subscriptable

my_other_set.add("Sbs") # Un set no es una estructura ordenada
print(my_other_set)

my_other_set.add("Sbs") # Un set no admite duplicados
print(my_other_set)

# podemos hacer busquedas
print("Solano" in my_other_set)     # True
print("Solani" in my_other_set)     # False

# eliminacion con valor concreto
my_other_set.remove("Solano")
print(my_other_set)

#vacia el set pero no elimina el set
my_other_set.clear()
print(len(my_other_set))

# elimina del todo el set
del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Esto se puede hacer pero NO es aconsejable porque no garantiza el orden
my_set = {"Sebastian", "Solano", 28}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Java","Javascript","Python"}

# crea un nuevo set con los 2 set pero no admite duplicados
my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"kotlin","C#"}))

# busca todo lo diferente a lo que le pases
print(my_new_set.difference(my_set))