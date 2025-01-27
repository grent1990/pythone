reddito = float(input("Inserisci il tuo reddito: "))
#le aliquote dell'imposta
ALIQUOTA_1 = 0.23
ALIQUOTA_2 = 0.35
ALIQUOTA_3 = 0.43
#fascie alle quali applicare le aliquote con la 3 fascia che è >50k
FASCIA_1 = 28000
FASCIA_2 = 50000


while reddito <= 0:
        print("Il valore inserito non è valido.")
        reddito = float(input("Inserisci il tuo reddito: "))
if reddito <= 28000:
    imposta = reddito * ALIQUOTA_1
elif reddito <= 50000:
    imposta = (FASCIA_1 * ALIQUOTA_1) + (reddito - FASCIA_1) * ALIQUOTA_2
elif reddito > 50000:
            imposta = (FASCIA_1 * ALIQUOTA_1) + ((FASCIA_2 - FASCIA_1) * ALIQUOTA_2) + ((reddito - FASCIA_2) * ALIQUOTA_3)
reddito_netto = reddito - imposta
print ("Il tuo reddito netto è: ", reddito_netto)
print ("La tua imposta sul reddito è: ", imposta)

