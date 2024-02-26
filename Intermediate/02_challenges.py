### Challenges ###

'''
#1 EL FAMOSO "FIZZ BUZZ"

Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

def fizzbuzz():
    for i in range(1,100):
        if i % 3 == 0 and i % 5 == 0:
            print(i,"fizzbuzz")
        elif i % 3 == 0:
            print(i,"fizz")
        elif i % 5 == 0:
            print(i,"buzz")
        else:
            print(i)

fizzbuzz()


print("--------------------------------Ejercicio #2--------------------------------")
'''
#2 ¿ES UN ANAGRAMA?

Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
'''

def is_anagram(first_word, second_word):
    if first_word.lower() == second_word.lower():
        return False 
    elif sorted(first_word.lower()) == sorted(second_word.lower()):
        return True
    else:
        return False

print(is_anagram("Amor","Roam"))


print("--------------------------------Ejercicio #3--------------------------------")
'''
#3 LA SUCESIÓN DE FIBONACCI

Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci():
    prev = 0
    next = 1

    for i in range(0, 50):
        print("Vuelta:",i+1,"fibonacci:",prev)

        fib = prev + next
        prev = next
        next = fib

fibonacci()


print("--------------------------------Ejercicio #4--------------------------------")
'''
#4 ¿ES UN NUMERO PRIMO?

Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''

def is_prime():
    
    for number in range(1,101):

        if number >= 2:

            is_divisible = False

            for i in range(2,number):

                if number % i == 0:

                    is_divisible = True

                    break

            if not is_divisible:

                print(number)    

is_prime()


print("--------------------------------Ejercicio #5--------------------------------")
'''
#5 INVERTIR CADENAS

Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
''' 

# version personal sin ayuda
def reverse_fv(text):
    reverseText = ""
    auxiliar = ""
    for element in range(0,len(text)):
        auxiliar += text[element]
        reverseText = auxiliar + reverseText
        auxiliar = ""
    print(reverseText)

reverse_fv("Hola mundo")

# version del profesor
def reverse_sv(text):
    reverseText = ""
    text_len = len(text)
    for i in range(0, text_len ):
        reverseText += text[text_len - i - 1]  
    print(reverseText)

reverse_sv("Hola mundo")

print("--------------------------------Ejercicio #6--------------------------------")
'''
#6 ÁREA DE UN POLÍGONO

Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
 - La función recibirá por parámetro sólo UN polígono a la vez.
 - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 - Imprime el cálculo del área de un polígono de cada tipo.
''' 

def calculate_area(poligono):
    if poligono["poligono"] == "triangulo":
        area = (poligono["base"]*poligono["altura"])/2 
        return print("triangulo:",area)
    elif poligono["poligono"] == "cuadrado":
        area = poligono["lado"]*poligono["lado"]
        return print("cuadrado:",area)
    elif poligono["poligono"] == "rectangulo":
        area = poligono["base"]*poligono["altura"]
        return print("rectangulo:",area)
    else:
        return print("poligono invalido")

triangulo = {"poligono":"triangulo","base":5,"altura":3}
calculate_area(triangulo)

cuadrado = {"poligono":"cuadrado","lado":5}
calculate_area(cuadrado)

rectangulo = {"poligono":"rectangulo","base":5,"altura":3}
calculate_area(rectangulo)

poligono_invalido = {"poligono":"none","base":5,"altura":3}
calculate_area(poligono_invalido)


print("--------------------------------Ejercicio #7--------------------------------")
'''
#7 CONTANDO PALABRAS

Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que
  lo resuelvan automáticamente.
''' 