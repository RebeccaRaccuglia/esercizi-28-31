numero = int(input("Inserisci il numero decimale da trasformare"))
n = numerobinario = []
quoziente = 1
while True:
    if numero == 0 or quoziente == 0:
        break
    elif quoziente <= numero:
        quoziente = round(numero / 2)
        resto =numero%2
        binario.append(resto)
        numero = quoziente
    else: 
        numero = round(quoziente / 2)
        resto = quozeinte%2
        binario.append(resto)
        quoziente = numero
binario.reverse()
print(binario) 
bin = int(input("Puoi riscrivere il numero binario che e risultato?"))
controllo = int(str(bin), base-2)
print(controllo)
if n == controllo:
    print("ok")
    print("Il numero", bin)
else:
    print("I numeri non coincidono")