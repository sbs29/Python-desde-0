### Type Hints ###

print("---------------- Ejemplo 1----------------")
my_string_variable = "My String variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

print("---------------- Ejemplo 2----------------")
my_typed_variable: int = "My typed String variable"
print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable: str = 5
print(my_typed_variable)
print(type(my_typed_variable))

print("---------------- Ejemplo 3----------------")
my_typed_variable: int = 5
my_typed_variable.bit_length()
print(my_typed_variable)
print(type(my_typed_variable))