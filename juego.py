import pygame, sys
from configuraciones import *
from interfaz.GUI_form_selector_lvls import *
from interfaz.GUI_form_menu_principal import *
from funcionalidades_generales import *
from modo_debug import *
from textos_lore import *
from interfaz.GUI_form_lore import Form_lore
from interfaz.GUI_form_pausa import *
from instancias_objetos_lvl1 import *
from instancias_objetos_lvl2 import *
from instancias_objetos_lvl3 import *
from reiniciar_nivel_1 import reiniciar_nivel_1
from reiniciar_nivel_2 import reiniciar_nivel_2
from reiniciar_nivel_3 import reiniciar_nivel_3
from screen_error import mostrar_pantalla_error


form_manejador_lvls = Form_Manejador_Lvls(PANTALLA, 0, 0, ANCHO_PANTALLA, 
                                        ALTO_PANTALLA, "Black", "Black", 1, True)
form_menu_principal = Form_Menu_Principal(PANTALLA, 0, 0, ANCHO_PANTALLA, 
                                        ALTO_PANTALLA, "Black", "Black", 1, True)
form_pausa = Form_pausa(PANTALLA, 0, 0, ANCHO_PANTALLA, ALTO_PANTALLA, "Black",
                        "Black", 1, True)
form_lore = Form_lore(PANTALLA, 0, 0, ANCHO_PANTALLA, 
                    ALTO_PANTALLA, "Black", "Black", 1, True )


def pausa():
    '''
    brief: Funcion que se encarga de ejecutar el menu de pausa
    parametros:
    return:
    '''
    pausado = True
    try:
        while pausado:
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            form_pausa.update(eventos)

            crear_texto(PANTALLA, 'PAUSA', 35, (605,160), 'Black')
            crear_texto(PANTALLA, 'DES-PAUSAR', 15, (605,250), 'Black')
            crear_texto(PANTALLA, 'MENU', 15, (605,350), 'Black')
            crear_texto(PANTALLA, 'SFX', 10, (605,475), 'Black')

            if form_pausa.nivel_actual == 'pausa':
                pass
            elif form_pausa.nivel_actual == 'menu':
                form_pausa.nivel_actual = ''
                pygame.mixer.music.stop()
                menu_principal_funcion()
            elif form_pausa.nivel_actual == 'unpause':
                form_pausa.nivel_actual = ''
                pausado = False
            pygame.display.flip()
    except Exception:
        mostrar_pantalla_error()



def nivel_uno():
    '''
    brief: Funcion que se encarga de ejecutar el nivel 1
    parametros:
    return:
    '''
    try:
        pygame.mixer.init()
        pygame.mixer.music.load('recursos/efectos/fairy_8bit.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        nivel_uno_running = True
        while nivel_uno_running:
            reloj.tick(FPS)
            capturar_eventos()

            personaje.actuar_segun_movimiento(PANTALLA, 
                                            lista_plataformas_lvl1, imagen_fondo_lvl1,
                                            posicion_inicial_personaje_lvl1, 
                                            form_pausa.checkbox.sfx_bool)
            Objeto_Consumible.dibujar_objeto(lista_cherrys_lvl1, lista_movimiento_cherry, 
                                            PANTALLA, personaje, 'cherry')
            Objeto_Consumible.dibujar_objeto(lista_pineapples_lvl1, lista_movimiento_pineapple, 
                                            PANTALLA, personaje, 'pineapple')
            Objeto_Consumible.dibujar_objeto(lista_coins_lvl1, lista_movimiento_coin, 
                                            PANTALLA, personaje, 'coin')
            Trampa_Dinamica_x.dibujar_objeto(lista_trampas_fuego_lvl1, 
                                            lista_movimiento_trampa_fuego_izq, personaje,
                                            PANTALLA, 405, 680, 55, personaje.lista_proyectiles)
            Enemigo_movimiento_x.dibujar_objeto(lista_slimes_lvl1, 
                                                lista_plataformas_limite_slime_lvl1,
                                                personaje.lista_proyectiles, personaje, PANTALLA, 
                                                6, 'slime')
            Trampa_Estatica.dibujar_objeto(lista_trampas_pinchos_lvl1, PANTALLA, personaje)
            Plataforma.dibujar_objeto(lista_plataformas_lvl1, PANTALLA)
            key.funcionar_key_paso_lvl(personaje, PANTALLA, 1, form_manejador_lvls)


            mover_personaje_teclas(personaje)
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_SPACE]:
                if len(personaje.lista_proyectiles) < 1:
                    x = personaje.forma_fisica.x
                    y = personaje.forma_fisica.y
                    mirando_personaje = personaje.lado_mirando 
                    personaje.verificar_disparo(x, y)
            if len(personaje.lista_proyectiles) > 0:
                personaje.mover_proyectil(mirando_personaje, x, 225)

            if obtener_modo() == True:
                mostrar_figuras(PANTALLA, personaje, lista_plataformas_lvl1, 
                                lista_plataformas_limite_slime_lvl1, 
                                lista_slimes_lvl1, lista_trampas_pinchos_lvl1, 
                                lista_cherrys_lvl1, lista_coins_lvl1, lista_pineapples_lvl1,
                                'no', 'no', lista_trampas_fuego_lvl1, '', '')

            if personaje.nivel_actual == 'pausa':
                personaje.nivel_actual = ''
                pausa()
            elif personaje.nivel_actual == 'menu':
                personaje.nivel_actual = ''
                menu_principal_funcion()

            pygame.display.flip()
    except Exception:
        mostrar_pantalla_error()



