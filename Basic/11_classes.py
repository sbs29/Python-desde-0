### Classes ###

class MyEmptyPerson:   # La buena practica nos dice que el nombre debe ser CamelCase
    pass        # Intruccion del sistema para ejecutar una clase "vacia"

print(MyEmptyPerson)
print(MyEmptyPerson()) # Sí se necesitara pasar parametros

print("------Clase con contructor con parametros externos------")
class Person:
    def __init__(self,name,surname):    # Habilita la capacidad para que Person reciba un parametro  //  self es requerido   //  Constructor
        self.name = name
        self.surname = surname

my_person = Person("Sebas","Solano")
print(f"{my_person.name} {my_person.surname}\n")

print("------Clase con contructor con parametros internos------")
class Person:
    def __init__(self):                 # Habilita la capacidad para que Person reciba un parametro  //  self es requerido   //  Constructor
        self.name = "Sebastian"
        self.surname = "Solano"

my_person = Person()
print(f"{my_person.name} {my_person.surname}\n")

print("------Clase con contructor con parametros externos y modificados------")
class Person:
    def __init__(self,name,surname):     # Habilita la capacidad para que Person reciba un parametro  //  self es requerido   //  Constructor
        self.fullname = f"{name} {surname}"

my_person = Person("Sebas","Solano")
print(my_person.fullname+"\n")

print("------Clase con contructor con parametros externos y funciones------")
class Person:
    def __init__(self,name,surname,alias = "sin alias"):     # Habilita la capacidad para que Person reciba un parametro  //  self es requerido   //  Constructor
        self.fullname = f"{name} {surname} ({alias})"       # Propiedad publica 
        self.__name = name
        self.__surname = surname            # __xxxxx defines la propiedad como privada por tanto no puedes modificarla

    def get_name (self):
        return self.__name

    def walk(self):                     # funcion declara en la clase y usando info del constructor con self
        print(f"{self.fullname} Está caminando\n")

my_person = Person("Sebas","Solano")
my_person.walk()

my_other_person = Person("Raul","Alvarez","Auronplay")
print(my_other_person.fullname)
my_other_person.walk()
my_other_person.fullname = "Auronplay el viejo sabroso... ABDUZCAN!!!!"
print(my_other_person.fullname)


# print(my_person.__name)     # AttributeError: 'Person' object has no attribute '__name'
print(my_person.get_name())     # Asi puedes obtener el nombre