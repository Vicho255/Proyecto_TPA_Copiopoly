import pygame as pg

class Casilla(pg.sprite.Sprite):

    def __init__(self, pos, groups):

        super().__init__(groups)

        self.image = pg.image.load('Graficos\casilla.png')
        self.rect = self.image.get_rect(topleft = pos)

class Casilla_especial(pg.sprite.Sprite):

    def __init__(self, pos, groups):

        super().__init__(groups)

        self.image = pg.image.load('Graficos\Casilla_especial.png')
        self.rect = self.image.get_rect(topleft = pos)

class Casilla_Suerte(Casilla):
    
    def __init__(self, pos, groups):
        super().__init__(pos, groups)

        self.image = pg.image.load('Graficos/Casilla_Suerte.png')

class Casilla_Noxxuz(Casilla):

    def __init__(self, pos, groups):
        super().__init__(pos, groups)

        self.image = pg.image.load("Graficos/Casilla_Noxus.png")

class Casilla_Demacia(Casilla):

    def __init__(self, pos, groups):
        super().__init__(pos, groups)

        self.image = pg.image.load("Graficos/Casilla_Demacia.png")

class Casilla_Jonia(Casilla):

    def __init__(self, pos, groups):
        super().__init__(pos, groups)

        self.image = pg.image.load("Graficos/Casilla_Jonia.png")

class Casilla_Zaun(Casilla):

    def __init__(self, pos, groups):
        super().__init__(pos, groups)

        self.image = pg.image.load("Graficos/Casilla_Zaund.png")