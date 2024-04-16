import pygame as pg
from settings import *
from casillas import *

class Tablero():

    def __init__(self):

        self.mostrar_superficie = pg.display.get_surface()

        self.sprits_visibles = pg.sprite.Group()

        self.crear_tablero()

    def crear_tablero(self):

        for linea_index,linea in enumerate(TABLERO):
            for col_index, colum in enumerate(linea):
                x = col_index * TILESIDE
                y = linea_index  * TILESIDE

                if colum == 'x':
                    Casilla((x+64,y+64),self.sprits_visibles)
                if colum == 'e':
                    Casilla_especial((x+64,y+64),self.sprits_visibles)
    
    def run(self):

        self.sprits_visibles.draw(self.mostrar_superficie)