def nivel_dos():
    '''
    brief: Funcion que se encarga de ejecutar el nivel 2
    parametros:
    return:
    '''
    try:
        pygame.mixer.init()
        pygame.mixer.music.load('recursos/efectos/fma_8bit.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        while True:
            reloj.tick(FPS)
            capturar_eventos()

            personaje_lvl2.actuar_segun_movimiento(PANTALLA, lista_plataformas_lvl2, 
            imagen_fondo_lvl2, posicion_inicial_personaje_lvl2, form_pausa.checkbox.sfx_bool)

            Objeto_Consumible.dibujar_objeto(lista_coins_lvl2, lista_movimiento_coin, 
                                            PANTALLA, personaje_lvl2, 'coin')
            Objeto_Consumible.dibujar_objeto(lista_pineapples_lvl2, 
                                            lista_movimiento_pineapple, PANTALLA,
                                            personaje_lvl2, 'pineapple')
            Objeto_Consumible.dibujar_objeto(lista_cherrys_lvl2, lista_movimiento_cherry, 
                                            PANTALLA, personaje_lvl2, 'cherry')
            Trampa_Estatica.dibujar_objeto(lista_trampas_pinchos_lvl2, PANTALLA,
                                            personaje_lvl2)
            Plataforma.dibujar_objeto(lista_plataformas_lvl2, PANTALLA)
            Enemigo_movimiento_x.dibujar_objeto(lista_bats_lvl2, 
                                                lista_plataformas_limite_bat_lvl2, 
                                                personaje_lvl2.lista_proyectiles, 
                                                personaje_lvl2, PANTALLA, 5, 'bat')
            Enemigo_movimiento_x.dibujar_objeto(lista_slimes_lvl2, 
                                                lista_plataformas_limite_bat_lvl2, 
                                                personaje_lvl2.lista_proyectiles, 
                                                personaje_lvl2, PANTALLA, 7, 'slime')
            Trampa_Dinamica_x.dibujar_objeto(lista1_trampas_fuego_lvl2, 
                                            lista_movimiento_trampa_fuego_izq, 
                                            personaje_lvl2, PANTALLA, 1250, 1300,
                                            350, personaje_lvl2.lista_proyectiles)
            Trampa_Dinamica_x.dibujar_objeto(lista2_trampas_fuego_lvl2, 
                                            lista_movimiento_trampa_fuego_izq, personaje_lvl2,
                                            PANTALLA, 645, 650, 
                                            0, personaje_lvl2.lista_proyectiles)
            Trampa_Dinamica_x.dibujar_objeto(lista3_trampas_fuego_lvl2, 
                                            lista_movimiento_trampa_fuego_izq, personaje_lvl2,
                                            PANTALLA, 1250, 1300, 
                                            650, personaje_lvl2.lista_proyectiles)
            key_lvl2.funcionar_key_paso_lvl(personaje_lvl2, PANTALLA, 2, form_manejador_lvls)

            mover_personaje_teclas(personaje_lvl2)
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_SPACE]:
                if len(personaje_lvl2.lista_proyectiles) < 1:
                    x = personaje_lvl2.forma_fisica.x
                    y = personaje_lvl2.forma_fisica.y
                    mirando_personaje = personaje_lvl2.lado_mirando 
                    personaje_lvl2.verificar_disparo(x, y)
            if len(personaje_lvl2.lista_proyectiles) > 0:
                personaje_lvl2.mover_proyectil(mirando_personaje, x, 225)

            if obtener_modo() == True:
                mostrar_figuras(PANTALLA, personaje_lvl2, lista_plataformas_lvl2,
                                lista_plataformas_limite_bat_lvl2,
                                lista_slimes_lvl2, lista_trampas_pinchos_lvl2, 
                                lista_cherrys_lvl2, lista_coins_lvl2,
                                lista_pineapples_lvl2, 'si', 'si', 
                                listas_trampa_fuego_debug, 3, lista_bats_lvl2)

            if personaje_lvl2.nivel_actual == 'pausa':
                personaje_lvl2.nivel_actual = ''
                pausa()
            elif personaje_lvl2.nivel_actual == 'menu':
                personaje_lvl2.nivel_actual = ''
                menu_principal_funcion()

            pygame.display.flip()
    except Exception:
        mostrar_pantalla_error()



