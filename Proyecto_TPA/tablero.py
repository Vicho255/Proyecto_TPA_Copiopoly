import pygame as pg
from Utilidades.settings import TABLERO, TILESIDE
from Utilidades.Cola import Cola2
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

        self.banco = Banca()

        self.jugador1 = Jugador(ficha=self.ficha.nombre, nombre="Jugador 1")
        self.jugador2 = Jugador(ficha=self.ficha2.nombre, nombre="Jugador 2")
        self.jugador3 = Jugador(ficha=self.ficha3.nombre, nombre="Jugador 3")
        self.jugador4 = Jugador(ficha=self.ficha4.nombre, nombre="Jugador 4")

        self.jugadores = {
            "Jugador 1": self.jugador1,
            "Jugador 2": self.jugador2,
            "Jugador 3": self.jugador3,
            "Jugador 4": self.jugador4
        }

        self.turnoj = Cola2()
        self.turnoj.agregar(self.jugador1)
        self.turnoj.agregar(self.jugador2)
        self.turnoj.agregar(self.jugador3)
        self.turnoj.agregar(self.jugador4)

        self.fichas = {
            "Ficha 1": self.ficha,
            "Ficha 2": self.ficha2,
            "Ficha 3": self.ficha3,
            "Ficha 4": self.ficha4

        }

        self.turno = Cola2()
        self.turno.agregar(self.ficha)
        self.turno.agregar(self.ficha2)
        self.turno.agregar(self.ficha3)
        self.turno.agregar(self.ficha4)

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
                elif colum == 'n1' or colum == 'n2' or colum == 'n3':
                    Casilla_Noxxuz((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla N")
                elif colum == 'd1' or colum == 'd2' or colum == 'd3':
                    Casilla_Demacia((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla D")
                elif colum == 'z1' or colum == 'z2' or colum == 'z3':
                    Casilla_Zaun((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla Z")
                elif colum == 'j1'or colum == 'j2':
                    Casilla_Jonia((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla J")
                elif colum == 's':
                    Casilla_Suerte((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla S")
        
        for ficha in self.fichas.values():
            ficha.visible = True 
    
    def div_ficha(self, screen):
        for ficha in self.fichas.values():
            if ficha:
                ficha.dibujar(screen)
                
    def mover_ficha(self,resultado_dado):
        fichat = self.turnoSiguiente()
        ficha = fichat[0]

        for _ in range(resultado_dado):
            pos_actual = self.pos_ficha(ficha)
            x, y = pos_actual
            mov = 64

            if ((x in [592, 528] and y in [592, 528]) or (80 < x <= 592 and y in [592, 528])):
                # Movimiento hacia la izquierda
                if x - mov > 80:
                    ficha.mov_left()
                else:
                    ficha.posicion_relativa.x = 80
                    ficha.mov_top()

            elif ((x in [80, 144] and y in[592, 528]) or (x in [80, 144] and y in [592, 528])):
                # Movimiento hacia arriba
                if y - mov > 80:
                    ficha.mov_top()
                else:
                    ficha.posicion_relativa.y = 80
                    ficha.mov_rigth()

            elif (x in [80, 592] and y == 80) or (80 <= x < 592 and y == 80):
                # Movimiento hacia la derecha
                if x + mov < 592:
                    ficha.mov_rigth()
                else:
                    ficha.posicion_relativa.x = 592
                    ficha.mov_bottom()

            elif (x == 592 and 80 <= y < 592) or (x == 592 and y == 80):
                # Movimiento hacia abajo
                if y + mov < 592:
                    ficha.mov_bottom()
                else:
                    ficha.posicion_relativa.y = 592
                    ficha.mov_left()

            x, y = self.pos_ficha(ficha)

        print(f"Posición final de {ficha.nombre}: ({x}, {y})")


    def pos_ficha(self,ficha):
        return ficha.rect.x , ficha.rect.y
    
    def turnoSiguiente(self):
        ficha_Siguiente = self.turno.avanzar()
        jugadoS = self.turnoj.avanzar()

        print(ficha_Siguiente.nombre)
        return ficha_Siguiente, jugadoS

    def run(self):

        self.sprits_visibles.draw(self.mostrar_superficie)