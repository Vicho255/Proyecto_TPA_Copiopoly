import pygame as pg
import sys
from settings import *

class Reglas():

    def __init__(self, screen):
        
        self.screen = screen
        self.font = pg.font.Font(None, 36)
        self.color_del_texto = (0,0,50) #RGB
        self.color_fondo  = MONO

    def mostrar_texto(self,texto):

        self.screen.fill(self.color_fondo)
        superficie_texto  = self.font.render(texto, True, self.color_del_texto)
        rect_texto = superficie_texto.get_rect(center = self.screen.get_rect().center)
        self.screen.blit(superficie_texto, rect_texto)

    
    