import pygame as pg

class Ficha(pg.sprite.Sprite):

    def __init__(self,nombre,imagen,x,y,visible = False):
        super().__init__()
        self.nombre = nombre
        self.imagen = pg.image.load(imagen)
        self.visible = visible
        self.posicion_relativa = pg.math.Vector2(x,y)
        self.rect = pg.Rect(self.posicion_relativa[0],self.posicion_relativa[1],32,32)
        self.imagen_rect = self.imagen.get_rect(topleft=(self.posicion_relativa[0],self.posicion_relativa[1]))

    def dibujar(self,screen):
        self.rect = pg.Rect(self.posicion_relativa[0],self.posicion_relativa[1],32,32)
        if self.visible:
            screen.blit(self.imagen, self.rect)

    def mov_left(self):
        self.posicion_relativa.x -= 64
        self.rect.x = self.posicion_relativa.x
        print(f"Movimiento izquierda: {self.posicion_relativa}")

    def mov_right(self):
        self.posicion_relativa.x += 64
        self.rect.x = self.posicion_relativa.x
        print(f"Movimiento derecha: {self.posicion_relativa}")

    def mov_top(self):
        self.posicion_relativa.y -= 64
        self.rect.y = self.posicion_relativa.y
        print(f"Movimiento arriba: {self.posicion_relativa}")

    def mov_bottom(self):
        self.posicion_relativa.y += 64
        self.rect.y = self.posicion_relativa.y
        print(f"Movimiento abajo: {self.posicion_relativa}")