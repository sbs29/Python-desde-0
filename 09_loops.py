### Loops ###

# While
print("*********** While *************")
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:   # Es opcional pero contamos con el en python
    print("Mi condicion ya no se cumple")

print(my_condition,"vueltas y salimos")

while my_condition < 20:
    my_condition += 2
    if my_condition == 14:
        print("mi condicion es 14. Adios")
        break   # Rompe la ejecucion del while

    print(my_condition)

# For
print("*********** For *************")

my_list = [23,16,24,35,31,27,18,29]

print("------For con list------")
for element in my_list:
    print(element)

print("------For con tuple------")
my_tuple = (28, 1.80, "Sebastian", "Solano","xxxxx")
for element in my_tuple:
    print(element)

print("------For con set------")
my_set = {"Java","Javascript","Python"}
for element in my_set:
    print(element)

print("------For con dict imprime keys------")
my_dict = {"Nombre":"Sebastian", "Apellido":"Solano", "Edad":28, 1:"Python"}
for element in my_dict:
    print(element)

print("------For con dict imprime values (break)------")
for element in my_dict.values():
    print(element)
    if element == 28:   # Podemos usar el if y el break para romper la ejecucion de un bucle
        break
else:
    print("El bucle for para el diccionario ha finalizado.")

print("La ejecucion continua.")

print("------For con dict imprime values (continue)------")
for element in my_dict.values():
    print(element)
    if element == 28:   # Podemos usar el if y el continue para saltar las lineas siguientes y empezar la siguente vuelta de la ejecucion de un bucle
        continue
    print("Esto no se imprime cuando se cuempla el if")
else:
    print("El bucle for para el diccionario ha finalizado.")

print("La ejecucion continua.")