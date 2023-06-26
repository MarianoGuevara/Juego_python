import pygame
from funcionalidades_generales import *


lista_quieto_derecha_boss = [
    pygame.image.load(f"recursos/boss_final/camina/0.png"),
    pygame.image.load(f"recursos/boss_final/camina/1.png")
]


lista_quieto_izquierda_boss = dar_vuelta_lista(lista_quieto_derecha_boss, True, False)


lista_caminar_derecha_boss = [
    pygame.image.load(f"recursos/boss_final/camina/0.png"),
    pygame.image.load(f"recursos/boss_final/camina/1.png"),
    pygame.image.load(f"recursos/boss_final/camina/2.png"),
    pygame.image.load(f"recursos/boss_final/camina/3.png")
]


lista_caminar_izquierda_boss = dar_vuelta_lista(lista_caminar_derecha_boss, True, False)


lista_salto_derecha_boss = [
    pygame.image.load(f"recursos/boss_final/salta/0.png")
]


lista_salto_izquierda_boss = dar_vuelta_lista(lista_salto_derecha_boss, True, False)


lista_daño_derecha_boss = [
    pygame.image.load(f"recursos/boss_final/daño/0.png"),
    pygame.image.load(f"recursos/boss_final/daño/1.png")
]


lista_animaciones_boss_final = [
    lista_quieto_derecha_boss,
    lista_quieto_izquierda_boss,
    lista_caminar_derecha_boss, 
    lista_caminar_izquierda_boss,
    lista_salto_derecha_boss,
    lista_salto_izquierda_boss,

    lista_daño_derecha_boss
]



lista_bola_img_der_boss = [
    pygame.image.load(f"recursos/boss_final/bola/0.png"),
    pygame.image.load(f"recursos/boss_final/bola/1.png"),
    pygame.image.load(f"recursos/boss_final/bola/2.png"),
    pygame.image.load(f"recursos/boss_final/bola/3.png"),
    pygame.image.load(f"recursos/boss_final/bola/4.png")
]


lista_bola_img_izq_boss = dar_vuelta_lista(lista_bola_img_der_boss, True, False)


lista_bola_choque_boss = [
    pygame.image.load(f"recursos/boss_final/bola/choque/hits-3-1.png"),
    pygame.image.load(f"recursos/boss_final/bola/choque/hits-3-2.png"),
    pygame.image.load(f"recursos/boss_final/bola/choque/hits-3-3.png"),
    pygame.image.load(f"recursos/boss_final/bola/choque/hits-3-4.png"),
    pygame.image.load(f"recursos/boss_final/bola/choque/hits-3-5.png")
]


lista_animaciones_bola_boss = [lista_bola_img_der_boss, lista_bola_img_izq_boss, lista_bola_choque_boss]