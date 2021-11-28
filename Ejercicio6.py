def cadena():
    
    while True:
        try:
            text= input("Ingrese las notas separadas por coma: ")
            text = text.split(sep=",")
            for i,a in enumerate(text):
                text[i]=int(text[i].strip())
            break
        except:
            print("Ingrese solo números")
    return text
        
notas = cadena()

print(f"notas: {notas}")
    
