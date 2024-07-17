import pygame as pg

class Casilla(pg.sprite.Sprite):

    def __init__(self, pos,groups,imagen):

        super().__init__(groups)

        self.image = pg.image.load(imagen)
        self.rect = self.image.get_rect(topleft = pos)