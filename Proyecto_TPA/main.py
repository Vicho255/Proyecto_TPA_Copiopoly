import pygame as pg
import sys
from Utilidades.settings import *
from debug import debug
from tablero import *
from Ventanas.reglas import Reglas
from Administrador import Administrador
from Ventanas.menu import Menu
from Ventanas.Juego import Juego

 

class Game():

    def __init__(self):
        pg.init()
 
        self.screen = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption('Copiopoly')
        self.clock = pg.time.Clock()

        self.administradorJuego = Administrador('menu')
        self.reglas = Reglas(self.screen, self.administradorJuego)
        self.menu = Menu(self.screen, self.administradorJuego)
        self.juego = Juego(self.screen, self.administradorJuego)


        self.etapas = {
            'menu': self.menu, 'juego': self.juego, 'reglas': self.reglas
        }

    def run(self):

        while True:

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.etapas[self.administradorJuego.get_etapa()].iniciar()

            pg.display.update()
            self.clock.tick(FPS)



if __name__ == '__main__':
    game = Game()
    game.run()