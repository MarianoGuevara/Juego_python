import pygame, sys
from modo_debug import *

def obtener_fuente(size): # Returns Press-Start-2P in the desired size
    '''
    brief: Devuelve la fuente en el tamaño deseado
    parametros: size: el tamaño que tendra la fuente
    return: Devuelve la fuente en el tamaño deseado
    '''
    return pygame.font.Font("interfaz/font.ttf", size)



def crear_texto(pantalla, texto, tamaño, posicion):
    '''
    brief: Crea un texto y lo dibuja en pantalla
    parametros: pantalla: donde se dibujara el texto. texto: el texto 
    propiamente dicho. tamaño: el cual tendra el texto. posicion: en la 
    cual se dibujará
    return:
    '''
    PLAY_TEXT = obtener_fuente(tamaño).render(texto, True, "Black")
    PLAY_RECT = PLAY_TEXT.get_rect(center=posicion)
    pantalla.blit(PLAY_TEXT, PLAY_RECT)



def capturar_eventos():
    '''
    brief: Captura los eventos del juego y segun el caso, realiza activa
    el modo debug o cierra el juego
    parametros: 
    return: 
    '''
    for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()



def mover_personaje_teclas(personaje):
    '''
    brief: Captura las teclas presionadas y acciona al personaje segun 
    las mismas
    parametros: personaje: personaje jugable
    return: 
    '''
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_ESCAPE]:
        personaje.nivel_actual = 'pausa'
    elif tecla[pygame.K_RIGHT] and personaje.forma_fisica.x < 1230:
        personaje.que_hace = "derecha"
        personaje.lado_mirando = 'derecha'
    elif tecla[pygame.K_LEFT] and personaje.forma_fisica.x > -5:
        personaje.que_hace = "izquierda"
        personaje.lado_mirando = 'izquierda'
    elif tecla[pygame.K_UP] and personaje.forma_fisica.y > 0:
        personaje.que_hace = "salta"
    else:
        personaje.que_hace = "quieto"



def verificar_disparo(personaje):
    '''
    brief: Se encarga de capturar y verificar el disparo del personaje
    parametros: personaje: personaje jugable
    return: 
    '''
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_SPACE]:
        if len(personaje.lista_proyectiles) < 1:
            x = personaje.forma_fisica.x
            y = personaje.forma_fisica.y
            mirando_personaje = personaje.lado_mirando 
            personaje.verificar_disparo(x, y)

    if len(personaje.lista_proyectiles) > 0:
        personaje.mover_proyectil(mirando_personaje, x, 225)



def dar_vuelta_lista(lista, flip_x, flip_y):
    '''
    brief: da vuelta segun como se diga una lista de imagenes
    parametros: lista: lista de imagenes a dar vuelta
    flip_x/flip_y: si se dará vuelta en el eje x o y
    return: devuelve la lista rotada
    '''
    lista_dada_vuelta = []
    for imagen in lista:
        lista_dada_vuelta.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_dada_vuelta



def reescalar_imagenes(lista_animaciones, ancho, alto):
    '''
    brief: reescala una lista de imagenes
    parametros: lista_animaciones: lista que contiene las imagenes a reesclar
    ancho/alto: al cual se reescalaran las imagenes
    return:
    '''
    for lista_imagen in lista_animaciones:
        for i in range(len(lista_imagen)):
            imagen = lista_imagen[i]
            lista_imagen[i] = pygame.transform.scale(imagen, (ancho,alto))