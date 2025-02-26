file = input("Quale file vuoi aprire? ")

try:
    with open(file, "r") as f:
        contenuto = f.read()  
    numeri = contenuto.split()  
    numeri.reverse()  
    print("\n".join(numeri))

except FileNotFoundError:
    print("Il file non è stato trovato!")
except Exception:
    print(f"Si è verificato un errore:")