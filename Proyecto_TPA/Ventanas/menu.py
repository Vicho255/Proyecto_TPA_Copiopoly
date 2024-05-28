import pygame as pg
import sys
from Utilidades.settings import *
from Utilidades.Boton import Boton

class Menu():

    def __init__(self, pantalla, administrador):
        pg.init()
        self.pantalla = pantalla
        self.admin = administrador

        self.botonInicio = Boton('Iniciar', 40, (200, 50), posicion= (100, 600), metodo= self.cambiarEtapa, argumento= 'juego', texto_centrado= True)
        self.botonReglas = Boton('Reglas', 40, (200, 50), posicion= (100, 700), metodo= self.cambiarEtapa, argumento= 'reglas', texto_centrado= True)
        self.botonSalir = Boton('Salir', 40, (200, 50), posicion= (100, 800), metodo= self.salir, texto_centrado= True)
        

    def iniciar(self):
        self.pantalla.fill(MONO)
        self.botonInicio.Dibujar(self.pantalla)
        self.botonReglas.Dibujar(self.pantalla)
        self.botonSalir.Dibujar(self.pantalla)

    def resetear(self):
        self.botonSalir.Resetear()

    def ManejadorEventos(self):
        pass

    def cambiarEtapa(self, etapa):
        self.admin.set_etapa(etapa)

    def salir(self):
        pg.quit()
        sys.exit()