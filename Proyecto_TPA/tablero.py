import pygame as pg
from settings import *
from casillas import *
from ficha import Ficha

class Tablero():

    def __init__(self):

        self.mostrar_superficie = pg.display.get_surface()
        self.sprits_visibles = pg.sprite.Group()
        self.ficha = Ficha("Ficha 1","d:\Proyecto_TPA\Graficos\Ficha_Roja.png",592,592,visible=False)
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
    
    def inicia(self):
        self.ficha.visible = True
    
    def div_ficha(self, screen):
        if self.ficha:
            self.ficha.dibujar(screen)

    def mover_ficha(self,direccion):
        if direccion == "arriba":
            self.ficha.mov_top()
        elif direccion == "abajo":
            self.ficha.mov_bottom()
        elif direccion == "izquierda":
            self.ficha.mov_left()
        elif direccion == "derecha":
            self.ficha.mov_rigth()

    def pos_ficha(self):
        return self.ficha.rect.x , self.ficha.rect.y

    def run(self):

        self.sprits_visibles.draw(self.mostrar_superficie)