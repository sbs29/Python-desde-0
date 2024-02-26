### Lambdas ###

# Las lambdas pueden almacenarse en una variable

# palabra reservada "lambda" "parametros:" "que_va_hacer"

sum_two_values = lambda first_value, second_value: first_value + second_value

print(sum_two_values(5,3))

multiply_values = lambda first_value, second_value: first_value * second_value - 3

print(multiply_values(5,3))

# Podemos ejecutar una lambda dentro de una funcion siempre que este en el return
def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2,4)) # Asi le pasariamos los parametros a la funcion y a la lambda