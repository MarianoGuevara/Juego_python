import pygame
from funcionalidades_generales import *

lista_movimiento_bat_der = [
    pygame.image.load(f"recursos/bat/imagenes_bat/1.png"),
    pygame.image.load(f"recursos/bat/imagenes_bat/2.png"),
    pygame.image.load(f"recursos/bat/imagenes_bat/3.png"),
    pygame.image.load(f"recursos/bat/imagenes_bat/4.png")
]

lista_movimiento_bat_izq = dar_vuelta_lista(lista_movimiento_bat_der, True, False)


lista_animaciones_bat = [lista_movimiento_bat_der, lista_movimiento_bat_izq]