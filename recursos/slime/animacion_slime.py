import pygame
from funcionalidades_generales import *

lista_movimiento_slime_izq = [
    pygame.image.load(f"recursos/slime/red/0.png"),
    pygame.image.load(f"recursos/slime/red/1.png"),
    pygame.image.load(f"recursos/slime/red/2.png"),
    pygame.image.load(f"recursos/slime/red/3.png"),
    pygame.image.load(f"recursos/slime/red/4.png"),
    pygame.image.load(f"recursos/slime/red/5.png")
]

lista_movimiento_slime_der = dar_vuelta_lista(lista_movimiento_slime_izq, True, False)


lista_animaciones_slime = [lista_movimiento_slime_izq, lista_movimiento_slime_der]