import pygame as pg
import sys
from settings import *
from debug import debug
from tablero import *
from Boton import Boton
from reglas import Reglas
from funciones import dado_fun
from dado_img import Dado

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
                            pg.quit()
                            sys.exit()
                else:
                    if self.mostra_pantalla_tex:
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_ESCAPE:
                                self.mostra_pantalla_tex = False
                                en_menu = True
                    elif self.mostra_pantalla_tex == False:
                        if event.type == pg.MOUSEBUTTONDOWN:
                            if self.regresar_b.rect.collidepoint(event.pos):
                                en_menu = True
                        elif event.type == pg.KEYDOWN:
                            if event.key == pg.K_ESCAPE:
                                self.mostrar_r = True
                            elif event.key == pg.K_SPACE:
                                pos_ficha = self.tablero.pos_ficha()
                                print(pos_ficha)
                                resultado_dado = dado_fun()
                                print(resultado_dado)
                                if resultado_dado == 1:
                                    dado = Dado(imagen= "d:\Proyecto_TPA\Graficos\Dado\Dado_1.png")
                                    dado.dibujar(self.screen)
                                elif resultado_dado == 2:
                                    dado = Dado(imagen= "d:\Proyecto_TPA\Graficos\Dado\Dado_2.png")
                                    dado.dibujar(self.screen)
                                elif resultado_dado == 3:
                                    dado = Dado(imagen= "d:\Proyecto_TPA\Graficos\Dado\Dado_3.png")
                                    dado.dibujar(self.screen)
                                elif resultado_dado == 4:
                                    dado = Dado(imagen= "d:\Proyecto_TPA\Graficos\Dado\Dado_4.png")
                                    dado.dibujar(self.screen)
                                elif resultado_dado == 5:
                                    dado = Dado(imagen= "d:\Proyecto_TPA\Graficos\Dado\Dado_5.png")
                                    dado.dibujar(self.screen)
                                elif resultado_dado == 6:
                                    dado = Dado(imagen= "d:\Proyecto_TPA\Graficos\Dado\Dado_6.png")
                                    dado.dibujar(self.screen)
                                for i in range(resultado_dado):
                                    if pos_ficha == (592,592):
                                        self.tablero.mover_ficha("izquierda")
                                    elif pos_ficha == (80,592):
                                        self.tablero.mover_ficha("arriba")
                                    elif pos_ficha == (80,80):
                                        self.tablero.mover_ficha("derecha")
                                    elif pos_ficha == (592,80):
                                        self.tablero.mover_ficha("abajo")
            
            if en_menu:
                self.mostrar_menu()
            else:
                if self.mostra_pantalla_tex:
                    self.reglas.mostrar_texto(texto_reglas)
                elif not self.mostra_pantalla_tex:
                    self.jugar()
                    self.tablero.inicia()
                    self.tablero.div_ficha(self.screen)

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


if __name__ == '__main__':
    game = Game()
    game.run()