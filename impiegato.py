class Employee:
    def __init__(self, nome, cognome, salario):
        self._nome = nome
        self._cognome = cognome
        self._salario = salario
    def __repr__(self):
        return self._nome + " " + self._cognome + " " + str(self._salario)
class Manager(Employee):
    def __init__(self, nome, cognome, salario, reparto):
        super().__init__(nome, cognome, salario )
        self._reparto = reparto
    def __repr__(self):
        return self._nome + " " + self._cognome + " " + str(self._salario) + " " + self._reparto

x = Manager("Grent", "Sota", 3000, "Reparto AI")
y = Employee("Giorgio", "Rossi", 2500)

print(x)
print (y)