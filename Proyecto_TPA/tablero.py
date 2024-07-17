import pygame as pg
from Utilidades.settings import TABLERO, TILESIDE
from Utilidades.TurnosIterador import IterarTurno
from casillas import *
from ficha import Ficha
from entidades import *

class Tablero():

    def __init__(self):

        self.mostrar_superficie = pg.display.get_surface()
        self.sprits_visibles = pg.sprite.Group()
        self.ficha = Ficha("Ficha Roja","d:\Proyecto_TPA\Graficos\Ficha_Roja.png",592,592,visible=False)
        self.ficha2 = Ficha("Ficha Verde","d:\Proyecto_TPA\Graficos\Ficha_Verde.png",528,592,visible=False)
        self.ficha3 = Ficha("Ficha Azul","d:\Proyecto_TPA\Graficos\Ficha_Azul.png",592,528,visible=False)
        self.ficha4 = Ficha("Ficha Amarilla","d:\Proyecto_TPA\Graficos\Ficha_Amarilla.png",528,528,visible=False)

        self.jugador1 = Jugador(ficha=self.ficha.nombre, nombre="Jugador 1")
        self.jugador2 = Jugador(ficha=self.ficha2.nombre, nombre="Jugador 2")
        self.jugador3 = Jugador(ficha=self.ficha3.nombre, nombre="Jugador 3")
        self.jugador4 = Jugador(ficha=self.ficha4.nombre, nombre="Jugador 4")

        self.jugadores = [self.jugador1, self.jugador2, self.jugador3, self.jugador4]

        self.turnoj = IterarTurno(self.jugadores)

        self.fichas = [self.ficha, self.ficha2, self.ficha3, self.ficha4]

        self.turno = IterarTurno(self.fichas)

        self.crear_tablero()

    def crear_tablero(self):

        for linea_index,linea in enumerate(TABLERO):
            i = 0
            i = i+1
            for col_index, colum in enumerate(linea):
                x = col_index * TILESIDE
                y = linea_index  * TILESIDE

                if colum == 'x':
                    Casilla((x+64,y+64),self.sprits_visibles,imagen=('Graficos/casilla.png'))
                elif colum == 'e':
                    Casilla((x+64,y+64),self.sprits_visibles, imagen= ('Graficos/Casilla_especial.png'))

                elif colum == 'n1' or colum == 'n2' or colum == 'n3':
                    Casilla((x+64, y+64), self.sprits_visibles,imagen= ('Graficos/Casilla_Noxus.png'))

                elif colum == 'd1' or colum == 'd2' or colum == 'd3':
                    Casilla((x+64, y+64), self.sprits_visibles,imagen= ('Graficos/Casilla_Demacia.png'))

                elif colum == 'z1' or colum == 'z2' or colum == 'z3':
                    Casilla((x+64, y+64), self.sprits_visibles,imagen= ('Graficos/Casilla_Zaund.png'))

                elif colum == 'j1'or colum == 'j2':
                    Casilla((x+64, y+64), self.sprits_visibles,imagen= ('Graficos/Casilla_Jonia.png'))

                elif colum == 's':
                    Casilla((x+64, y+64), self.sprits_visibles,imagen= ('Graficos/Casilla_Suerte.png'))

        
        for ficha in self.fichas:
            ficha.visible = True 
    
    def div_ficha(self, screen):
        for ficha in self.fichas:
            if ficha:
                ficha.dibujar(screen)
                
    def mover_ficha(self, resultado_dado):
        # Obtener la ficha que le toca moverse
        ficha = self.turnoSiguiente()[0]

        for _ in range(resultado_dado):
            
            pos_actual = self.pos_ficha(ficha)
            x, y = pos_actual
            mov = 64

            if (80 < x <= 592 and y in [592, 528]) or (x in [80, 592] and y in [592, 528]):
                # Movimiento hacia la izquierda
                if x - mov >= 80:
                    ficha.mov_left()
                else:
                    ficha.posicion_relativa.x = 80
                    ficha.mov_top()

            elif (x in [80, 144] and 80 < y <= 592) or (x in [80, 144] and y in [592, 528]):
                # Movimiento hacia arriba
                if y - mov >= 80:
                    ficha.mov_top()
                else:
                    ficha.posicion_relativa.y = 80
                    ficha.mov_right()

            elif (x in [80, 592] and y in [80, 144]) or (80 <= x < 592 and y in [80, 144]):
                # Movimiento hacia la derecha
                if x + mov <= 592:
                    ficha.mov_right()
                else:
                    ficha.posicion_relativa.x = 592
                    ficha.mov_bottom()

            elif (x == 592 and 80 <= y < 592) or (x == 592 and y == 80):
                # Movimiento hacia abajo
                if y + mov <= 592:
                    ficha.mov_bottom()
                else:
                    ficha.posicion_relativa.y = 592
                    ficha.mov_left()

            # Actualizar la posición
            x, y = self.pos_ficha(ficha)

            if x < 80:
                ficha.posicion_relativa.x = 80
            elif x > 592:
                ficha.posicion_relativa.x = 592

            if y < 80:
                ficha.posicion_relativa.y = 80
            elif y > 592:
                ficha.posicion_relativa.y = 592


    def pos_ficha(self, ficha):
        return ficha.rect.x, ficha.rect.y

    def turnoSiguiente(self):
        ficha_Siguiente = self.turno.avanzar()
        jugadoS = self.turnoj.avanzar()

        print(ficha_Siguiente.nombre, jugadoS.nombre)
        return ficha_Siguiente, jugadoS

    def run(self):

        self.sprits_visibles.draw(self.mostrar_superficie)