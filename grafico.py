import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery') # selezione dello stile del grafico
# valori del grafico
n = 20
x = np.sin(np.linspace(0, 2*np.pi, n)) # array x con 20 valori distribuiti tra 0 e 2*np.pi applicando la funzione np.sin, valori ass x
y = np.cos(np.linspace(0, 2*np.pi, n)) # come sopra ma applica la funzione np.cos, asse y
z = np.linspace(0, 1, n) # array di 20 valori, asse z, rappresenta profondità o altezza

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"}) # creazione oggetto figura, specificando grafico 3d
ax.stem(x, y, z) # creazione stemplot, grafico a stelo, utile per mostrare dati discreti con visualizzazione chiara

# etichette 
ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show() # visualizza il grafico sullo schermo