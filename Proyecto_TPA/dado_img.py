import pygame as pg

class Dado():

    def __init__(self, imagen):
        self.imagen = pg.image.load(imagen)
        self.pocicion_relativa = pg.math.Vector2(80, 840)
        self.rect = pg.Rect(self.pocicion_relativa[0], self.pocicion_relativa[1], 64, 64)
        self.imagen_rect = self.imagen.get_rect(topleft=(self.pocicion_relativa[0],self.pocicion_relativa[1]))

    def dibujar(self, screen):
        screen.blit(self.imagen, self.rect)
    
    def set_imagen(self, imagen):
        self.imagen = pg.image.load(imagen)

    def cambiar_imagen(self, resultado_dado, screen):
        if 0 < resultado_dado < 7: 
            self.set_imagen(f"d:\Proyecto_TPA\Graficos\Dado\Dado_{resultado_dado}.png")
            self.dibujar(screen)