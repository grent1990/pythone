class Figura :
    def __init__(self,initialVolume = 0.0, initialWeight = 0.0 ):
        self._volume = initialVolume
        self._peso = initialWeight
    def volume(self):
        return self._volume
    def weight(self):
        return self._peso
    def peso_specifico(self):
        if self._volume == 0.0:
            return "Volume non impostato"
        return self._peso/self._volume

a = Figura(21.9)
b = Figura()
c = Figura(15.9, 22.0)
print(type(a))
print(a.volume(), b.volume(), c.volume())
print(a.weight(), b.weight(), c.weight())
print(b.peso_specifico())
print(c.peso_specifico())