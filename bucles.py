def run():
    LIMITE=11
    contador=0
    while (contador<=LIMITE):
        potencia_2=2**contador
        print(f'2 elevado a {contador} es igual a {potencia_2}')
        contador=contador+1




if __name__=='__main__':
    run()