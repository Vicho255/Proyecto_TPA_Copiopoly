import pygame as pg

class Administrador():

    def __init__(self, etapaActual):
        self.etapaActual = etapaActual

    def get_etapa(self):
        return self.etapaActual
    
    def set_etapa(self, etapa):
        self.etapaActual = etapa