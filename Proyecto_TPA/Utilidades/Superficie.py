import pygame as pg
from Utilidades.settings import BLANCO

class Superficie:
    '''
        Descripcion: Superficie que se basa en la clase Surface de pygame, pero potenciando su funcionalidad se han agregado los atributos de posicion y color, estos en pos de mejorar la obtencion de posiciones de objetos que estan sobre superficies en posiciones respecto a la pantalla.
        Atributos:
            dimensiones(tuple(int)): tupla de largo 2 que en su posicion 0 esta el ancho y en la posicion 1 el alto
            posicion(tuple(int)): tupla de largo 2 que alberha en la posicion 0 de la tupla el valor de posicion x en el plano, y en el 1 la posicion de y
        Metodos:
            Dibujar: metodo que dibuja la superficie con todos los elementos que estan sobre ella y su color correspondiente
    '''
    def __init__(self, dimensiones, posicion, color=(0,0,0,0)):
        self.ancho, self.alto = self.dimensiones = dimensiones
        self.posicion = posicion
        self.color = color
        self.lienzo = pg.Surface((self.ancho, self.alto), pg.SRCALPHA)
        self.listaElementos = []
       
    def ObtenerPosicion(self):
        return self.posicion
    
    def ObtenerDimensiones(self):
        return self.dimensiones
    
    def ObtenerLienzo(self):
        return self.lienzo
    
    def ObtenerRectangulo(self):
        return pg.Rect(0 , 0 , self.ancho, self.alto)

    def CambiarDimensiones(self, dimensiones):
        self.ancho, self.alto = self.dimensiones = dimensiones
        self.lienzo = pg.Surface((self.ancho, self.alto), pg.SRCALPHA)

    def CambiarPosicion(self, posicion):
        self.posicion = posicion

    def CambiarColor(self, color):
        self.color = color

    def AgregarElemento(self, indice, elemento):
        self.listaElementos.insert(indice, elemento)

    def SustituirElemento(self, indice, elemento):
        self.listaElementos.pop(indice)
        self.listaElementos.insert(indice, elemento)

    def Dibujar(self, ventana):
        self.lienzo.fill(self.color)
        for elemento in self.listaElementos:
            elemento.Dibujar(self.lienzo)
        ventana.blit(self.lienzo, self.posicion)