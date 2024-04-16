import pygame as pg

pg.init()

font = pg.font.Font(None,30)

def debug(info, y = 10, x = 10):
    mostrar_superficie = pg.display.get_surface()
    debug_sup = font.render(str(info),True,'white')
    debug_rect = debug_sup.get_rect(topleft = (x,y))
    pg.draw.rect(mostrar_superficie,'black',debug_rect)
    mostrar_superficie.blit(debug_sup,debug_rect)