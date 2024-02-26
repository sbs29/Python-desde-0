### List Comprehesion ###

my_original_list = [35, 25, 18, 32, 19, 22, 27, 30, 25, 21]
print(my_original_list)

my_original_list = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_original_list)

my_range = range(10)
print(list(my_range))

# Podemos usar range() para marcar un rango determido para crear elementos

my_list = [i for i in range(10)]        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)

my_list = [i + 1 for i in range(10)]    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)

my_list = [i * 2 for i in range(10)]    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(my_list)

my_list = [i * i for i in range(10)]    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(my_list)

def sun_five(number):
    return (number + 5)*number          # Ej: (1 + 5) * 1 , (2 + 5) * 2, (3 + 5) * 3 ...

my_list = [sun_five(i) for i in range(10)]    # [0, 6, 14, 24, 36, 50, 66, 84, 104, 126]
print(my_list)