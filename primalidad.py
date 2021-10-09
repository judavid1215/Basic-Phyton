def run():
    numero=int(input("Escribe el numero que quieres evaluar: "))
    primalidad=es_primo(numero)
    if primalidad==True: 
        print(f"El numero {numero} es primo")
    else: 
        print(f'El numero {numero} no es primo')

    pass

def es_primo(numero):
    
    contador=0
    for i in range(1, numero+1):
        if i==1 or i==numero:
            continue
        if numero%i==0: 
            contador+=1
    if contador==0:
        return True
    else:
        return False
    

if __name__=='__main__':
    run()