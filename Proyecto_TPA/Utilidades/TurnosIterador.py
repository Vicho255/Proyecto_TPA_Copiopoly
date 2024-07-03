class IterarTurno:
    def __init__(self, elementos):
        self.elementos = elementos
        self.indice_actual = -1

    def avanzar(self):
        self.indice_actual = (self.indice_actual + 1) % len(self.elementos)
        return self.elementos[self.indice_actual]
