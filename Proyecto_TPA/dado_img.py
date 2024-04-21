import pygame as pg

class Dado():

    def __init__(self, imagen):
        self.imagen = pg.image.load(imagen)
        self.pocicion_relativa = pg.math.Vector2(80, 840)
        self.rect = pg.Rect(self.pocicion_relativa[0], self.pocicion_relativa[1], 64, 64)

    def dibujar(self, screen):
        screen.blit(self.imagen, self.rect)