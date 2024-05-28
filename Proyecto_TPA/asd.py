        while True:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit

                if en_menu:
                    if event.type == pg.MOUSEBUTTONDOWN:

                        if self.iniciar_b.rect.collidepoint(event.pos):
                            en_menu = False
                            self.mostrar_r = False

                        elif self.reglas_b.rect.collidepoint(event.pos):
                            self.mostra_pantalla_tex = True
                            en_menu = False

                        elif self.salir_b.rect.collidepoint(event.pos):
                            pg.quit()
                            sys.exit()
                else:
                    if self.mostra_pantalla_tex:

                        if event.type == pg.KEYDOWN:
                            
                            if event.key == pg.K_ESCAPE:
                                self.mostra_pantalla_tex = False
                                en_menu = True

                    elif self.mostra_pantalla_tex == False:

                        if event.type == pg.MOUSEBUTTONDOWN:
                            
                            if self.regresar_b.rect.collidepoint(event.pos):
                                en_menu = True

                        elif event.type == pg.KEYDOWN:

                            if event.key == pg.K_ESCAPE:
                                self.mostrar_r = True

                            elif event.key == pg.K_SPACE:
                                pos_ficha = self.tablero.pos_ficha()
                                print(pos_ficha)
                                resultado_dado = dado_fun()
                                self.dado.dibujar(self.screen)
                                self.dado.cambiar_imagen(resultado_dado, self.screen)
                                print(resultado_dado)

                                self.tablero.mover_ficha(resultado_dado)
            
            if en_menu:
                self.mostrar_menu()

            else:

                if self.mostra_pantalla_tex:
                    self.reglas.mostrar_texto(texto_reglas)

                elif not self.mostra_pantalla_tex:
                    self.jugar()
                    self.tablero.inicia()
                    self.tablero.div_ficha(self.screen)

            pg.display.update()
            self.clock.tick(FPS)
    
    def mostrar_menu(self):
        self.screen.fill(MONO)
        self.iniciar_b.actualizar(self.screen)
        self.salir_b.actualizar(self.screen)
        self.reglas_b.actualizar(self.screen)

    def jugar(self):
        self.screen.fill(MONO)
        self.tablero.run()
        self.dado.dibujar(self.screen)
        if self.mostrar_r:
            overlay = pg.Surface((ANCHO,ALTO), pg.SRCALPHA)
            overlay.fill((0, 0, 0, 100))
            self.screen.blit(overlay, (0, 0))

            self.regresar_b.actualizar(self.screen)


        self.iniciar_b = Boton(COLOR_1,ANCHO//2 - 100, 200, 200, 50, "Iniciar")
        self.salir_b = Boton(COLOR_1,ANCHO//2 - 100, 500, 200, 50, "Salir")
        self.regresar_b = Boton(COLOR_1,ANCHO//2 - 100, 400, 200, 50, "Regresar")
        self.reglas_b = Boton(COLOR_1,ANCHO//2 - 100, 300, 200, 50, "Reglas")



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