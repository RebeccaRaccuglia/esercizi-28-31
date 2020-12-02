nome=[]
lanci=[]
contatore= 1
while True:
    nome_cand=input("inserisci nome studente " + str(contatore))
    lanci_cand= input("inserisci il numero di lanci di "+ nome_cand)
    nome.append (nome_cand)
    lanci.append(lanci_cand)
    contatore += 1
    domanda= int(input("vuoi inserire un nuovo candidato? se si digita 1 se no digita 0"))
    if domanda== 0:
        break
    else:
        continue
print(max(lanci))