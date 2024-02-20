### Tuples ###  *********(NO SON MUTABLES // INMUTABLE)**********

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (28, 1.80, "Sebastian", "Solano","xxxxx")
my_other_tuple = (25,24,15,17,28,26,30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count(28))
print(my_tuple.index("Sebastian"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# se crea una nueva tupla 
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

# formatea el tipo de dato de tuple a list
my_tuple = list(my_tuple)
print(type(my_tuple))

# una vez sea una lista trabajamos con ella
my_tuple[4] = "Sbs"
my_tuple.insert(1, "Rojo")
print(my_tuple)

# formatea el tipo de dato de list a tuple
my_tuple = tuple(my_tuple)
print(type(my_tuple))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)


# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion
# del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined