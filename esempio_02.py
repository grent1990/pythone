#esempio_02.py

# ottenere 1 numero intero e una lettera. voglio in output 


numero = int(input("Inserisci la lunghezza: "))
lettera = str(input("Inserisci una lettera"))

contatore = 1
for operazione in range (numero):
    operazione = (" " * numero + lettera * contatore)
    contatore += 2
    numero -= 1
    print(operazione)
