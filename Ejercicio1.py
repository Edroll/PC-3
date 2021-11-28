#Ejercicio1

def contar(x : str):
    list1 = x.strip().split(sep= " ")
    print(f"Lista inicial: {list1}")
    for e in range(list1.count("")):
        list1.remove("")
    print(f"La lista ahora es: {list1}")   
    return len(list1[-1])

enter=input("Ingrese una cadena de texto: ")

print(f"La longitud de la ultima palabra es: {contar(enter)}")
