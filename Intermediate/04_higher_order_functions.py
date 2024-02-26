### Higher Order Functions ###

from functools import reduce


def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_one(first_value, second_value,f_sum):
    return f_sum(first_value+second_value)

print(sum_two_values_and_add_one(5, 4, sum_one))
print(sum_two_values_and_add_one(5, 4, sum_five))

### Closures ###

# Funcion que define una funcion que retorna una funcion
def sum_ten(original_value):
    def add(value):
        return value + 10 +original_value
    return add

add_closure = sum_ten(2)
print(add_closure(5))

print(sum_ten(5)(1))        # Esto funcionaria como una lambda en su llamada

### Built-in Higher Order Functions ###

numbers = [2, 15, 10 , 21, 35, 24, 18, 4]
# Map 
# Con un listado iterable genera otro listado iterable en funcion a la funcion que le pasamos
# Recorre cada uno de los valores y ejecutaba una funcion 

def mutiply_two(number):
    return number * 2

print(list(map(mutiply_two, numbers)))                  # Con una funcion

print(list(map(lambda number: number * 2, numbers)))    # Con una lambda

# Filter
# Le pasamos una funcion y un iterable para filtrar los valores segun la misma funcion
# Recorre cada uno de los valores y filtraba valores

def filter_greater_than_ten(number):
    if number > 10:
        return True
    else:
        return False

print(list(filter(filter_greater_than_ten, numbers)))   # Con una funcion

print(list(filter(lambda number: number> 10, numbers))) # Con una lambda

# Reduce
# Opera entre los valores que va recorriendo y va operando con los mismos valores que va recorriendo este iterable

def sum_two_values(first_value, second_value):
    print("First Value:",first_value,"Second Value",second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))

# numbers = [2, 15, 10 , 21, 35, 24, 18, 4]