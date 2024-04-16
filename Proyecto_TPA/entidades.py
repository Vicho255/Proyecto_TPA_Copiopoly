import pygame as pg
from funciones import *

class Banca():

    def __init__(self):

        self.dinero = 10000000000000000000000000000000.0
        self.propiedades = {
            'asd' : 100,
            'dsa' : 25
        }
    
    def get_propiedades(self):
        return self.propiedades
    
    def set_dinero(self,plata):
        if plata == salida: self.dinero = self.dinero - salida; return self.dinero
        if plata == impuesto: self.dinero = self.dinero + impuesto; return self.dinero

    def set_propiedades(self,propiedad):
        self.propiedades.pop(propiedad)
        return self.propiedades
    


class Jugador():

    def __init__(self):

        self.dinero = 1500
        self.Propiedades = {

        }

    def ganar_dinero():
        pass

    def perder_dinero():
        pass

    def adquirir_propiedad():
        pass
