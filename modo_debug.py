import pygame

DEBUG = False

def cambiar_modo():
    '''
    brief: cambia el valor del booleano
    parametros:
    return: devuelve el booleano con su valor invertido
    '''
    global DEBUG
    DEBUG = not DEBUG



def obtener_modo():
    '''
    brief: obtiene el modo
    parametros:
    return: DEBUG; un booleano
    '''
    return DEBUG



def actualizar_bats(pantalla, lista_bats):
    '''
    brief: muestra el contorno del contenido especifico de una lista
    parameteros: lista_bats: la lista sobre la cual muestra el contorno
    return:
    '''
    for bat in lista_bats:
        for rectangulo in bat.rectangulos:
            pygame.draw.rect(pantalla, (125, 60, 152), bat.rectangulos[rectangulo], 2)



def actualizar_multiples_bolas_fuego(pantalla, lista_bolas, cantidad):
    '''
    brief: muestra el contorno del contenido especifico de una lista
    parameteros: lista_bolas: la lista sobre la cual muestra el contorno
    cantidad: de bolas 
    return:
    '''
    for i in range(cantidad):
        for trampa_fuego in lista_bolas[i]:
            for rectangulo in trampa_fuego.rectangulos:
                pygame.draw.rect(pantalla, 'Red', trampa_fuego.rectangulos[rectangulo], 2)



def actualizar_bolas_fuego(pantalla, lista_bolas):
    '''
    brief: muestra el contorno del contenido especifico de una lista
    parameteros: lista_bolas: la lista sobre la cual muestra el contorno 
    return:
    '''
    for trampa_fuego in lista_bolas:
            for rectangulo in trampa_fuego.rectangulos:
                pygame.draw.rect(pantalla, 'Red', trampa_fuego.rectangulos[rectangulo], 2)



def mostrar_figuras(pantalla, personaje, lista_plataformas, 
                    lista_plataformas_limite, lista_slimes,
                    lista_trampas_pinchos,lista_cherrys, lista_coins,
                    lista_pineapples, bola_fuego_multiples, bats,
                    lista_bolas_fuego, cantidad, lista_bats):
    '''
    brief: muestra el contorno de todos los objetos del juego
    parameteros: pantalla: donde se dibujaran estos contornos
    personaje, lista_plataformas, lista_plataformas_limite, 
    lista_slimes,lista_trampas_pinchos,lista_cherrys, lista_coins,
    lista_pineapples, bola_fuego_multiples, bats,
    lista_bolas_fuego, cantidad, lista_bats: De todos estos, se mostrará
    el contorno
    return:
    '''
    for rectangulo in personaje.rectangulos:
            pygame.draw.rect(pantalla, (244, 208, 63), personaje.rectangulos[rectangulo], 2)
    for plataforma in lista_plataformas:
        for rectangulo in plataforma.rectangulos:
            pygame.draw.rect(pantalla, (192, 57, 43), plataforma.rectangulos[rectangulo], 2)
    for plataforma in lista_plataformas_limite:
        for rectangulo in plataforma.rectangulos:
            pygame.draw.rect(pantalla, "Blue", plataforma.rectangulos[rectangulo], 2)
    for slime in lista_slimes:
        for rectangulo in slime.rectangulos:
            pygame.draw.rect(pantalla, (125, 60, 152), slime.rectangulos[rectangulo], 2)
    for pincho in lista_trampas_pinchos:
        for rectangulo in pincho.rectangulos:
            pygame.draw.rect(pantalla, (125, 60, 152), pincho.rectangulos[rectangulo], 2)
    for cherry in lista_cherrys:
        for rectangulo in cherry.rectangulos:
            pygame.draw.rect(pantalla, 'Gray', cherry.rectangulos[rectangulo], 2)
    for coin in lista_coins:
        for rectangulo in coin.rectangulos:
            pygame.draw.rect(pantalla, 'Gray', coin.rectangulos[rectangulo], 2)
    for pineapple in lista_pineapples:
        for rectangulo in pineapple.rectangulos:
            pygame.draw.rect(pantalla, 'Gray', pineapple.rectangulos[rectangulo], 2)
    if len(personaje.lista_proyectiles) > 0:
        for bola in personaje.lista_proyectiles:
            for rectangulo in bola.rectangulos:
                pygame.draw.rect(pantalla, 'Blue', bola.rectangulos[rectangulo], 2)
    if bola_fuego_multiples == 'si':
        actualizar_multiples_bolas_fuego(pantalla, lista_bolas_fuego, cantidad)
    else:
        actualizar_bolas_fuego(pantalla, lista_bolas_fuego)
    if bats == 'si':
        actualizar_bats(pantalla, lista_bats)