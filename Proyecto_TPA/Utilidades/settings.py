ALTO = 960
ANCHO = 1280
TILESIDE = 64
FPS = 60

TABLERO =[['e','e','x','d1','s','d2','d3','e','e'],
          ['e','e','x','d1','s','d2','d3','e','e'],
          ['z2','z3',' ',' ',' ',' ',' ','x','x'],
          ['x','x',' ',' ',' ',' ',' ','j1','j1'],
          ['s','s',' ',' ',' ',' ',' ','s','s'],
          ['z2','z2',' ',' ',' ',' ',' ','j2','j2'],
          ['z1','z1',' ',' ',' ',' ',' ','x','x'],
          ['e','e','n3','x','s','n2','n1','e','e'],
          ['e','e','n3','x','s','n2','n1','e','e']
          ]

#Colores

MONO = (205,230,208)
COLOR_1 = (50,50,200)
ROJO = (255,0,0)
BLANCO = (255, 255, 255)

#TEXTOS

texto_reglas = """
Reglas del juego de Copiopoly\n

Preparación del juego:\n
-Se distribuyen cierta cantidad de dinero a cada jugador.\n


Turno de juego:\n
-Los jugadores lanzan los dados y mueven sus fichas un número de casillas indicado por los dados.\n
-Dependiendo de la casilla en la que aterricen, los jugadores pueden comprar una propiedad, pagar alquiler, etc.\n

Comprar propiedades:\n
-Si un jugador aterriza en una propiedad no poseída, puede comprarla pagando el precio indicado.\n

Fin del juego:\n
-El juego puede acabar si un jugador llega a cierta cantidad de dinero.\n
-El juego puede acabar si la Banca se queda sin dinero y el jugador con mas dinero y propiedades gana.\n
"""
texto_provisorio = """Este es el lugar donde aparecera la\ninformacon de la Banca\n
Este es el lugar donde aparecera la\ninformacon de la Banca\n
Este es el lugar donde aparecera la\ninformacon de la Banca"""
texto_noxus = "Noxuz"
texto_demacia = "Demacia"
texto_jonia = "Jonia"
texto_zaund = "Zaun"