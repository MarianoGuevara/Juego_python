import pygame, sys
from configuraciones import PANTALLA
from funcionalidades_generales import obtener_fuente

def mostrar_pantalla_error():
    '''
    brief: Funcion que se encarga de ejecutar la pantalla de error en caso
    de que haya uno
    parametros:
    return:
    '''
    while True:
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        PANTALLA.fill('Black')

        PLAY_TEXT = obtener_fuente(25).render("ERROR! perdon las molestias", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(620, 260))
        PANTALLA.blit(PLAY_TEXT, PLAY_RECT)

        pygame.display.flip()