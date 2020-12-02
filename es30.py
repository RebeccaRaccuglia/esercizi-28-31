numero_cifre=int(input("inserisci il numero di cifre da cui è composto il numero binario che desideri convertire in decimale?"))
print("scrivi le cifre binarie una alla volta a partire da destra")
elevatore_potenze=0
numero_decimale=0
for i in range(numero_cifre):
    cifra=int(input())
    numero_da_sommare=cifra*(2**elevatore_potenze)
    numero_decimale+=numero_da_sommare
    elevatore_potenze+=1
numero_binario=input("non sono sicuro di aver fatto tutto correttamente, riscrivi il numero da sinistra verso destra ")
numero_certo=int(numero_binario,2)
if numero_decimale==numero_certo:
    print("ok, il numero decimale è ",numero_decimale)
else:
    print("prenderò 2 in informatica")
        