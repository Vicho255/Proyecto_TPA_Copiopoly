import pygame as pg
from Utilidades.Texto import Texto
from Utilidades.Superficie import Superficie

class Boton:
    def __init__(self, cadena, dimensionFuente, dimensiones, color_texto='white', color=(200,50,75,255), color_colision='red', posicion=(0,0),metodo=None, argumento=None, texto_centrado=False):
        '''
        Descripcion:
        Clase boton para pygame
        Atributos:
            cadena(str): Texto que estara escrito sobre el boton
            dimensionFuente(int): Numero entero que define el tamaño del texto
            dimensiones(tuple(int)): Tupla de largo 2 que almacenar en la posicion 0 el ancho y en la posicion 1 el alto del boton
        Metodos:
            Dibujar(ventana/superficie): Metodo encargado de dibujar el boton sobre una superficie o pantalla.
            Deshabilitar(): Metodo que deshabilita el boton de manera que no se comprueba si se ha presionado.
        '''
        self.superficie = Superficie(dimensiones, posicion, color)
        self.rectangulo = self.superficie.ObtenerRectangulo()
        self.texto = Texto(cadena, dimensionFuente, color=color_texto, texto_centrado=texto_centrado)
        if not texto_centrado:
            self.texto.CentrarTextoVerticalmente()
        self.superficie.AgregarElemento(0, self.texto)
        self.color = color
        self.color_colision = color_colision
        self.colision= False
        self.habilitado = True
        self.Presionado = False
        self.metodo = metodo
        self.argumento = argumento
        self.iniciado = True

    def __str__(self):
        self.texto.__str__()

    def CambiarTexto(self, cadena):
        self.texto.CambiarCadena(cadena)
        self.superficie.SustituirElemento(0, self.texto)

    def CambiarDimensionTexto(self, dimension):
        self.texto.CambiarDimensionFuente(dimension)
        self.superficie.SustituirElemento(0, self.texto)

    def CambiarColorTexto(self, color):
        self.texto.CambiarColor(color)
        self.superficie.SustituirElemento(0, self.texto)
    
    def CambiarColor(self, color):
        self.superficie.CambiarColor(color)

    def CambiarDimensiones(self, dimensiones):
        self.superficie.CambiarDimensiones(dimensiones)
        self.rectangulo = self.superficie.ObtenerRectangulo()

    def CambiarPosicion(self, posicion):
        self.superficie.CambiarPosicion(posicion)
        self.rectangulo = self.superficie.ObtenerRectangulo()

    def Deshabilitar(self):
        self.habilitado = False

    def Resetear(self):
        self.iniciado = True

    def Dibujar(self, ventana):
        if self.iniciado:
            self.Detectar_Presionar()
            if not self.Presionado:
                self.iniciado = False
        else:
            if self.habilitado:
                self.ManejoEventos()
        self.superficie.Dibujar(ventana)

    def ManejoEventos(self):
        self.Detectar_Colision()
        self.Detectar_Presionar()
        if self.colision and self.Presionado:
            if self.metodo is not None and self.argumento is not None:
                #print('metodo: ', self.metodo, ', argumento: ', self.argumento)
                self.metodo(self.argumento)
            elif self.metodo is not None:
                self.metodo()
        elif self.colision:
            self.CambiarColor(self.color_colision)
        else:
            self.CambiarColor(self.color)

    def Detectar_Colision(self):
        punto = pg.mouse.get_pos()
        posicion_superficie = self.superficie.ObtenerPosicion()
        punto = (punto[0] - posicion_superficie[0], + punto[1] - posicion_superficie[1] )
        if self.rectangulo.collidepoint(punto):
            self.colision= True
        else:
            self.colision= False

    def Detectar_Presionar(self):
        if pg.mouse.get_pressed()[0]==1:
            self.Presionado = True
        else:
            self.Presionado = False
