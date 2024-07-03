import pygame as pg
import json
import sys
from Utilidades.settings import *
from tablero import Tablero
from Utilidades.dado_img import Dado
from Utilidades.Boton import Boton
from Utilidades.Superficie import Superficie
from Utilidades.Texto import Texto
from entidades import *

with open('Utilidades/Textos/Textos_Casillas.json', 'r') as archivo:
    textos = json.load(archivo)
print(textos)


class Juego():

    def __init__(self, pantalla, administrador):
        pg.init()
        self.pantalla = pantalla
        self.admin = administrador

        self.tablero = Tablero()
        self.dado = Dado(imagen= "d:\Proyecto_TPA\Graficos\Dado\Dado_1.png")
        self.botonRegresar = Boton('Regresar', 40, (200, 50), posicion= (ANCHO//2 - 100, 400), metodo= self.cambiarEtapa, argumento= 'menu', texto_centrado= True)
        self.botonCambioBanca = Boton("Banca", 35, (150,45), posicion= (736,96),color = (0,100,200,255), color_colision='blue',metodo= self.volverBanca,texto_centrado= True)
        self.botonComprar = Boton("Comprar", 35, (150,45), posicion= (750,580),color = (0,200,100,255),color_colision='green')
        self.botonRechazar = Boton("Rechazar", 35, (150,45), posicion= (1020,580),color = (200,0,0,255), metodo= self.rechazado)

        self.teclas_presionado_espacio = False
        self.teclas_presionado_escape = False

        self.info = Superficie(dimensiones=(448, 512), posicion= (736, 128), color=(200, 255, 200, 255))

        self.texto_banca = Texto(dimension_fuente= 30, cadena= "Banca", posicion= (935, 138), color=(0, 0, 0))
        self.info_Banca = Texto(dimension_fuente= 30, cadena= texto_provisorio, posicion= (746,160), color=(0, 0, 0))
        self.texto_casilla = Texto(dimension_fuente= 30, cadena= "Casilla", posicion= (900, 138), color=(0, 0, 0))
        self.info_Casilla = Texto(dimension_fuente= 30, cadena= texto_provisorio, posicion= (746,160), color=(0, 0, 0))
        self.texto_Compra = Texto(dimension_fuente= 30, cadena= "!COMPRA REALIZADA CON EXITO¡", posicion= (746,640), color=(0, 0, 0))
        self.texto_Rechazo = Texto(dimension_fuente= 30, cadena= "!COMPRA RECHAZADA¡", posicion= (746,640), color=(0, 0, 0))

        self.mostrar_boton = False
        self.mostrar_Tex_Banca = True
        self.mostrar_Tex_Casilla = False
        self.mostrar_compra = False
        self.mostrar_rechazo = False

    def iniciar(self):
        #print(pg.mouse.get_pos())
        #print(self.mostrar_boton)
        self.pantalla.fill(MONO)
        self.tablero.run()
        self.dado.dibujar(self.pantalla)
        self.tablero.div_ficha(self.pantalla)
        self.dado.dibujar(self.pantalla)
        self.info.Dibujar(self.pantalla)
        self.botonCambioBanca.Dibujar(self.pantalla)

        if self.mostrar_Tex_Banca:
            self.mostrar_Tex_Casilla = False
            self.texto_banca.Dibujar(self.pantalla)
            self.info_Banca.Dibujar(self.pantalla)
            self.botonCambioBanca.CambiarColor((100,100,200,255))
        elif self.mostrar_Tex_Casilla:
            self.mostrar_Tex_Banca = False
            self.texto_casilla.Dibujar(self.pantalla)
            self.info_Casilla.Dibujar(self.pantalla)
            self.botonComprar.Dibujar(self.pantalla)
            self.botonRechazar.Dibujar(self.pantalla)
            

        teclas = pg.key.get_pressed()


        if teclas[pg.K_SPACE] and not self.teclas_presionado_espacio:
            self.teclas_presionado_espacio = True
            resultado = self.dado.lanzar()
            self.dado.cambiar_imagen(resultado, self.pantalla)
            self.tablero.mover_ficha(resultado_dado= resultado)
            print(resultado)

        elif not teclas[pg.K_SPACE]:
            self.teclas_presionado_espacio = False

        if teclas[pg.K_ESCAPE]:
            if not self.teclas_presionado_escape:
                if not self.mostrar_boton:
                    self.mostrar_boton = True
                else:
                    self.mostrar_boton = False
            self.teclas_presionado_escape = True
        else:
            self.teclas_presionado_escape = False
        
        if self.mostrar_boton:
            self.botonRegresar.Dibujar(self.pantalla)
        
        self.posicion_tablero()

        if self.mostrar_compra and self.botonComprar.colision:
            self.texto_Compra.Dibujar(self.pantalla)
        elif self.mostrar_rechazo and self.botonRechazar.colision:
            self.texto_Rechazo.Dibujar(self.pantalla)
        elif not self.mostrar_compra and not self.mostrar_rechazo:
            pass

    def resetear(self):
        self.mostrar_boton = False

    def posicion_tablero(self):
        for linea_index,linea in enumerate(TABLERO):
            for col_index, colum in enumerate(linea):
                x = col_index * TILESIDE
                y = linea_index  * TILESIDE

                ficha = self.tablero.turnoSiguiente()[0]

                if self.tablero.pos_ficha(ficha) == (x+80,y+80) and colum == "n1":
                    self.texto_casilla.CambiarCadena(textos["Noxus"]["Noxus_1"]["Nombre"])
                    self.info_Casilla.CambiarCadena(textos["Noxus"]["Noxus_1"]["Descripcion"])
                    self.mostrar_Tex_Casilla = True
                    self.mostrar_Tex_Banca = False
                elif self.tablero.pos_ficha(ficha) == (x+80,y+80) and colum == "n2":
                    self.texto_casilla.CambiarCadena(textos["Noxus"]["Noxus_2"]["Nombre"])
                    self.info_Casilla.CambiarCadena(textos["Noxus"]["Noxus_2"]["Descripcion"])
                    self.mostrar_Tex_Casilla = True
                    self.mostrar_Tex_Banca = False
                elif self.tablero.pos_ficha(ficha) == (x+80,y+80) and colum == "n3":
                    self.texto_casilla.CambiarCadena(textos["Noxus"]["Noxus_3"]["Nombre"])
                    self.info_Casilla.CambiarCadena(textos["Noxus"]["Noxus_3"]["Descripcion"])
                    self.mostrar_Tex_Casilla = True
                    self.mostrar_Tex_Banca = False
                elif self.tablero.pos_ficha(ficha) == (x+80, y+80) and colum == "d":
                    self.texto_casilla.CambiarCadena(texto_demacia)
                    self.info_Casilla.CambiarCadena(texto_demacia)
                    self.mostrar_Tex_Casilla = True
                    self.mostrar_Tex_Banca = False
                elif self.tablero.pos_ficha(ficha) == (x+80, y+80) and colum == "j":
                    self.texto_casilla.CambiarCadena(texto_jonia)
                    self.info_Casilla.CambiarCadena(texto_jonia)
                    self.mostrar_Tex_Casilla = True
                    self.mostrar_Tex_Banca = False
                elif self.tablero.pos_ficha(ficha) == (x+80, y+80) and colum == "z":
                    self.texto_casilla.CambiarCadena(texto_zaund)
                    self.info_Casilla.CambiarCadena(texto_zaund)
                    self.mostrar_Tex_Casilla = True
                    self.mostrar_Tex_Banca = False

    def volverBanca(self):
        self.mostrar_Tex_Casilla = False
        self.mostrar_Tex_Banca = True

    def cambiarEtapa(self, etapa):
        self.admin.set_etapa(etapa)

    def comprado(self, jugador):
        propiedad = self.posicion_tablero()
        j = self.tablero.jugadores[jugador.nombre]
        b = self.tablero.banco
        j.adquirir_propiedad(propiedad)
        b.set_propiedades(propiedad)

        self.mostrar_compra = True

    def rechazado(self):
        self.mostrar_compra = False
        self.mostrar_rechazo = True

class Ficha():

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

    def mov_rigth(self):
        vector_derecha = pg.math.Vector2(64, 0)
        self.posicion_relativa += vector_derecha