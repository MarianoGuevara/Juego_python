import random
from Clase_Personaje import *
from Clase_boss_final import *
from Clase_plataforma import Plataforma
from Clase_Trampa_dinamica_x import Trampa_Dinamica_x
from Clase_Trampa_estatica_horizontal import Trampa_Estatica
from Clase_Objeto_Consumible import Objeto_Consumible
from Clase_Enemigo_Movimiento_x import Enemigo_movimiento_x
from recursos.trampas.trampa_horizontal.animacion_trampa_fuego import *
from recursos.cherry.animacion_cherry import *
from recursos.pineapple.animaciones_pineapple import *
from recursos.bat.animaciones_bat import *
from recursos.slime.animacion_slime import *
from recursos.coin.animaciones_coin import *
from configuraciones import *

reescalar_imagenes(lista_animaciones_personaje, 50, 60)
reescalar_imagenes(lista_animaciones_bola, 90, 50)

personaje_lvl3 = Personaje(lista_caminar_derecha[0], posicion_inicial_personaje_lvl3[0],
                        posicion_inicial_personaje_lvl3[1])


reescalar_imagenes(lista_animaciones_boss_final, 50, 60)
reescalar_imagenes(lista_animaciones_bola_boss, 90, 50)

boss_final = Boss_Final(lista_caminar_derecha_boss[0], posicion_inicial_boss[0], 
                        posicion_inicial_boss[1])


piso_pasto_chiquito_1 = Plataforma(plataforma_pasto_1, 410, 180, (40,40))
piso_pasto_chiquito_2 = Plataforma(plataforma_pasto_1, 980, 100, (40,40))
piso_pasto_chiquito_3 = Plataforma(plataforma_pasto_1, 1100, 160, (40,40))
piso_pasto_chiquito_4 = Plataforma(plataforma_pasto_1, 950, 325, (40,40))
piso_pasto_chiquito_5 = Plataforma(plataforma_pasto_1, 1075, 300, (40,40))
piso_pasto_chiquito_6 = Plataforma(plataforma_pasto_1, 1200, 300, (40,40))
piso_pasto_chiquito_7 = Plataforma(plataforma_pasto_1, 845, 300, (40,40))
piso_pasto_chiquito_8 = Plataforma(plataforma_pasto_1, 500, 475, (40,40))

piso_pasto_mediano_1 = Plataforma(plataforma_pasto_mediano, 0, 110, (75,40))
piso_pasto_mediano_2 = Plataforma(plataforma_pasto_mediano, 1210, 100, (75,40))

piso_pasto_largo_1 = Plataforma(plataforma_pasto_largo_flot, 0, 250, (340,40))
piso_pasto_largo_2 = Plataforma(plataforma_pasto_largo_flot, 550, 160, (340,40))

piso_pasto_super_largo_1 = Plataforma(plataforma_pasto_super_largo_estat, 600, 540, (680,40))
piso_pasto_super_largo_2 = Plataforma(plataforma_pasto_super_largo_estat, -250, 475, (680,40))

pared_vertical_largo_1 = Plataforma(plataforma_roca_largo, 600, 580, (40,525))
pared_vertical_largo_2 = Plataforma(plataforma_roca_largo, 390, 515, (40,525))

fondo_plano = Plataforma(piso_plano, 0, 515, (390,300))
fondo_plano2 = Plataforma(piso_plano, 640, 580, (800,200))

png_pared_izq = Plataforma(png_vacio, -50, 0, (40,ALTO_PANTALLA))

lista_plataformas_lvl3 = [
    piso_pasto_chiquito_1, piso_pasto_chiquito_2, piso_pasto_chiquito_3, piso_pasto_chiquito_4,
    piso_pasto_chiquito_5, piso_pasto_chiquito_6, piso_pasto_chiquito_7, piso_pasto_chiquito_8,

    piso_pasto_mediano_1, piso_pasto_mediano_2,

    piso_pasto_largo_1, piso_pasto_largo_2,
    piso_pasto_super_largo_1, piso_pasto_super_largo_2,

    pared_vertical_largo_1, pared_vertical_largo_2,

    fondo_plano, fondo_plano2,

    png_pared_izq
]



pinchos_1 = Trampa_Estatica(pinchos_imagen, 340, 260, (100,35))
pinchos_2 = Trampa_Estatica(pinchos_imagen, 440, 260, (100,35))

