

def suma():
    while True:
        print("Se realizara una SUMA")
        try:
            a = float(input("Ingrese primer número: "))
            b = float(input("Ingrese segundo número: "))
            return(a+b)
            break
        except:
            print("Error: tipo de dato no valido")

def resta():
    while True:
        print("Se realizara una RESTA")
        try:
            a = float(input("Ingrese primer número: "))
            b = float(input("Ingrese segundo número: "))
            return(a-b)
            break
        except:
            print("Error: tipo de dato no valido")

def producto():
    while True:
        print("Se realizara una MULTIPLICACIÓN")
        try:
            a = float(input("Ingrese primer número: "))
            b = float(input("Ingrese segundo número: "))
            return(a*b)
            break
        except:
            print("Error: tipo de dato no valido")

def division():
    while True:
        print("Se realizara una DIVISIÓN")
        try:
            a = float(input("Ingrese primer número: "))
            b = float(input("Ingrese segundo número: "))
            if(b==0):
                print("No es posible dividir entre 0")
                division()
            else:
                return(a/b)
                break
        except:
            print("Error: tipo de dato no valido")


