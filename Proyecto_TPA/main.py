import pygame as pg
import sys
from settings import *
from debug import debug
from tablero import *
from Boton import Boton
from reglas import Reglas


class Game():

    def __init__(self):

        self.screen = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption('Copiopoly')
        self.clock = pg.time.Clock()

        self.tablero = Tablero()
        self.reglas = Reglas(self.screen)
        
        self.iniciar_b = Boton(COLOR_1,ANCHO//2 - 100, 200, 200, 50, "Iniciar")
        self.salir_b = Boton(COLOR_1,ANCHO//2 - 100, 500, 200, 50, "Salir")
        self.regresar_b = Boton(COLOR_1,ANCHO//2 - 100, 400, 200, 50, "Regresar")
        self.reglas_b = Boton(COLOR_1,ANCHO//2 - 100, 300, 200, 50, "Reglas")
        self.mostrar_r = False
        self.mostra_pantalla_tex = False

    def get_screen(self):
        return self.screen

    def run(self):

        en_menu = True

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit
                if en_menu:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if self.iniciar_b.rect.collidepoint(event.pos):
                            en_menu = False
                            self.mostrar_r = False
                        elif self.reglas_b.rect.collidepoint(event.pos):
                            self.mostra_pantalla_tex = True
                            en_menu = False
                        elif self.salir_b.rect.collidepoint(event.pos):
                            pg. QUIT()
                            sys.exit()
                else:
                    if self.mostra_pantalla_tex:
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_ESCAPE:
                                self.mostra_pantalla_tex = False
                                en_menu = True
                    elif not self.mostra_pantalla_tex:
                        if event.type == pg.MOUSEBUTTONDOWN:
                            if self.regresar_b.rect.collidepoint(event.pos):
                                en_menu = True
                        elif event.type == pg.KEYDOWN:
                            if event.key == pg.K_ESCAPE:
                                self.mostrar_r = True
            
            if en_menu:
                self.mostrar_menu()
            else:
                if self.mostra_pantalla_tex:
                    self.reglas.mostrar_texto("Esto es una pueba")
                elif not self.mostra_pantalla_tex:
                    self.jugar()
            
            pg.display.update()
            self.clock.tick(FPS)
    
    def mostrar_menu(self):
        self.screen.fill(MONO)
        self.iniciar_b.actualizar(self.screen)
        self.salir_b.actualizar(self.screen)
        self.reglas_b.actualizar(self.screen)

    def jugar(self):
        self.screen.fill(MONO)
        self.tablero.run()
        if self.mostrar_r:
            overlay = pg.Surface((ANCHO,ALTO), pg.SRCALPHA)
            overlay.fill((0, 0, 0, 100))
            self.screen.blit(overlay, (0, 0))

            self.regresar_b.actualizar(self.screen)

class Fichas():

    def __init__(self):
        self.x = 640
        self.y = 640

    def mov_left(self,da):
        self.x -= da

    def mov_top(self,da):
        self.y += da

    def mov_rigth(self,da):
        self.x += da

    def mov_down(self,da):
        self.y -= da

    def draw(self):
        pg.draw.rect(Game.get_screen(),MONO,(self.x,self.y))



if __name__ == '__main__':
    game = Game()
    game.run()