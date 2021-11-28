#Ejercicio5

class Alumno:
    def __init__(self, nomb, num):
        self.nomb = nomb
        self.num = num
        
    
    def Display(self):
        print(f"El nombre del alumno es: {self.nomb}")
        print(f"El número de registro es: {self.num}")
    
    def setAge(self):
        edad = input("Ingrese edad del alumno: ")
        self.edad = edad
        print(f"Edad asignada: {self.edad}")
    def setNota(self):
        nota = input("Ingrese nota del alumno: ")
        self.nota = nota
        print(f"Nota asignada: {self.nota}")


nombre = input("Ingrese nombre del alumno: ")
num = input("Ingrese número de registro: ")

alumno1 = Alumno(nombre,num)
alumno1.Display()
alumno1.setAge()
alumno1.setNota()
