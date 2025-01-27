contatore = 0
numero = input("Inserisci un numero: ")
somma = 0

while numero != "fine":
    contatore += 1
    somma += float(numero)
    numero = input("Inserisci un altro numero: ")
print ("La tua media è: ", somma/contatore)
