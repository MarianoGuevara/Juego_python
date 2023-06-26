import pygame
from funcionalidades_generales import *

lista_movimiento_trampa_fuego_der = [
    pygame.image.load(f"recursos/trampas/trampa_horizontal/0.png"),
    pygame.image.load(f"recursos/trampas/trampa_horizontal/1.png"),
    pygame.image.load(f"recursos/trampas/trampa_horizontal/2.png"),
    pygame.image.load(f"recursos/trampas/trampa_horizontal/3.png")
]

lista_movimiento_trampa_fuego_izq = dar_vuelta_lista(lista_movimiento_trampa_fuego_der, True, False)

lista_animaciones_trampa_fuego = [lista_movimiento_trampa_fuego_der, 
                                lista_movimiento_trampa_fuego_izq]