from configuraciones import *
from instancias_objetos_lvl1 import *

def reiniciar_nivel_1():
    '''
    brief: funcion que se encarga de reinciar el nivel 1
    parametros:
    return:
    '''
    personaje.vidas = 3
    personaje.poderes_disponibles = 4
    personaje.puntaje = 0
    personaje.que_hace = 'quieto'
    personaje.lado_mirando = 'derecha'
    Objeto.reestablecer_posicion(personaje, 7, 440)

    Objeto.reestablecer_posicion(lista_coins_lvl1[0], 1065, 20)
    Objeto.reestablecer_posicion(lista_coins_lvl1[1], 885, 305)
    Objeto.reestablecer_posicion(lista_coins_lvl1[2], 60, 200)
    Objeto.reestablecer_posicion(lista_coins_lvl1[3], 790, 35)
    Objeto.reestablecer_posicion(lista_coins_lvl1[4], 345, 550)

    Objeto.reestablecer_posicion(lista_cherrys_lvl1[0], 740, 21)
    Objeto.reestablecer_posicion(lista_cherrys_lvl1[1], 5, 186)

    Objeto.reestablecer_posicion(lista_pineapples_lvl1[0], 1165, 15)
    Objeto.reestablecer_posicion(lista_pineapples_lvl1[1], 765, 305)


    lista_slimes_lvl1.clear()

    slime1 = Enemigo_movimiento_x(lista_movimiento_slime_izq[0], 410, 55)
    slime2 = Enemigo_movimiento_x(lista_movimiento_slime_izq[0], 810, 20)
    slime3 = Enemigo_movimiento_x(lista_movimiento_slime_izq[0], 910, 135)

    lista_slimes_lvl1.append(slime1)
    lista_slimes_lvl1.append(slime2)
    lista_slimes_lvl1.append(slime3)