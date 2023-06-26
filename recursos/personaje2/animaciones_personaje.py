import pygame
from funcionalidades_generales import *


lista_quieto_derecha = [
    pygame.image.load(f"recursos/personaje2/camina/0.png"),
    pygame.image.load(f"recursos/personaje2/camina/1.png")
]


lista_quieto_izquierda = dar_vuelta_lista(lista_quieto_derecha, True, False)


lista_caminar_derecha = [
    pygame.image.load(f"recursos/personaje2/camina/0.png"),
    pygame.image.load(f"recursos/personaje2/camina/1.png"),
    pygame.image.load(f"recursos/personaje2/camina/2.png"),
    pygame.image.load(f"recursos/personaje2/camina/3.png"),
    pygame.image.load(f"recursos/personaje2/camina/4.png"),
    pygame.image.load(f"recursos/personaje2/camina/5.png"),
    pygame.image.load(f"recursos/personaje2/camina/6.png"),
    pygame.image.load(f"recursos/personaje2/camina/7.png")
]


lista_caminar_izquierda = dar_vuelta_lista(lista_caminar_derecha, True, False)


lista_salto_derecha = [
    pygame.image.load(f"recursos/personaje2/salta/0.png"),
    pygame.image.load(f"recursos/personaje2/salta/1.png"),
    pygame.image.load(f"recursos/personaje2/salta/2.png"),
    pygame.image.load(f"recursos/personaje2/salta/3.png")
]


lista_salto_izquierda = dar_vuelta_lista(lista_salto_derecha, True, False)


lista_animaciones_personaje = [
    lista_quieto_derecha,
    lista_quieto_izquierda,
    lista_caminar_derecha, 
    lista_caminar_izquierda,
    lista_salto_derecha,
    lista_salto_izquierda,
]



lista_bola_img_der = [
    pygame.image.load(f"recursos/personaje2/bola/0.png"),
    pygame.image.load(f"recursos/personaje2/bola/1.png"),
    pygame.image.load(f"recursos/personaje2/bola/2.png"),
    pygame.image.load(f"recursos/personaje2/bola/3.png"),
    pygame.image.load(f"recursos/personaje2/bola/4.png")
]


lista_bola_img_izq = dar_vuelta_lista(lista_bola_img_der, True, False)


lista_bola_choque = [
    pygame.image.load(f"recursos/personaje2/bola/choque/hits-3-1.png"),
    pygame.image.load(f"recursos/personaje2/bola/choque/hits-3-2.png"),
    pygame.image.load(f"recursos/personaje2/bola/choque/hits-3-3.png"),
    pygame.image.load(f"recursos/personaje2/bola/choque/hits-3-4.png"),
    pygame.image.load(f"recursos/personaje2/bola/choque/hits-3-5.png")
]


lista_animaciones_bola = [lista_bola_img_der, lista_bola_img_izq, lista_bola_choque]