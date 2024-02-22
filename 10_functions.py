### Functions ###

def my_function():
    print("Esto es una funcion")

my_function()

def sum_tow_values(first_number,second_number):
    return first_number+second_number

print("El resultado es:",sum_tow_values(5,10))


def print_name(name,surname):
    print(f"{name} {surname}")

print_name(surname="Solano",name="Sebastian")   # Puedo poner un orden manual si fuera necesario (misma cantidad de parametros)

def print_name_with_default(name, surname, alias = "sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Sebastian","Solano")           # Sin pasarle el tercer parametro
print_name_with_default("Sebastian","Solano","Sbs")     # Pasandole el tercer parametro

def print_texts(*texts):     # Si pones un * antes del nombre del parametro puedes pasarle multiples parametros en su llamada
    for text in texts:
        print(text)

print_texts("Hola","como","esta","?")   # Ejemplo