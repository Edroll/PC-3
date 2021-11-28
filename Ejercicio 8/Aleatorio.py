import random
def generate():
    list1 = []
    for aleatory in range(20):
         list1.append(random.randint(1,100))
    return(list1)

def mostrar(p : list):
    print(f"La lista obtenida es: {p}")

def ordenar(n: list):
    n.sort() #para ordenar datos
    print(f"La lista ordenada es: {n}")

if __name__ == "__main__":
    lista = generate()
    mostrar(lista)
    ordenar(lista)
