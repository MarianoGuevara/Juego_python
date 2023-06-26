import pygame
from constantes import * 



pygame.init()

PANTALLA = pygame.display.set_mode(tamaño_pantalla)
imagen_fondo_lvl1 = pygame.image.load(fondo_medio_dia)
imagen_fondo_lvl1 = pygame.transform.scale(imagen_fondo_lvl1, tamaño_pantalla)

imagen_fondo_lvl2 = pygame.image.load(fondo_atardecer)
imagen_fondo_lvl2 = pygame.transform.scale(imagen_fondo_lvl2, tamaño_pantalla)

imagen_fondo_lvl3 = pygame.image.load(fondo_noche)
imagen_fondo_lvl3 = pygame.transform.scale(imagen_fondo_lvl3, tamaño_pantalla)

# timer_imagen = pygame.image.load(timer_ruta)
# timer_imagen = pygame.transform.scale(timer_imagen, (80,40))
# fuente_pixel = pygame.font.Font(fuente_ruta, 50)

reloj = pygame.time.Clock()

vidas3 = pygame.image.load(corazones3_ruta)
vidas3 = pygame.transform.scale(vidas3, (115,40))

vidas2 = pygame.image.load(corazones2_ruta)
vidas2 = pygame.transform.scale(vidas2, (115,40))

vidas1 = pygame.image.load(corazones1_ruta)
vidas1 = pygame.transform.scale(vidas1, (115,40))


puntaje0 = pygame.image.load(puntaje0_visual_ruta)
puntaje0 = pygame.transform.scale(puntaje0, (100,40))

puntaje1 = pygame.image.load(puntaje1_visual_ruta)
puntaje1 = pygame.transform.scale(puntaje1, (100,40))

puntaje2 = pygame.image.load(puntaje2_visual_ruta)
puntaje2 = pygame.transform.scale(puntaje2, (100,40))

puntaje3 = pygame.image.load(puntaje3_visual_ruta)
puntaje3 = pygame.transform.scale(puntaje3, (100,40))

puntaje4 = pygame.image.load(puntaje4_visual_ruta)
puntaje4 = pygame.transform.scale(puntaje4, (100,40))

puntaje5 = pygame.image.load(puntaje5_visual_ruta)
puntaje5 = pygame.transform.scale(puntaje5, (100,40))


poderes4 = pygame.image.load(poderes4_ruta)
poderes4 = pygame.transform.scale(poderes4, (115,40))

poderes3 = pygame.image.load(poderes3_ruta)
poderes3 = pygame.transform.scale(poderes3, (115,40))

poderes2 = pygame.image.load(poderes2_ruta)
poderes2 = pygame.transform.scale(poderes2, (115,40))

poderes1 = pygame.image.load(poderes1_ruta)
poderes1 = pygame.transform.scale(poderes1, (115,40))

poderes0 = pygame.image.load(poderes0_ruta)
poderes0 = pygame.transform.scale(poderes0, (115,40))


efecto_colision_enemigo = pygame.mixer.Sound(ruta_musica_colision)

efecto_colision_cherry = pygame.mixer.Sound(ruta_musica_agarra_cherry)

efecto_pineapple = pygame.mixer.Sound(ruta_musica_agarra_pineapple)

efecto_enemy = pygame.mixer.Sound(ruta_muerte_sonido_enemigo)

efecto_coin = pygame.mixer.Sound(ruta_musica_agarra_coin)

efecto_salto = pygame.mixer.Sound(ruta_salto)

efecto_muerte = pygame.mixer.Sound(ruta_muerte_sonido)

efecto_paso = pygame.mixer.Sound(ruta_musica_paso)

efecto_poder = pygame.mixer.Sound(ruta_musica_poder)


boss_vidas3 = pygame.image.load(boss_corazones3_ruta)
boss_vidas3 = pygame.transform.scale(boss_vidas3, (115,40))

boss_vidas2 = pygame.image.load(boss_corazones2_ruta)
boss_vidas2 = pygame.transform.scale(boss_vidas2, (115,40))

boss_vidas1 = pygame.image.load(boss_corazones1_ruta)
boss_vidas1 = pygame.transform.scale(boss_vidas1, (115,40))