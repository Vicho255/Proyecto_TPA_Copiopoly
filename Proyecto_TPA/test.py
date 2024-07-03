import random as rd

def dado():
    """
    Genera un numero aleatorio entre el 1 y el 6
    """

    i = rd.randint(1,6)

    return i



while dado() != 0:
    print(dado(),"\n loco")


    def posicion_tablero(self):
        for linea_index,linea in enumerate(TABLERO):
            for col_index, colum in enumerate(linea):
                x = col_index * TILESIDE
                y = linea_index  * TILESIDE

                ficha = self.turnoSiguiente()[0]

                if self.pos_ficha(ficha) == (x+80,y+80) and colum == "n1":
                    self.texto_casilla.CambiarCadena(textos["Noxus"]["Noxus_1"]["Nombre"])
                    self.info_Casilla.CambiarCadena(textos["Noxus"]["Noxus_1"]["Descripcion"])
                    self.mostrar_Tex_Casilla = True
                    self.mostrar_Tex_Banca = False
                elif self.pos_ficha(ficha) == (x+80,y+80) and colum == "n2":
                    self.texto_casilla.CambiarCadena(textos["Noxus"]["Noxus_2"]["Nombre"])
                    self.info_Casilla.CambiarCadena(textos["Noxus"]["Noxus_2"]["Descripcion"])
                    self.mostrar_Tex_Casilla = True
                    self.mostrar_Tex_Banca = False
                elif self.pos_ficha(ficha) == (x+80,y+80) and colum == "n3":
                    self.texto_casilla.CambiarCadena(textos["Noxus"]["Noxus_3"]["Nombre"])
                    self.info_Casilla.CambiarCadena(textos["Noxus"]["Noxus_3"]["Descripcion"])
                    self.mostrar_Tex_Casilla = True
                    self.mostrar_Tex_Banca = False
                elif self.pos_ficha(ficha) == (x+80, y+80) and colum == "d":
                    self.texto_casilla.CambiarCadena("Demacia")
                    self.info_Casilla.CambiarCadena("Demacia")
                    self.mostrar_Tex_Casilla = True
                    self.mostrar_Tex_Banca = False
                elif self.pos_ficha(ficha) == (x+80, y+80) and colum == "j":
                    self.texto_casilla.CambiarCadena("Jonia")
                    self.info_Casilla.CambiarCadena("Jonia")
                    self.mostrar_Tex_Casilla = True
                    self.mostrar_Tex_Banca = False
                elif self.pos_ficha(ficha) == (x+80, y+80) and colum == "z":
                    self.texto_casilla.CambiarCadena("Zaun")
                    self.info_Casilla.CambiarCadena("Zaun")
                    self.mostrar_Tex_Casilla = True
                    self.mostrar_Tex_Banca = False