pinchos_3 = Trampa_Estatica(pinchos_imagen, 1050, 350, (100,35))
pinchos_4 = Trampa_Estatica(pinchos_imagen, 950, 350, (100,35))
pinchos_5 = Trampa_Estatica(pinchos_imagen, 850, 350, (100,35))
pinchos_6 = Trampa_Estatica(pinchos_imagen, 750, 350, (100,35))
pinchos_7 = Trampa_Estatica(pinchos_imagen, 1150, 350, (100,35))

lista_trampas_pinchos_lvl3 = [
    pinchos_1, pinchos_2, pinchos_3, pinchos_4, pinchos_5, pinchos_6, pinchos_7,
]



reescalar_imagenes(lista_animaciones_coin, 30, 30)
coin1 = Objeto_Consumible(lista_movimiento_coin[0], 15, 200)
coin2 = Objeto_Consumible(lista_movimiento_coin[0], 695, 40)
coin3 = Objeto_Consumible(lista_movimiento_coin[0], 1235, 60)
coin4 = Objeto_Consumible(lista_movimiento_coin[0], 1235, 30)
coin5 = Objeto_Consumible(lista_movimiento_coin[0], 65, 430)

lista_coins_lvl3 = [coin1, coin2, coin3, coin4, coin5]


reescalar_imagenes(lista_animaciones_pineapple, 30, 40)
pineapple1 = Objeto_Consumible(lista_movimiento_pineapple[0], 415, 130)
pineapple2 = Objeto_Consumible(lista_movimiento_pineapple[0], 505, 420)

lista_pineapples_lvl3 = [pineapple1, pineapple2]


reescalar_imagenes(lista_animaciones_cherry, 50, 50)
cherry1 = Objeto_Consumible(lista_movimiento_cherry[0], 1200, 240)
cherry2 = Objeto_Consumible(lista_movimiento_cherry[0], 5, 420)

lista_cherrys_lvl3 = [cherry1, cherry2]



reescalar_imagenes(lista_animaciones_bat, 40, 40)
bat1 = Enemigo_movimiento_x(lista_movimiento_bat_der[0], 175, 195)
bat2 = Enemigo_movimiento_x(lista_movimiento_bat_der[0], 900, 250)
bat3 = Enemigo_movimiento_x(lista_movimiento_bat_der[0], 360, 410)

lista_bats_lvl3 = [bat1, bat2, bat3]


reescalar_imagenes(lista_animaciones_slime, 45, 45)
slime1 = Enemigo_movimiento_x(lista_movimiento_slime_der[0], 550, 115)
slime2 = Enemigo_movimiento_x(lista_movimiento_slime_der[0], 800, 115)
lista_slimes_lvl3 = [slime1, slime2]

png_bat = Plataforma(png_vacio, -30, 200, (50,50))
png_bat2 = Plataforma(png_vacio, 430, 200, (50,50))
png_slime3 = Plataforma(png_vacio, 500, 101, (50,50))
png_slime4 = Plataforma(png_vacio, 900, 101, (50,50))
png_bat5 = Plataforma(png_vacio, 675, 250, (50,50))
png_bat6 = Plataforma(png_vacio, 1250, 250, (50,50))
png_bat7 = Plataforma(png_vacio, 430, 430, (50,50))
png_bat8 = Plataforma(png_vacio, -30, 430, (50,50))

lista_plataformas_limite_bat_lvl3 = [
    png_bat, png_bat2, png_slime3, png_slime4, png_bat5, png_bat6, png_bat7, png_bat8
]


reescalar_imagenes(lista_animaciones_trampa_fuego, 55,40)
trampa_fuego1 = Trampa_Dinamica_x(lista_movimiento_trampa_fuego_der[0], random.randrange(-200, -100, 1), 175, 5,7, 'derecha')
trampa_fuego2 = Trampa_Dinamica_x(lista_movimiento_trampa_fuego_izq[0], random.randrange(1300, 1500, 1), 50, -7,-5, 'izquierda')
trampa_fuego3 = Trampa_Dinamica_x(lista_movimiento_trampa_fuego_izq[0], random.randrange(1300, 1500, 1), 255, -7,-5, 'izquierda')
trampa_fuego4 = Trampa_Dinamica_x(lista_movimiento_trampa_fuego_izq[0], random.randrange(1300, 1500, 1), 415, -7,-5, 'izquierda')

lista1_trampas_fuego_lvl3 = [trampa_fuego1]
lista2_trampas_fuego_lvl3 = [trampa_fuego2, trampa_fuego3]
lista3_trampas_fuego_lvl3 = [trampa_fuego4]


listas_trampa_fuego_debug2 = [lista1_trampas_fuego_lvl3, lista2_trampas_fuego_lvl3, lista3_trampas_fuego_lvl3]

png_boss_final = Plataforma(png_vacio, 700, 470, (100,75))