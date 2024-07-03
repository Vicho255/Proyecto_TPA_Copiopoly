import pygame as pg
from funciones import *

class Banca():

    def __init__(self):

        self.dinero = 100000
        self.propiedades = [
            {"Nombre":"Bastion Imortal", "precio":100},
            {"Nombre":"Roza Negra", "precio":100},
            {"Nombre":"Pozo", "precio":100},
            {"Nombre":"Respiradero", "precio":100},
            {"Nombre":"Canales", "precio":100},
            {"Nombre":"Nivel del Paceo", "precio":100},
            {"Nombre":"Demacia 1", "precio":100},
            {"Nombre":"Demacia 2", "precio":100},
            {"Nombre":"Demacia 3", "precio":100},
            {"Nombre":"Jonia 1", "precio":100},
            {"Nombre":"Jonia 2", "precio":100}
        ]
        
    
    def get_propiedades(self):
        return self.propiedades
    
    def get_dinero_banca(self):
        return self.dinero
    
    def ganar_dinero_banca(self,cantidad):

        self.dinero += cantidad
        return self.dinero

    def perder_dinero_banca(self, cantidad):

        self.dinero -= cantidad
        return self.dinero

    def set_propiedades(self,propiedad):
        self.propiedades.pop(propiedad)
        return self.propiedades

class Jugador():
    
    def __init__(self, ficha, nombre):
        self.nomFicha = ficha
        self.nombre = nombre
        self.dinero = 1500
        self.Propiedades = []

    def ganar_dinero(self, cantidad):

        self.dinero += cantidad
        return self.dinero

    def perder_dinero(self,cantidad):

        self.dinero -= cantidad
        return self.dinero
    
    def get_dinero_restante(self):
        return self.dinero
    
    def get_Propiedades(self):
        return self.Propiedades

    def adquirir_propiedad(self,propiedad):
            
        if self.dinero >= propiedad["precio"]:
            self.dinero -= propiedad["precio"]
            self.Propiedades.append(propiedad)
            return True
        return False

hola = {"H":1,
        "O":2,
        "L":3,
        "A":4}
print(hola)
hola.pop("O")
print(hola)