def nivel_tres():
    '''
    brief: Funcion que se encarga de ejecutar el nivel 3
    parametros:
    return:
    '''
    try:
        pygame.mixer.init()
        pygame.mixer.music.load('recursos/efectos/naruto_8bit.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        while True:
            reloj.tick(FPS)
            capturar_eventos()

            personaje_lvl3.actuar_segun_movimiento(PANTALLA, lista_plataformas_lvl3, 
                                                imagen_fondo_lvl3, 
                                                posicion_inicial_personaje_lvl3,
                                                form_pausa.checkbox.sfx_bool)
            personaje_lvl3.daño_por_bola(boss_final.lista_proyectiles, boss_final)

            Objeto_Consumible.dibujar_objeto(lista_coins_lvl3, lista_movimiento_coin, 
                                            PANTALLA, personaje_lvl3, 'coin')
            Objeto_Consumible.dibujar_objeto(lista_pineapples_lvl3, lista_movimiento_pineapple, 
                                            PANTALLA, personaje_lvl3, 'pineapple')
            Objeto_Consumible.dibujar_objeto(lista_cherrys_lvl3, lista_movimiento_cherry, 
                                            PANTALLA, personaje_lvl3, 'cherry')
            Plataforma.dibujar_objeto(lista_plataformas_lvl3, PANTALLA)
            png_boss_final.crear_png_boss_final(PANTALLA, personaje_lvl3, boss_final)
            Trampa_Estatica.dibujar_objeto(lista_trampas_pinchos_lvl3, PANTALLA, personaje_lvl3)
            Trampa_Dinamica_x.dibujar_objeto(lista1_trampas_fuego_lvl3, 
                                            lista_movimiento_trampa_fuego_der, personaje_lvl3,
                                            PANTALLA, -200, -100, 400,
                                            personaje_lvl3.lista_proyectiles)
            Trampa_Dinamica_x.dibujar_objeto(lista2_trampas_fuego_lvl3, 
                                            lista_movimiento_trampa_fuego_izq, personaje_lvl3,
                                            PANTALLA, 1300, 1500, 
                                            750, personaje_lvl3.lista_proyectiles)
            Trampa_Dinamica_x.dibujar_objeto(lista3_trampas_fuego_lvl3, 
                                            lista_movimiento_trampa_fuego_izq, personaje_lvl3,
                                            PANTALLA, 1300, 1500, 0, personaje_lvl3.lista_proyectiles)
            Enemigo_movimiento_x.dibujar_objeto(lista_bats_lvl3, lista_plataformas_limite_bat_lvl3, 
                                                personaje_lvl3.lista_proyectiles, personaje_lvl3, 
                                                PANTALLA, 5, 'bat')
            Enemigo_movimiento_x.dibujar_objeto(lista_slimes_lvl3, 
                                                lista_plataformas_limite_bat_lvl3, 
                                                personaje_lvl3.lista_proyectiles, 
                                                personaje_lvl3, PANTALLA, 5, 'slime')

            boss_final.mover_enemigo(lista_quieto_izquierda_boss, PANTALLA, 
                                    lista_plataformas_lvl3, posicion_inicial_boss, 
                                    personaje_lvl3.lista_proyectiles, personaje_lvl3)

            mover_personaje_teclas(personaje_lvl3)
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_SPACE]:
                if len(personaje_lvl3.lista_proyectiles) < 1:
                    x = personaje_lvl3.forma_fisica.x
                    y = personaje_lvl3.forma_fisica.y
                    mirando_personaje = personaje_lvl3.lado_mirando 
                    personaje_lvl3.verificar_disparo(x, y)
            if len(personaje_lvl3.lista_proyectiles) > 0:
                personaje_lvl3.mover_proyectil(mirando_personaje, x, 225)

            if boss_final.activacion == 'activado':
                if len(boss_final.lista_proyectiles) < 1:
                    lado_mirando_boss = boss_final.lado_mirando
                    x_boss = boss_final.forma_fisica.x
                    y_boss = boss_final.forma_fisica.y
                    boss_final.atacar_boss(x_boss, y_boss)

                if len(boss_final.lista_proyectiles) > 0:
                    boss_final.mover_proyectil(lado_mirando_boss, x_boss, 570)

            if obtener_modo() == True:
                mostrar_figuras(PANTALLA, personaje_lvl3, 
                                lista_plataformas_lvl3, lista_plataformas_limite_bat_lvl3,
                                lista_slimes_lvl3, lista_trampas_pinchos_lvl3,
                                lista_cherrys_lvl3, lista_coins_lvl3,
                                lista_pineapples_lvl3, 'si', 'si',
                                listas_trampa_fuego_debug2, 2, lista_bats_lvl3)
                for rectangulo in boss_final.rectangulos:
                    pygame.draw.rect(PANTALLA, 'Black', boss_final.rectangulos[rectangulo], 2)
                for rectangulo in png_boss_final.rectangulos:
                    pygame.draw.rect(PANTALLA, 'Green', png_boss_final.rectangulos[rectangulo], 2)

            if personaje_lvl3.nivel_actual == 'pausa':
                personaje_lvl3.nivel_actual = ''
                pausa()
            elif personaje_lvl3.nivel_actual == 'menu':
                personaje_lvl3.nivel_actual = ''
                mostrar_lore_final()

            pygame.display.flip()
    except Exception:
        mostrar_pantalla_error()



