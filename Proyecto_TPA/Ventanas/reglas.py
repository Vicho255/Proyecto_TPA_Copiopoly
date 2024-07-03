import pygame as pg
import sys
from Utilidades.settings import *
from Utilidades.Texto import Texto

class Reglas():

    def __init__(self, pantalla, administrador):
        
        self.pantalla = pantalla
        self.admin = administrador
        self.reglas = Texto(dimension_fuente= 30, cadena= texto_reglas)
        self.teclas_presionado_escape = False

    def iniciar(self):
        self.pantalla.fill(MONO)
        self.reglas.Dibujar(self.pantalla)

        teclas = pg.key.get_pressed()

        if teclas[pg.K_ESCAPE] and not self.teclas_presionado_escape:
            self.teclas_presionado_escape = True
            self.admin.set_etapa("menu")
            if self.teclas_presionado_escape:
                self.teclas_presionado_escape = False