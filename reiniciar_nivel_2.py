from configuraciones import *
from instancias_objetos_lvl2 import *

def reiniciar_nivel_2():
    '''
    brief: funcion que se encarga de reinciar el nivel 2
    parametros:
    return:
    '''
    personaje_lvl2.vidas = 3
    personaje_lvl2.poderes_disponibles = 4
    personaje_lvl2.puntaje = 0
    personaje_lvl2.que_hace = 'quieto'
    personaje_lvl2.lado_mirando = 'derecha'
    Objeto.reestablecer_posicion(personaje_lvl2, 10, 55)

    Objeto.reestablecer_posicion(lista_coins_lvl2[0], 570, 80)
    Objeto.reestablecer_posicion(lista_coins_lvl2[1], 570, 40)
    Objeto.reestablecer_posicion(lista_coins_lvl2[2], 10, 360)
    Objeto.reestablecer_posicion(lista_coins_lvl2[3], 1055, 540)
    Objeto.reestablecer_posicion(lista_coins_lvl2[4], 1055, 500)

    Objeto.reestablecer_posicion(lista_cherrys_lvl2[0], 350, 420)
    Objeto.reestablecer_posicion(lista_cherrys_lvl2[1], 700, 275)

    Objeto.reestablecer_posicion(lista_pineapples_lvl2[0], 50, 360)
    Objeto.reestablecer_posicion(lista_pineapples_lvl2[1], 1075, 400)


    lista_bats_lvl2.clear()

    bat1 = Enemigo_movimiento_x(lista_movimiento_bat_der[0], 115, 130)
    bat2 = Enemigo_movimiento_x(lista_movimiento_bat_der[0], 600, 130)
    bat3 = Enemigo_movimiento_x(lista_movimiento_bat_der[0], 725, 265)
    bat4 = Enemigo_movimiento_x(lista_movimiento_bat_der[0], 900, 535)

    lista_bats_lvl2.append(bat1)
    lista_bats_lvl2.append(bat2)
    lista_bats_lvl2.append(bat3)
    lista_bats_lvl2.append(bat4)


    lista_slimes_lvl2.clear()
    slime1 = Enemigo_movimiento_x(lista_movimiento_slime_der[0], 50, 365)
    lista_slimes_lvl2.append(slime1)