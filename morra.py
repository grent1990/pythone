#Per n = 2 → {CC, CS, CF, SC, SS, SF, FC, FS, FF} 
PUNTI_GIOC1 = 0
PUNTI_GIOC2 = 0
Punteggio_combinato = PUNTI_GIOC1 - PUNTI_GIOC2
while abs(Punteggio_combinato) < 3:
    GIOCATORE1 = input(str("Inserisci la scelta del giocatore 1 tra C: carta, S: sasso e F: forbici!: ")).upper()
    GIOCATORE2 = input(str("Inserisci la scelta del giocatore 2 tra C: carta, S: sasso e F: forbici!: ")).upper()
    if GIOCATORE1 == "C" and GIOCATORE2 == "C":
        PUNTI_GIOC2 += 0
        PUNTI_GIOC1 += 0
    elif GIOCATORE1 == "S" and GIOCATORE2 == "S":
        PUNTI_GIOC2 += 0
        PUNTI_GIOC1 += 0
    elif GIOCATORE1 == "F" and GIOCATORE2 == "F":
        PUNTI_GIOC2 += 0
        PUNTI_GIOC1 += 0
    elif GIOCATORE1 == "C" and GIOCATORE2 == "S":
        PUNTI_GIOC2 += 0
        PUNTI_GIOC1 += 1
    elif GIOCATORE1 == "C" and GIOCATORE2 == "F":
        PUNTI_GIOC2 += 1
        PUNTI_GIOC1 += 0
    elif GIOCATORE1 == "S" and GIOCATORE2 == "F":
        PUNTI_GIOC2 += 0
        PUNTI_GIOC1 += 1
    elif GIOCATORE1 == "S" and GIOCATORE2 == "C":
        PUNTI_GIOC2 += 0
        PUNTI_GIOC1 += 1
    elif GIOCATORE1 == "F" and GIOCATORE2 == "C":
        PUNTI_GIOC2 += 1
        PUNTI_GIOC1 += 0
    elif GIOCATORE1 == "F" and GIOCATORE2 == "S":
        PUNTI_GIOC2 += 0
        PUNTI_GIOC1 += 1
    else:
        print("Valore non ammesso!")
    print ("Il punteggio sta: ", PUNTI_GIOC1,":",PUNTI_GIOC2)
    Punteggio_combinato = PUNTI_GIOC1 - PUNTI_GIOC2

if PUNTI_GIOC1 > PUNTI_GIOC2:
    print ("Vince il giocatore 1")
else:
    print("Vince il giocatore 2")