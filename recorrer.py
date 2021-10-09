def run():
    nombre= input("Escribe tu nombre: ")
    for letra in nombre:
        print(letra.upper())
    for i in range(0,len(nombre)):
        letra=nombre[i]
        print(letra.upper())
        

if __name__=='__main__':
    run()

