import pygame as pg


class Texto:
    '''
        Descripcion: Clase de Texto, crea una superficie apartir de una cadena de texto
        Atributos:
            cadena(string): valor que se asocia a la cadena de texto apartir de la que se genera la superficie
            dimension_
            posicion(tuple(int)): tupla de largo 2 que alberha en la posicion 0 de la tupla el valor de posicion x en el plano, y en el 1 la posicion de y
        Metodos:
            Dibujar: metodo que dibuja la superficie con todos los elementos que estan sobre ella y su color correspondiendte, es capaz de centrarlo sobre la superficie que se dibuja
    '''
    def __init__(self, cadena, dimension_fuente=15, posicion=(10,10), color=(0,0,0), fuente= 'monogram-extended', texto_centrado = False):
        self.cadena = cadena
        self.posicion = posicion
        self.color = color
        self.nombre_fuente = fuente
        self.fuente = pg.font.Font(f'Graficos/font/{fuente}.ttf', dimension_fuente) 
        self.superficie = self.fuente.render(self.cadena, True, self.color)
        self.texto_centrado_horizontal = self.texto_centrado_vertical = texto_centrado

    def __str__(self):
        return self.cadena
    
    def CambiarDimensionFuente(self, dimension):
        self.fuente = pg.font.Font(f'Graficos/font/{self.nombre_fuente}.tff', dimension)  

    def CambiarFuente(self, fuente):
        self.fuente = pg.font.Font(f'Graficos/font/{fuente}.tff', self.dimension)
        self.superficie = self.fuente.render(self.cadena, True, self.color)
   
    def CambiarCadena(self, cadena):
        self.cadena = cadena
        self.superficie = self.fuente.render(self.cadena, True, self.color)
    
    def CambiarColor(self, color):
        self.color = color
        self.superficie = self.fuente.render(self.cadena, True, self.color)

    def CambiarPosicion(self, posicion):
        self.posicion = posicion

    def ObtenerDimensiones(self):
        return self.superficie.get_size()
    
    def CentrarTexto(self):
        self.texto_centrado_horizontal, self.texto_centrado_vertical = True

    def CentrarTextoVerticalmente(self):
        self.texto_centrado_vertical = True

    def CentrarTextoHorizontalmente(self):
        self.texto_centrado_horizontal = True

    def Dibujar(self, ventana):
        ancho_ventana, alto_ventana = ventana.get_size()
        ancho_texto, alto_texto = self.superficie.get_size()
        x = self.posicion[0]
        y = self.posicion[1]
        if self.texto_centrado_horizontal:
            x = ((ancho_ventana / 2 ) - (ancho_texto / 2))
        if self.texto_centrado_vertical:
            y = ((alto_ventana / 2) - (alto_texto / 2))
        ventana.blit(self.superficie, (x, y))
