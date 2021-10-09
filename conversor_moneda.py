menu = """"
Binvennido al conversor de moneda 💵
1 - Pesos colombianos 
2 - Pesos argentinos 
3 - Pesos mexicanos 

Elige una opcion : """ 

opcion=int(input(menu)); 


dinero=float(input("Que cantidad quieres cambiar? "));
peso_colombiano=3700;
peso_argentino=65;
peso_mexicano=20; 


if opcion==1:
    dolares=round(dinero/peso_colombiano,2)
elif opcion==2:
    dolares=round(dinero/peso_argentino,2)
elif opcion==3: 
    dolares=round(dinero/peso_mexicano,2)
else: 
    print("Elige una opcion valida")

dolares=str(dolares);
print("Tienes "+dolares+ " dolares");



