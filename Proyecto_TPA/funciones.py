import random as rd
import pygame as pg

def dado_fun():
    """
    Genera un numero aleatorio entre el 1 y el 6
    """

    i = rd.randint(1,6)

    return i


salida = 1
impuesto = 2
propiedad = 'asd'

da = dado_fun()