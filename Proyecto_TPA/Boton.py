import pygame as pg

class Boton(pg.sprite.Sprite):
    def __init__(self, color, x, y, ancho, alto, texto):
        super().__init__()

        self.image = pg.Surface((ancho, alto))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.font = pg.font.Font(None, 36)
        self.text = self.font.render(texto, True, "white")
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def actualizar(self, pantalla):
        pantalla.blit(self.image, self.rect)
        pantalla.blit(self.text, self.text_rect)