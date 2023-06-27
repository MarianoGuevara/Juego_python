from configuraciones import *
from instancias_objetos_lvl3 import *


def reiniciar_nivel_3():
    '''
    brief: funcion que se encarga de reinciar el nivel 3
    parametros:
    return:
    '''
    personaje_lvl3.vidas = 3
    personaje_lvl3.poderes_disponibles = 4
    personaje_lvl3.puntaje = 0
    personaje_lvl3.que_hace = 'quieto'
    personaje_lvl3.lado_mirando = 'derecha'
    Objeto.reestablecer_posicion(personaje_lvl3, 10, 51)

    Objeto.reestablecer_posicion(lista_coins_lvl3[0], 15, 200)
    Objeto.reestablecer_posicion(lista_coins_lvl3[1], 695, 40)
    Objeto.reestablecer_posicion(lista_coins_lvl3[2], 1235, 60)
    Objeto.reestablecer_posicion(lista_coins_lvl3[3], 1235, 30)
    Objeto.reestablecer_posicion(lista_coins_lvl3[4], 65, 430)

    Objeto.reestablecer_posicion(lista_cherrys_lvl3[0], 1200, 240)
    Objeto.reestablecer_posicion(lista_cherrys_lvl3[1], 5, 420)

    Objeto.reestablecer_posicion(lista_pineapples_lvl3[0], 415, 130)
    Objeto.reestablecer_posicion(lista_pineapples_lvl3[1], 505, 420)


    lista_bats_lvl3.clear()

    bat1 = Enemigo_movimiento_x(lista_movimiento_bat_der[0], 175, 195)
    bat2 = Enemigo_movimiento_x(lista_movimiento_bat_der[0], 900, 250)
    bat3 = Enemigo_movimiento_x(lista_movimiento_bat_der[0], 360, 410)

    lista_bats_lvl3.append(bat1)
    lista_bats_lvl3.append(bat2)
    lista_bats_lvl3.append(bat3)


    lista_slimes_lvl3.clear()

    slime1 = Enemigo_movimiento_x(lista_movimiento_slime_der[0], 550, 115)
    slime2 = Enemigo_movimiento_x(lista_movimiento_slime_der[0], 800, 115)
    lista_slimes_lvl3.append(slime1)
    lista_slimes_lvl3.append(slime2)
    
    boss_final.vidas = 3
    boss_final.lista_proyectiles.clear()
    boss_final.activacion = 'desactivado'
    
    Objeto.reestablecer_posicion(boss_final, 1200, 440)