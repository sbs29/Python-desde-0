### Conditionals ###


my_conditional = False      # Condicion inicial

if my_conditional:
    print("Se ejecuta la condicion del if")     # No entra

my_conditional = 5+5      # Python es de tipado flexible por eso cambiamos su valor facilmente    True

if my_conditional == 10:
    print("Se ejecuta la condicion del segundo if")     # Entra

if my_conditional >= 10:
    print("Se ejecuta la condicion del tercer if")      # Entra


if my_conditional > 10 and my_conditional < 20:
    print("Es mayor que 10 y menor que 20")             # No entra


elif my_conditional == 1:
    print("Es 1")



else:
    print("Es menor o igual que 10 o mayor o igual que 20")        # No entra




    print("Esto pertenece al else da igual los saltos de linea. Lo que importa es la Tabulacion")

print("La ejecucion continua")              # Entra

my_string = ""  # Esto aunque este vacio tiene un valor

if my_string == "":
    print("mi cadena de texto es vacia comprobando")    # Entra

if not my_string:
    print("mi cadena de texto es vacia negando")    # Entra