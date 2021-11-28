import random
def generate():
    num = random.randint(1,100)
    return(num)

def probar(p : int):
    while True:
        valor = int(input("Ingrese su numero para adivinar: "))
        if (valor == p):
            print("¡Haz Ganado!")
            break
        elif (valor < p):
            print("El numero que ingresaste es menor :(")
        elif (valor > p):
            print("El numero que ingresaste es mayor :(")

