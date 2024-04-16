import pygame as pg
from settings import *

class Casilla(pg.sprite.Sprite):

    def __init__(self, pos, groups):

        super().__init__(groups)

        self.image = pg.image.load('d:\Proyecto_TPA\Graficos\casilla.png')
        self.rect = self.image.get_rect(topleft = pos)

class Casilla_especial(pg.sprite.Sprite):

    def __init__(self, pos, groups):

        super().__init__(groups)

        self.image = pg.image.load('d:\Proyecto_TPA\Graficos\Casilla_especial.png')
        self.rect = self.image.get_rect(topleft = pos)


class Casilla_Noxxuz(Casilla):

    def __init__(self, pos, groups):
        super().__init__(pos, groups)

        self.image = pg.image.load("d:\Proyecto_TPA\Graficos\rimworld-piel-432383-5500-1-07-08.png")

class Casilla_Demacia(Casilla):

    def __init__(self, pos, groups):
        super().__init__(pos, groups)

        self.image = pg.image.load("d:\Proyecto_TPA\Graficos\rimworld-piel-432383-5500-1-07-010.png")

class Casilla_Jonia(Casilla):

    def __init__(self, pos, groups):
        super().__init__(pos, groups)

        self.image = pg.image.load("d:\Proyecto_TPA\Graficos\rimworld-piel-432383-5500-1-07-09.png")

class Casilla_Zaun(Casilla):

    def __init__(self, pos, groups):
        super().__init__(pos, groups)

        self.image = pg.image.load("d:\Proyecto_TPA\Graficos\rimworld-piel-432383-5500-1-07-011.png")