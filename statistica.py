contenitore = []

for voto in range(10):
    valutazione = input("Inserisci la tua valutazione che va da 1 a 5: ")
    contenitore.append(int(valutazione))
contenitore.remove(min(contenitore))
contenitore.remove(min(contenitore))
print(contenitore)
print("La tua media è: ", sum(contenitore)/len(contenitore))