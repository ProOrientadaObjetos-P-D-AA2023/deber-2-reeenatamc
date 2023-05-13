# Crear dos objetos de la clase Gato

class Gato:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

# objeto 01

# crear

gato_1 = Gato("Whiskers", 2, "Siamés")

# Presentar objeto; usar el método __st__

print("Mi primer gato se llama", gato_1.nombre, "tiene", gato_1.edad, "años y es de raza", gato_1.raza)

# objeto 02

# crear ingresando valores por teclado

nombre = input("Ingresa el nombre del segundo gato: ")
edad = int(input("Ingresa la edad del segundo gato: "))
raza = input("Ingresa la raza del segundo gato: ")

gato_2 = Gato(nombre, edad, raza)

# Presentar objeto; usar el método __st__

print("Mi segundo gato se llama", gato_2.nombre, "tiene", gato_2.edad, "años y es de raza", gato_2.raza)

