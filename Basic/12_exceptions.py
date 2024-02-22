### Exceptions Handling ###

number_one = 5
number_two = 1
number_two = "1"

print("-------Ejemplo 1-------")
# Try - except
try:
    print(number_one + number_two)
    print("No se ha producido ningun error")
except:
    print("Se ha producido un error")               # Se ejecuta cuando ocurre una exception

print("-------Ejemplo 2-------")
# Try - except - else
try:
    print(number_one + number_two)
    print("No se ha producido ningun error")
except:
    print("Se ha producido un error")
else:
    print("La ejecucion contiúa correctamente")     # Se ejecuta cuando no ocurrio ninguna exception entre el try y el except

print("-------Ejemplo 3-------")
# Try - except - else - finally
try:
    print(number_one + number_two)
    print("No se ha producido ningun error")
except:
    print("Se ha producido un error")
else:   # Opcional
    print("La ejecucion contiúa correctamente")
finally:# Opcional
    print("La ejecucion continúa siempre")          # Se ejecutara siempre


# Exceptions por tipo
print("-------Ejemplo 4-------")
try:
    print(number_one + number_two)
    print("No se ha producido ningun error")
except TypeError:
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError") 

# Captura la informacion del Error
print("-------Ejemplo 5-------")
try:
    print(number_one + number_two)
    print("No se ha producido ningun error")
except TypeError as error:
    print("Se ha producido un TypeError") 
    print(error)
except Exception as exception:
    print(exception)