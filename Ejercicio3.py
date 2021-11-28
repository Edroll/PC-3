#Ejercicio3

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        ar = 3.14 * (self.radio**2)
        print(f"El área del circulo es {ar}")

radio = float(input("Ingrese radio del circulo: "))
circulo1 = CIRCULO(radio)
circulo1.area()