def mostrar_lore_inicio():
    '''
    brief: Funcion que se encarga de mostrar la pantalla con la historia 
    inicial del juego
    parametros:
    return:
    '''
    try:
        while True:
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            PANTALLA.fill('Black')

            form_lore.update(eventos)
            crear_texto(PANTALLA, 'JUGAR', 15, (600,440), 'Black')

            textos_lore_inicio()

            if form_lore.jugar == True:
                form_lore.jugar = False
                form_lore.menu = False
                reiniciar_nivel_1()
                nivel_uno()


            pygame.display.flip()
    except Exception:
        mostrar_pantalla_error()



def mostrar_lore_final():
    '''
    brief: Funcion que se encarga de ejecutar la pantalla de error en caso
    de que haya uno
    parametros:
    return:
    '''
    try:
        while True:
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            PANTALLA.fill('Black')

            form_lore.update(eventos)

            textos_lore_final()

            if form_lore.menu == True:
                form_lore.menu = False
                form_lore.jugar = False
                menu_principal_funcion()

            pygame.display.flip()
    except Exception:
        mostrar_pantalla_error()



def niveles():
    '''
    brief: Funcion que se encarga de ejecutar el navegador entre los 3 niveles
    parametros:
    return:
    '''
    try:
        while True:
            reloj.tick(FPS)
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if form_manejador_lvls.nivel_actual == 'menu':
                pass
            elif form_manejador_lvls.nivel_actual == 'uno':
                form_manejador_lvls.nivel_actual = ''
                mostrar_lore_inicio()
            elif form_manejador_lvls.nivel_actual == 'dos':
                form_manejador_lvls.nivel_actual = ''
                reiniciar_nivel_2()
                nivel_dos()
            elif form_manejador_lvls.nivel_actual == 'tres':
                form_manejador_lvls.nivel_actual = ''
                reiniciar_nivel_3()
                nivel_tres()
            elif form_manejador_lvls.nivel_actual == 'menu_principal':
                form_manejador_lvls.nivel_actual = ''
                menu_principal_funcion()

            form_manejador_lvls.cambiar_boton()
            form_manejador_lvls.update(eventos)


            crear_texto(PANTALLA, '1', 30, (620,175), 'Black')
            crear_texto(PANTALLA, '2', 30, (620,265), 'Black')
            crear_texto(PANTALLA, '3', 30, (620,365), 'Black')

            pygame.display.flip()
    except Exception:
        mostrar_pantalla_error()



def menu_principal_funcion():
    '''
    brief: Funcion que se encarga de ejecutar el menu principal
    parametros:
    return:
    '''
    try:
        pygame.mixer.init()
        pygame.mixer.music.load('recursos/efectos/unravel_8bit.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        while True:
            reloj.tick(FPS)
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if form_menu_principal.nivel_actual == 'selector':
                form_menu_principal.nivel_actual = ''
                niveles()
            elif form_menu_principal.nivel_actual == 'quit':
                pygame.quit()
                sys.exit()

            form_menu_principal.update(eventos)

            crear_texto(PANTALLA, 'EL ANTIHEROE', 25, (610,175), 'Black')
            crear_texto(PANTALLA, 'NIVELES', 25, (610,290), 'Black')

            pygame.display.flip()
    except Exception:
        mostrar_pantalla_error()

menu_principal_funcion()