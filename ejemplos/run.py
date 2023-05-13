"""
Crear dos objetos de la clase Auto
"""

class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

# Crear objeto 01
auto_1 = Auto("Toyota", "Corolla", 2020)

# Presentar objeto; usar el método __str__
print("Mi primer auto es de marca: ", auto_1.marca)

# Crear objeto 02 ingresando valores por teclado
marca = input("Ingresa la marca del segundo auto: ")
modelo = input("Ingresa el modelo del segundo auto: ")
año = int(input("Ingresa el año del segundo auto: "))
auto_2 = Auto(marca, modelo, año)

# Presentar objeto; usar el método __str__
print("Mi segundo auto es de marca: ", auto_2.marca)


