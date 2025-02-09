#esempio_03

#ricevere in input una sequenza
# 1 - 2, 1 - 2
# tennis 15 - 0, 15 - 15, 30 - 15, 30 - 30, 40 - 30, 40 - 40.

giocatore1 = 0
giocatore2 = 0
set_giocatore1 = 0
set_giocatore2 = 0
vantaggio1 = 0
vantaggio2 = 0
while True:
    punto = int(input("Chi ha fatto il punto tra giocatore 1 e 2? "))
    if punto == 1 or punto == 2:
        if punto == 1:
            if giocatore1 < 40:
                giocatore1 += 15
            if giocatore1 == 40 and giocatore2 == 40: # controllo del vantaggio
                vantaggio1 += 1
                vantaggio2 -= 1
                if vantaggio1 == 2: # vittoria
                    set_giocatore1 += 1
                    giocatore1 = 0
                    giocatore2 = 0
                    vantaggio1 = 0
                    vantaggio2 = 0
            if giocatore1 == 40 and giocatore2 != 40: # verifica set senza vantaggi
                set_giocatore1 += 1
                giocatore1 = 0
                giocatore2 = 0
            elif giocatore1 > 30: # trasformazione punteggio in 40
                giocatore1 = 40

        if punto == 2: # codice speculare di if punto == 1:
            if giocatore2 < 40:
                giocatore2 += 15
            if giocatore2 == 40 and giocatore1 == 40:
                vantaggio2 += 1
                vantaggio1 -= 1
                if vantaggio2 == 2:
                    set_giocatore2 += 1
                    giocatore1 = 0
                    giocatore2 = 0
                    vantaggio1 = 0
                    vantaggio2 = 0
            if giocatore2 == 40 and giocatore1 != 40:
                    set_giocatore2 += 1
                    giocatore1 = 0
                    giocatore2 = 0
            elif giocatore2 > 30:
                giocatore2 = 40
        
    else:
        print("Hai inserito un numero diverso da 1 o 2!!!")
    print("Il punteggio attuale è: " , giocatore1 ,":" , giocatore2 )
    print("Il punteggio dei Set è: ", set_giocatore1 , ":", set_giocatore2)
    print ("I vantaggi sono:", vantaggio1, ":", vantaggio2)