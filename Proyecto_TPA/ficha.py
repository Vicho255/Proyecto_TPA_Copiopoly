import pygame as pg

class Ficha(pg.sprite.Sprite):

    def __init__(self,nombre,imagen,x,y,visible = False):
        
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

    def mov_top(self):
        vector_arriba = pg.math.Vector2(0, -64)
        self.posicion_relativa += vector_arriba 

    def mov_bottom(self):
        vector_abajo = pg.math.Vector2(0, 64)
        self.posicion_relativa += vector_abajo

    def mov_left(self):
        vector_izquierda = pg.math.Vector2(-64, 0)
        self.posicion_relativa += vector_izquierda

    def mov_right(self):
        vector_derecha = pg.math.Vector2(64, 0)
        self.posicion_relativa += vector_derecha