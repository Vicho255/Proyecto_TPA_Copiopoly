import pygame as pg
from Utilidades.settings import TABLERO, TILESIDE
from casillas import Casilla,Casilla_Demacia,Casilla_especial,Casilla_Jonia,Casilla_Noxxuz,Casilla_Zaun, Casilla_Suerte
from ficha import Ficha

class Tablero():

    def __init__(self):

        self.mostrar_superficie = pg.display.get_surface()
        self.sprits_visibles = pg.sprite.Group()
        self.ficha = Ficha("Ficha 1","d:\Proyecto_TPA\Graficos\Ficha_Roja.png",592,592,visible=False)
        self.crear_tablero()

    def crear_tablero(self):

        for linea_index,linea in enumerate(TABLERO):
            i = 0
            i = i+1

            print(f"Fila {i}")
            for col_index, colum in enumerate(linea):
                x = col_index * TILESIDE
                y = linea_index  * TILESIDE

                if colum == 'x':
                    Casilla((x+64,y+64),self.sprits_visibles)
                elif colum == 'e':
                    Casilla_especial((x+64,y+64),self.sprits_visibles)
                    print(x+64, y+64, "Casilla E")
                elif colum == 'n':
                    Casilla_Noxxuz((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla N")
                elif colum == 'd':
                    Casilla_Demacia((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla D")
                elif colum == 'z':
                    Casilla_Zaun((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla Z")
                elif colum == 'j':
                    Casilla_Jonia((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla J")
                elif colum == 's':
                    Casilla_Suerte((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla S")
        self.ficha.visible = True 
    
    def div_ficha(self, screen):
        if self.ficha:
            self.ficha.dibujar(screen)

    def mover_ficha(self,resultado_dado):
        for i in range(resultado_dado):

            j = 0
            j += 1

            if (self.pos_ficha() == (592,592) or 80 < self.pos_ficha()[0] <= 592) and self.pos_ficha()[1] == 592:
                pos_predi = self.pos_ficha()[0] - (64 * resultado_dado)
                print(f"La Siguiente Pocicion es {pos_predi} x")

                if pos_predi >= 80:
                    self.ficha.mov_left()
                                    
            elif (self.pos_ficha() == (80,592) or 592 >= self.pos_ficha()[1] > 80) and self.pos_ficha()[0] == 80:
                pos_predi = self.pos_ficha()[1] - (64 * resultado_dado)
                print(f"La Siguiente Pocicion es {pos_predi} y")

                if pos_predi >= 80:
                    self.ficha.mov_top()

            elif (self.pos_ficha() == (80,80) or 80 <= self.pos_ficha()[0] < 592) and self.pos_ficha()[1] == 80:
                pos_predi = self.pos_ficha()[0] + (64 * resultado_dado)
                print(f"La Siguiente Pocicion es {pos_predi} x")

                if pos_predi <= 592:
                    self.ficha.mov_rigth()

            elif (self.pos_ficha() == (592,80) or 80 <= self.pos_ficha()[1] < 592) and self.pos_ficha()[0] == 592:
                pos_predi = self.pos_ficha()[1] + (64 * resultado_dado)
                print(f"La Siguiente Pocicion es {pos_predi} y")

                if pos_predi <= 592:
                    self.ficha.mov_bottom()

    def pos_ficha(self):
        return self.ficha.rect.x , self.ficha.rect.y

    def run(self):

        self.sprits_visibles.draw(self.mostrar_superficie)