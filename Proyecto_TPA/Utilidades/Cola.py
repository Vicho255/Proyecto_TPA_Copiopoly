class Cola2:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.append(item)

    def avanzar(self):
        elemento = self.items.pop(0)
        self.items.append(elemento)
        return elemento

    def tamano(self):
        return len(self.items)

    def mostrar(self):
        return self.items
    
    def primero(self):
        return self.items[0]
    
    def ultimo(self):
        return self.items[-1]
    
turno = Cola2()
jugadores = {"J1": 1, "J2": 2, "J3": 3, "J4": 4}

for i in jugadores:
    turno.agregar(i)

def turnos(cola):

    actual = cola.avanzar()
    print(actual)
    print(cola.mostrar())

turnos(turno)