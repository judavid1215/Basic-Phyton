
def palindromo(palabra):
    palabra=palabra.replace(' ','')
    palabra=palabra.lower()
    print (str(len(palabra)))
    palabra_invertida=palabra[0:len(palabra):1] # Tambien se podria poner asi palabra[::-1]
    print(palabra_invertida)
    if palabra==palabra_invertida:
        return True
    else:
        return False


def run():
    palabra=input("Escribe una palabra: ")
    es_palindromo=palindromo(palabra)
    if es_palindromo==True:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == '__main__':
    run()




