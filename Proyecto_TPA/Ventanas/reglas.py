import pygame as pg
import sys
from Utilidades.settings import *

class Reglas():

    def __init__(self, pantalla, administrador):
        
        self.pantalla = pantalla
        self.admin = administrador

    def iniciar(self):
        self.pantalla.fill("blue")