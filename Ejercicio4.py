#Ejercicio4

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def area(self):
        ar = self.largo * self.ancho
        print(f"El área del rectangulo es {ar}")


largo = float(input("Ingrese largo del rectangulo: "))
ancho = float(input("Ingrese ancho del rectangulo: "))

rectangulo1 = RECTANGULO(largo,ancho)
rectangulo1.area()