### Operadores Aritmeticos ###

print(2 + 3)   # addition(+)                    result: 5
print(3 - 1)   # subtraction(-)                 result: 2
print(2 * 3)   # multiplication(*)              result: 6
print(3 / 2)   # division(/)                    result: 1.5
print(3 ** 2)  # exponential(**)                result: 9
print(3 % 2)   # modulus(%)                     result: 1
print(3 // 2)  # Floor division operator(//)    result: 1

# El + funciona con str para concatena str con str. No funciona con diferente tipo de dato
print("Hola " + "Python") # result: Hola Python
# print("Hola" + 5) # result: error
print("Hola " + str(5)) # result: Hola 5
print("Hola " * 5) # result: Hola Hola Hola Hola Hola (SOLO FUNCIONA CON ENTEROS)

### Operadores Comparativos ###

print(2 > 5)    # Mayor que(>)
print(2 < 5)    # Menor que(<)
print(2 >= 5)   # Mayor o igual(>=)
print(5 <= 5)   # Menor o igual(<=)
print(2 == 5)   # Igual(==)
print(2 != 5)   # Distinto(!=)

print("--------------------------------------------")
# Si usamos los operadores comparativos con str lo que compara es la Ordenación alfabética(Teniendo en cuenta las mayusculas por ASCII) 

print("Hola" > "Python")    # Mayor que(>)
print("Hola" < "Python")    # Menor que(<)
print("Hola" >= "Python")   # Mayor o igual(>=)
print("Hola" <= "Python")   # Menor o igual(<=)
print("Hola" == "Python")   # Igual(==)
print("Hola" != "Python")   # Distinto(!=)

print("--------------------------------------------")
### Operadores Lógicos (AND , OR , NOT) ###

print(3 > 4 and "Hola" > "Python")  # result: False
print(3 > 4 or "Hola" > "Python")   # result: False

print(3 < 4 and "Hola" < "Python")  # result: True
print(3 < 4 or "Hola" < "Python")   # result: True

print(3 < 4 or "Hola" > "Python" and 4 == 4)   # result: True

print(3 > 4)        # result: False
print(not(3 > 4))   # result: True

