#esempio_01.py
#Fare un ciclo che acquisisce tramite input una sequenza di numeri float e fermarsi tramite un contatore quando le ultime letture sono uguale a 0 per 2 volte

somma = 0.0
valore_precedente = 9999.99
while True:
    valore_corrente = float(input())
    somma += valore_corrente
    if valore_corrente == 0.0 and valore_precedente == 0.0:
        break
    print("Sto per assegnare il valore corrente", valore_corrente, "rimpiazzando il valore precedente")
    valore_precedente = valore_corrente
print("Somma =", somma)