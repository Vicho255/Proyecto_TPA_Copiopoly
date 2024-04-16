import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir algunas constantes
WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 60

# Crear la ventana
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monopoly")

# Definir la clase Tile para representar las casillas del tablero
class Tile:
    def __init__(self, color, rect, name):
        self.color = color
        self.rect = rect
        self.name = name

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

# Definir la clase Player para representar al jugador
class Player:
    def __init__(self, color, tile):
        self.color = color
        self.tile = tile

    def move(self, steps):
        # Lógica para mover al jugador
        current_index = tiles.index(self.tile)
        new_index = (current_index + steps) % len(tiles)
        self.tile = tiles[new_index]

    def draw(self):
        pygame.draw.circle(window, self.color, self.tile.rect.center, 20)

# Crear una lista de casillas del tablero
tiles = []
tile_width = WIDTH // 10
tile_height = HEIGHT // 10
for i in range(10):
    for j in range(10):
        if i % 2 == 0:
            if j % 2 == 0:
                color = WHITE
            else:
                color = BLACK
        else:
            if j % 2 == 0:
                color = BLACK
            else:
                color = WHITE
        rect = pygame.Rect(j * tile_width, i * tile_height, tile_width, tile_height)
        name = f"Tile {i * 10 + j + 1}"
        tiles.append(Tile(color, rect, name))

# Crear una instancia del jugador
player = Player(RED, tiles[0])

# Función para lanzar el dado
def roll_dice():
    return random.randint(1, 6)

# Game Loop
clock = pygame.time.Clock()
running = True
while running:
    window.fill(BLUE)

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                steps = roll_dice()
                player.move(steps)

    # Dibujar las casillas del tablero
    for tile in tiles:
        tile.draw()

    # Dibujar al jugador
    player.draw()

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(FPS)

# Salir de Pygame
pygame.quit()
sys.exit()