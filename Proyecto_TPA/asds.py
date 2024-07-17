import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configurar la pantalla
ancho_pantalla, alto_pantalla = 800, 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Juego con Menú de Opciones")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)
NARANJA = (255, 165, 0)

# Fuentes
fuente = pygame.font.Font(None, 36)

# Botón para abrir el menú de opciones
boton_menu = pygame.Rect(650, 500, 100, 50)

# Sliders del menú de opciones
slider_sfx = pygame.Rect(300, 150, 200, 20)
slider_music = pygame.Rect(300, 250, 200, 20)
slider_handle_sfx = pygame.Rect(slider_sfx.x, slider_sfx.y - 10, 20, 40)
slider_handle_music = pygame.Rect(slider_music.x, slider_music.y - 10, 20, 40)

# Botón de vibración
boton_vibration = pygame.Rect(300, 350, 100, 50)
vibration_on = True

# Menú desplegable para resolución
resoluciones = [(800, 600), (1024, 768), (1280, 720)]
indice_resolucion = 0
desplegable_abierto = False
opciones_resolucion_rects = [pygame.Rect(300, 450 + i * 40, 200, 40) for i in range(len(resoluciones))]

# Estado del menú
mostrar_menu = False

# Bucle principal del juego
corriendo = True
arrastrando_sfx = False
arrastrando_music = False
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if mostrar_menu:
                if slider_handle_sfx.collidepoint(evento.pos):
                    arrastrando_sfx = True
                if slider_handle_music.collidepoint(evento.pos):
                    arrastrando_music = True
                if boton_vibration.collidepoint(evento.pos):
                    vibration_on = not vibration_on
                if opciones_resolucion_rects[0].collidepoint(evento.pos):
                    desplegable_abierto = not desplegable_abierto
                if desplegable_abierto:
                    for i, rect in enumerate(opciones_resolucion_rects):
                        if rect.collidepoint(evento.pos):
                            indice_resolucion = i
                            ancho_pantalla, alto_pantalla = resoluciones[i]
                            pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
                            desplegable_abierto = False
                if boton_menu.collidepoint(evento.pos):
                    mostrar_menu = False  # Cierra el menú
            else:
                if boton_menu.collidepoint(evento.pos):
                    mostrar_menu = True  # Abre el menú

        if evento.type == pygame.MOUSEBUTTONUP:
            arrastrando_sfx = False
            arrastrando_music = False
        if evento.type == pygame.MOUSEMOTION:
            if arrastrando_sfx:
                slider_handle_sfx.x = max(slider_sfx.x, min(evento.pos[0], slider_sfx.x + slider_sfx.width - slider_handle_sfx.width))
            if arrastrando_music:
                slider_handle_music.x = max(slider_music.x, min(evento.pos[0], slider_music.x + slider_music.width - slider_handle_music.width))

    # Dibujar la pantalla principal
    pantalla.fill(BLANCO)
    titulo_principal = fuente.render("Pantalla Principal", True, NEGRO)
    pantalla.blit(titulo_principal, (ancho_pantalla // 2 - titulo_principal.get_width() // 2, 50))

    # Botón para abrir el menú de opciones
    pygame.draw.rect(pantalla, GRIS, boton_menu)
    texto_boton_menu = fuente.render("Opciones", True, NEGRO)
    pantalla.blit(texto_boton_menu, (boton_menu.x + 10, boton_menu.y + 10))

    # Dibujar el menú de opciones si está activo
    if mostrar_menu:
        # Fondo del menú
        menu_rect = pygame.Rect(150, 100, 500, 400)
        pygame.draw.rect(pantalla, NARANJA, menu_rect)

        # Título del menú
        titulo_menu = fuente.render("Opciones", True, NEGRO)
        pantalla.blit(titulo_menu, (menu_rect.x + 200, menu_rect.y + 20))

        # Slider SFX
        pygame.draw.rect(pantalla, GRIS, slider_sfx)
        pygame.draw.rect(pantalla, NARANJA, slider_handle_sfx)
        texto_sfx = fuente.render("SFX", True, NEGRO)
        pantalla.blit(texto_sfx, (200, slider_sfx.y))

        # Slider Music
        pygame.draw.rect(pantalla, GRIS, slider_music)
        pygame.draw.rect(pantalla, NARANJA, slider_handle_music)
        texto_music = fuente.render("Música", True, NEGRO)
        pantalla.blit(texto_music, (200, slider_music.y))

        # Botón Vibration
        pygame.draw.rect(pantalla, GRIS, boton_vibration)
        texto_vibration = fuente.render("Vibración", True, NEGRO)
        pantalla.blit(texto_vibration, (200, boton_vibration.y + 10))
        estado_vibration = fuente.render("On" if vibration_on else "Off", True, NEGRO)
        pantalla.blit(estado_vibration, (boton_vibration.x + 30, boton_vibration.y + 10))

        # Menú desplegable para resolución
        pygame.draw.rect(pantalla, GRIS, opciones_resolucion_rects[0])
        texto_resolucion = fuente.render(f"Resolución: {resoluciones[indice_resolucion][0]}x{resoluciones[indice_resolucion][1]}", True, NEGRO)
        pantalla.blit(texto_resolucion, (opciones_resolucion_rects[0].x + 10, opciones_resolucion_rects[0].y + 5))

        if desplegable_abierto:
            for i, rect in enumerate(opciones_resolucion_rects):
                if i > 0:
                    pygame.draw.rect(pantalla, GRIS, rect)
                    texto_opcion = fuente.render(f"{resoluciones[i][0]}x{resoluciones[i][1]}", True, NEGRO)
                    pantalla.blit(texto_opcion, (rect.x + 10, rect.y + 5))

        # Botón para cerrar el menú
        pygame.draw.rect(pantalla, GRIS, boton_menu)
        texto_cerrar_menu = fuente.render("Cerrar", True, NEGRO)
        pantalla.blit(texto_cerrar_menu, (boton_menu.x + 10, boton_menu.y + 10))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
