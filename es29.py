citta = []
escursione = []
massima = []
minima = []
contatore = 1
while True:
    nome = input("Inserisci il nome della citta: ")
    citta.append(nome)
    valore = int(input("Inserisci il valore di controllo per l'escursione termica: "))
    massim = int(input("Inserire la temperatura massima registrata: "))
    massima.append(massim)
    minim = int(input("Inserisci temperatura minima registrata: "))
    minima.append(minim)
    escursion = massim-minim
    print ("L'escursione termica e di: ", escursione, "gradi")
    escursione.append(escursion)
    if citta == 1:
        contatore += 1
    else:
        continue
    if escursione == valore:
        print("L'escursione termica presenta un valore accettabile")
    elif escursione > valore:
        print("L'escursione termica e elevata")
        contatore +=1
    elif escursione < valore:
        print("L'escursione termica presenta un valore basso")
    else:
        print("I valori inseriti non sono accettabili")
    print (citta)
    print (massima)
    print (minima)
    x= input("Se vuoi continuare scrivi 1, se no inserisci 0 ")
    if x== "0":
        break
    else:
        continue
print(contatore)