class Tablero():

    def __init__(self):

        self.mostrar_superficie = pg.display.get_surface()
        self.sprits_visibles = pg.sprite.Group()
        self.sprits_visibles2 = pg.sprite.Group()
        self.fichas = pg.sprite.Group()

        self.inicializar_fichas()
        self.turno = IterarTurno(self.fichas.sprites())
        self.jugador1 = Jugador("J1","Ficha Roja")
        self.jugador2 = Jugador("J2","Ficha Verde")
        self.jugador3 = Jugador("J3","Ficha Azul")
        self.jugador4 = Jugador("J4","Ficha Amarilla")
        self.jugadores = [self.jugador1, self.jugador2, self.jugador3, self.jugador4]
        self.turnoj = IterarTurno(self.jugadores)

        self.fichas_por_casilla = {}        


        self.banco = Banca()

        self.crear_tablero()

    def inicializar_fichas(self):
        ficha1 = Ficha("Ficha Roja","d:\Proyecto_TPA\Graficos\Ficha_Roja.png",592,592,visible=False)
        ficha2 = Ficha("Ficha Verde","d:\Proyecto_TPA\Graficos\Ficha_Verde.png",528,592,visible=False)
        ficha3 = Ficha("Ficha Azul","d:\Proyecto_TPA\Graficos\Ficha_Azul.png",592,528,visible=False)
        ficha4 = Ficha("Ficha Amarilla","d:\Proyecto_TPA\Graficos\Ficha_Amarilla.png",528,528,visible=False)

        self.fichas.add(ficha1, ficha2, ficha3, ficha4)



    def crear_tablero(self):

        for linea_index,linea in enumerate(TABLERO):
            i = 0
            i = i+1

            print(f"Fila {i}")
            for col_index, colum in enumerate(linea):
                x = col_index * TILESIDE
                y = linea_index  * TILESIDE

                if colum == 'x':
                    Casilla((x+64,y+64),self.sprits_visibles)
                elif colum == 'e':
                    Casilla_especial((x+64,y+64),self.sprits_visibles)
                    print(x+64, y+64, "Casilla E")
                elif colum == 'n1' or colum == 'n2' or colum == 'n3':
                    Casilla_Noxxuz((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla N")
                elif colum == 'd1'or colum == 'd2' or colum == 'd3':
                    Casilla_Demacia((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla D")
                elif colum == 'z1'or colum == 'z2' or colum == 'z3':
                    Casilla_Zaun((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla Z")
                elif colum == 'j1'or colum == 'j2':
                    Casilla_Jonia((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla J")
                elif colum == 's':
                    Casilla_Suerte((x+64, y+64), self.sprits_visibles)
                    print(x+64, y+64, "Casilla S")
    
    def div_ficha(self, screen):
        for ficha in self.fichas:
            self.mostrar_superficie.blit(ficha.imagen, ficha.rect)
                
    def mover_ficha(self, resultado_dado):
        ficha, jugador = self.turnoSiguiente()

        pos_anterior = self.pos_ficha(ficha)
        print(f"Posición inicial de {ficha.nombre}: {pos_anterior}")

        if pos_anterior in self.fichas_por_casilla and ficha in self.fichas_por_casilla[pos_anterior]:
            self.fichas_por_casilla[pos_anterior].remove(ficha)
            if not self.fichas_por_casilla[pos_anterior]:
                del self.fichas_por_casilla[pos_anterior]

        for _ in range(resultado_dado):
            pos_actual = self.pos_ficha(ficha)
            x, y = pos_actual
            mov = 64


            if ((x in [592, 528] and y in [592, 528]) or (80 < x <= 592 and y in [592, 528])):
                # Movimiento hacia la izquierda
                if x - mov > 80:
                    ficha.mov_left()
                else:
                    ficha.posicion_relativa.x = 80
                    ficha.mov_top()

            elif ((x in [80, 144] and y in [592, 528]) or (x in [80, 144] and y in [592, 528])):
                # Movimiento hacia arriba
                if y - mov > 80:
                    ficha.mov_top()
                else:
                    ficha.posicion_relativa.y = 80
                    ficha.mov_right()

            elif (x in [80, 592] and y == 80) or (80 <= x < 592 and y == 80):
                # Movimiento hacia la derecha
                if x + mov < 592:
                    ficha.mov_right()
                else:
                    ficha.posicion_relativa.x = 592
                    ficha.mov_bottom()

            elif (x == 592 and 80 <= y < 592) or (x == 592 and y == 80):
                # Movimiento hacia abajo
                if y + mov < 592:
                    ficha.mov_bottom()
                else:
                    ficha.posicion_relativa.y = 592
                    ficha.mov_left()

            pos_actual = self.pos_ficha(ficha)

        x, y = self.pos_ficha(ficha)
        print(f"Posición final de {ficha.nombre}: ({x}, {y})")

        if pos_actual not in self.fichas_por_casilla:
            self.fichas_por_casilla[pos_actual] = []
        if ficha not in self.fichas_por_casilla[pos_actual]:
            self.fichas_por_casilla[pos_actual].append(ficha)

        casilla_actual = self.obtener_casilla(pos_actual)
        if casilla_actual and casilla_actual["precio"] > 0:
            if jugador.adquirir_propiedad(casilla_actual):
                self.banco.perder_dinero_banca(casilla_actual["precio"])
                print(f"{jugador.nombre} ha comprado {casilla_actual['Nombre']}.")


    def pos_ficha(self,ficha):
        return ficha.rect.x , ficha.rect.y
    
    def obtener_casilla(self, pos):
        x, y = pos
        col_index = (x - 80) // TILESIDE
        linea_index = (y - 80) // TILESIDE
        if 0 <= linea_index < len(TABLERO) and 0 <= col_index < len(TABLERO[linea_index]):
            if TABLERO[linea_index][col_index] == "n1":
                return self.banco.propiedades[0]
            elif TABLERO[linea_index][col_index] == "n2":
                return self.banco.propiedades[1]
            elif TABLERO[linea_index][col_index] == "n3":
                return self.banco.propiedades[2]
            elif TABLERO[linea_index][col_index] == "z1":
                return self.banco.propiedades[3]
            elif TABLERO[linea_index][col_index] == "z2":
                return self.banco.propiedades[4]
            elif TABLERO[linea_index][col_index] == "z3":
                return self.banco.propiedades[5]
            elif TABLERO[linea_index][col_index] == "d1":
                return self.banco.propiedades[6]
            elif TABLERO[linea_index][col_index] == "d2":
                return self.banco.propiedades[7]
            elif TABLERO[linea_index][col_index] == "d3":
                return self.banco.propiedades[8]
            elif TABLERO[linea_index][col_index] == "j1":
                return self.banco.propiedades[9]
            elif TABLERO[linea_index][col_index] == "j2":
                return self.banco.propiedades[10]

        else:
            return None
    
    def turnoSiguiente(self):
        ficha_Siguiente = self.turno.avanzar()
        jugadoS = self.turnoj.avanzar()

        print(ficha_Siguiente.nombre)
        return ficha_Siguiente, jugadoS

    def run(self):

        self.sprits_visibles.draw(self.mostrar_superficie)



with open('Utilidades/Textos/Textos_Casillas.json', 'r') as archivo:
    textos = json.load(archivo)

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
            self.actualizar_info(self.tablero.pos_ficha(self.tablero.turnoSiguiente()[0]))
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
        
        if self.mostrar_compra and self.botonComprar.colision:
            self.texto_Compra.Dibujar(self.pantalla)
        elif self.mostrar_rechazo and self.botonRechazar.colision:
            self.texto_Rechazo.Dibujar(self.pantalla)
        elif not self.mostrar_compra and not self.mostrar_rechazo:
            pass

    def actualizar_info(self, pos):
        colum = self.obternerColumna(pos)

        if colum == "n1":
            self.texto_casilla.CambiarCadena(textos["Noxus"]["Noxus_1"]["Nombre"])
            self.info_Casilla.CambiarCadena(textos["Noxus"]["Noxus_1"]["Descripcion"])
        elif colum == "n2":
            self.texto_casilla.CambiarCadena(textos["Noxus"]["Noxus_2"]["Nombre"])
            self.info_Casilla.CambiarCadena(textos["Noxus"]["Noxus_2"]["Descripcion"])
        elif colum == "n3":
            self.texto_casilla.CambiarCadena(textos["Noxus"]["Noxus_3"]["Nombre"])
            self.info_Casilla.CambiarCadena(textos["Noxus"]["Noxus_3"]["Descripcion"])
        elif colum == "d":
            self.texto_casilla.CambiarCadena(texto_demacia)
            self.info_Casilla.CambiarCadena(texto_demacia)
        elif colum == "j":
            self.texto_casilla.CambiarCadena(texto_jonia)
            self.info_Casilla.CambiarCadena(texto_jonia)
        elif colum == "z":
            self.texto_casilla.CambiarCadena(texto_zaund)
            self.info_Casilla.CambiarCadena(texto_zaund)

        self.mostrar_Tex_Casilla = True
        self.mostrar_Tex_Banca = False

    def obternerColumna(self, pos):
        x, y = pos
        col_index = (x-80)//TILESIDE
        linea_index = (y-80)//TILESIDE
        return TABLERO[linea_index][col_index]

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