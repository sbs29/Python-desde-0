### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# los dicts funcionan como un mapa clave:valor (parecido a un JSON)
my_other_dict = {"Nombre":"Sebastian", "Apellido":"Solano", "Edad":28, 1:"Python"}

my_dict = {
    "Nombre":"Sebastian", 
    "Apellido":"Solano", 
    "Edad":28, 
    1:1.80,
    "Lenguage": {"Python","Java","JavaScript"}
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# facilidad para acceder a un elemeto
print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# podemos añador nuevos elementos 
my_dict["Calle"] = "Calle sebas"
print(my_dict)

# Eliminar elementos
my_dict.pop("Calle")
print(my_dict)

# del my_dict["Calle"]
# print(my_dict)

# busqueda por clave
print("Apellido" in my_dict)     # True
print("Solano" in my_dict)     # False

# listado por item
print(my_dict.items())

# listado de las keys
print(my_dict.keys())

# listado de valores
print(my_dict.values())


# crear un copia pero sin valores
my_list = ["Nombre", 1]

my_new_dict = my_dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = my_dict.fromkeys(("Nombre", 1))
print(my_new_dict)

my_new_dict = my_dict.fromkeys((my_dict))
print(my_new_dict)

my_new_dict = my_dict.fromkeys(my_dict,("Sebas","Solano"))
print(my_new_dict)