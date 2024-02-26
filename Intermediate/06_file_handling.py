### File Handling ###

import os

# .txt file

txt_file = open("Intermediate/my_file.txt","r+")    # funcion para abrir ficheros ("ruta desde la carpeta", "modo del fichero w+ Leer, escribir y sobreescribe si ya existe")
#txt_file.write("Mi nombre es Sebastian\ny mi apellido es Solano,\nmi edad es de 28 Anos\ny mi lenguaje favorito es Python")

#print(txt_file.read())      #Leé todo el archivo
#print(txt_file.read(10))   # Leer un numero determinado de caracteres
#print(txt_file.readline())  # Leer linea a linea 
#print(txt_file.readline())  # Leé la siguiente linea  

for line in txt_file.readlines():   # Leé todo el archivo y crea un listado con las lineas que encuentra
    print(line)

txt_file.write("\nmi apodo es sbs")   # Escribe una linea nueva despues del ultimo caracter
print(txt_file.readline())

txt_file.close()

with open("Intermediate/my_file.txt","a") as my_other_file: # Añadimos una linea con alias
    my_other_file.write("\npero siempre pongo sbs29")

# para eliminar necesitamos import os
#os.remove("Intermediate/my_file.txt")
    

# .json file

import json

json_file = open("Intermediate/my_file.json","w+")      # Abrir fichero

json_test = {               # Estructura fichero    de dict a json
    "name":"Sebastian", 
    "surname":"Solano", 
    "age":28, 
    "language": ["Python","Java","JavaScript"],
    "website":"https://google.es"
    }

json.dump(json_test, json_file, indent=4)     # Crear el json manualmente (contenido, ruta, indentado y espacios,  )

json_file.close()

with open("Intermediate/my_file.json") as my_other_file: # Leemos el fichero despues de cerrarlo
    for line in my_other_file.readlines():   
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))    # pasamos de json a dict

print(type(json_dict))  # ahora que es un dict podemos usar todas sus funciones

print(json_dict["name"])


# .csv file

import csv

csv_file = open("Intermediate/my_file.csv","w+")

csv_writer = csv.writer(csv_file)

csv_writer.writerow(["name","surname","age","language","website"])
csv_writer.writerow(["Sebastian","Solano", 28, "Python","https://google.es"])
csv_writer.writerow(["Yolanda","Garcia", 24, "Css",""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file: # Leemos el fichero despues de cerrarlo
    for line in my_other_file.readlines():   
        print(line)

# .xlsx file

#import xlrd # debe instalarse este modulo

# .xml file

import xml

