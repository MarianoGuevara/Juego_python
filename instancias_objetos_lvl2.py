import random
from Clase_Personaje import *
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

personaje_lvl2 = Personaje(lista_caminar_derecha[0], posicion_inicial_personaje_lvl2[0],
                        posicion_inicial_personaje_lvl2[1])


piso_pasto_chiquito_1 = Plataforma(plataforma_pasto_1, 130, 175, (40,40))
piso_pasto_chiquito_2 = Plataforma(plataforma_pasto_1, 285, 175, (40,40))
piso_pasto_chiquito_3 = Plataforma(plataforma_pasto_1, 425, 175, (40,40))
piso_pasto_chiquito_4 = Plataforma(plataforma_pasto_1, 565, 125, (40,40))
piso_pasto_chiquito_5 = Plataforma(plataforma_pasto_1, 800, 575, (40,40))
piso_pasto_chiquito_6 = Plataforma(plataforma_pasto_1, 935, 515, (40,40))
piso_pasto_chiquito_7 = Plataforma(plataforma_pasto_1, 1190, 375, (40,40))
piso_pasto_chiquito_8 = Plataforma(plataforma_pasto_1, 1070, 310, (40,40))
piso_pasto_chiquito_9 = Plataforma(plataforma_pasto_1, 1190, 240, (40,40))
piso_pasto_chiquito_10 = Plataforma(plataforma_pasto_1, 1070, 175, (40,40))
piso_pasto_chiquito_11 = Plataforma(plataforma_pasto_1, 970, 125, (40,40))
piso_pasto_chiquito_12 = Plataforma(plataforma_pasto_1, 835, 125, (40,40))
piso_pasto_chiquito_13 = Plataforma(plataforma_pasto_1, 1050, 575, (40,40))


piso_pasto_mediano_1 = Plataforma(plataforma_pasto_mediano, 0, 150, (75,40))
piso_pasto_mediano_2 = Plataforma(plataforma_pasto_mediano, 1050, 450, (75,40))
piso_pasto_mediano_3 = Plataforma(plataforma_pasto_mediano, 685, 65, (100,40))

piso_pasto_largo_1 = Plataforma(plataforma_pasto_largo_estat, 0, 410, (340,40))
piso_pasto_largo_2 = Plataforma(plataforma_pasto_largo_estat, 340, 480, (340,40))
piso_pasto_largo_3 = Plataforma(plataforma_pasto_largo_flot, 690, 330, (340,40))

pared_vertical_largo_1 = Plataforma(plataforma_roca_largo, 650, -150, (40,525))
pared_vertical_largo_2 = Plataforma(plataforma_roca_largo, 640, 520, (40,525))

roca_corto_1 = Plataforma(plataforma_roca_corto, 300, 450, (40,40))

fondo_plano = Plataforma(piso_plano, 0, 450, (300,300))
fondo_plano2 = Plataforma(piso_plano, 340, 520, (300,300))
fondo_plano3 = Plataforma(piso_plano, 300, 480, (40,300))

png_pared_izq = Plataforma(png_vacio, -50, 0, (40,ALTO_PANTALLA+100))

lista_plataformas_lvl2 = [
    piso_pasto_chiquito_1, piso_pasto_chiquito_2, piso_pasto_chiquito_3, piso_pasto_chiquito_4,
    piso_pasto_chiquito_5, piso_pasto_chiquito_6, piso_pasto_chiquito_7, piso_pasto_chiquito_8,
    piso_pasto_chiquito_9, piso_pasto_chiquito_10, piso_pasto_chiquito_11, piso_pasto_chiquito_12,
    piso_pasto_chiquito_13,

    piso_pasto_mediano_1, piso_pasto_mediano_2, piso_pasto_mediano_3,

    piso_pasto_largo_1, piso_pasto_largo_2, piso_pasto_largo_3,

    pared_vertical_largo_1, pared_vertical_largo_2,

    roca_corto_1,

    fondo_plano, fondo_plano2, fondo_plano3,

    png_pared_izq
]

pinchos_0 = Trampa_Estatica(pinchos_imagen, -25, 245, (100,35))
pinchos_1 = Trampa_Estatica(pinchos_imagen, 75, 245, (100,35))
pinchos_2 = Trampa_Estatica(pinchos_imagen, 175, 245, (100,35))
pinchos_3 = Trampa_Estatica(pinchos_imagen, 275, 245, (100,35))
pinchos_4 = Trampa_Estatica(pinchos_imagen, 375, 245, (100,35))
pinchos_5 = Trampa_Estatica(pinchos_imagen, 800, 170, (100,35))
pinchos_6 = Trampa_Estatica(pinchos_imagen, 900, 170, (100,35))
pinchos_7 = Trampa_Estatica(pinchos_imagen, 700, 170, (100,35))



lista_trampas_pinchos_lvl2 = [pinchos_0, pinchos_1, 
                            pinchos_2, pinchos_3, pinchos_4,
                            pinchos_5, pinchos_6, pinchos_7
                            ]



reescalar_imagenes(lista_animaciones_bat, 40, 40)
bat1 = Enemigo_movimiento_x(lista_movimiento_bat_der[0], 115, 130)
bat2 = Enemigo_movimiento_x(lista_movimiento_bat_der[0], 600, 130)
bat3 = Enemigo_movimiento_x(lista_movimiento_bat_der[0], 725, 265)
bat4 = Enemigo_movimiento_x(lista_movimiento_bat_der[0], 900, 535)

lista_bats_lvl2 = [bat1, bat2, bat3, bat4]

reescalar_imagenes(lista_animaciones_slime, 45, 45)
slime1 = Enemigo_movimiento_x(lista_movimiento_slime_der[0], 50, 365)
lista_slimes_lvl2 = [slime1]


png_bat = Plataforma(png_vacio, 650, 120, (50,50))
png_bat2 = Plataforma(png_vacio, 100, 120, (50,50))
png_bat3 = Plataforma(png_vacio, 640, 270, (50,50))
png_bat4 = Plataforma(png_vacio, 1030, 270, (50,50))
png_bat5 = Plataforma(png_vacio, 640, 525, (50,50))
png_bat6 = Plataforma(png_vacio, 1090, 525, (50,50))
png_slime7 = Plataforma(png_vacio, -30, 360, (50,50))
png_slime8 = Plataforma(png_vacio, 330, 360, (50,50))

lista_plataformas_limite_bat_lvl2 = [
    png_bat, png_bat2,

    png_bat3, png_bat4,

    png_bat5, png_bat6,

    png_slime7, png_slime8
]


reescalar_imagenes(lista_animaciones_trampa_fuego, 55,45)
trampa_fuego1 = Trampa_Dinamica_x(lista_movimiento_trampa_fuego_izq[0], random.randrange(1600, 1700, 1), 420, -8,-7, 'izquierda')
trampa_fuego2 = Trampa_Dinamica_x(lista_movimiento_trampa_fuego_izq[0], random.randrange(645, 650, 1), 350, -7,-5, 'izquierda')
trampa_fuego3 = Trampa_Dinamica_x(lista_movimiento_trampa_fuego_izq[0], random.randrange(1600, 1700, 1), 85, -7,-5, 'izquierda')


lista1_trampas_fuego_lvl2 = [trampa_fuego1]
lista2_trampas_fuego_lvl2 = [trampa_fuego2]
lista3_trampas_fuego_lvl2 = [trampa_fuego3]

listas_trampa_fuego_debug = [lista1_trampas_fuego_lvl2, lista2_trampas_fuego_lvl2, lista3_trampas_fuego_lvl2]

reescalar_imagenes(lista_animaciones_coin, 30, 30)
coin1 = Objeto_Consumible(lista_movimiento_coin[0], 570, 80)
coin2 = Objeto_Consumible(lista_movimiento_coin[0], 570, 40)
coin3 = Objeto_Consumible(lista_movimiento_coin[0], 10, 360)
coin4 = Objeto_Consumible(lista_movimiento_coin[0], 1055, 540)
coin5 = Objeto_Consumible(lista_movimiento_coin[0], 1055, 500)

lista_coins_lvl2 = [coin1, coin2, coin3, coin4, coin5]

reescalar_imagenes(lista_animaciones_pineapple, 30, 40)
pineapple1 = Objeto_Consumible(lista_movimiento_pineapple[0], 50, 360)
pineapple2 = Objeto_Consumible(lista_movimiento_pineapple[0], 1075, 400)

lista_pineapples_lvl2 = [pineapple1, pineapple2]


reescalar_imagenes(lista_animaciones_cherry, 50, 50)
cherry1 = Objeto_Consumible(lista_movimiento_cherry[0], 350, 420)
cherry2 = Objeto_Consumible(lista_movimiento_cherry[0], 700, 275)

lista_cherrys_lvl2 = [cherry1, cherry2]


key_lvl2 = Plataforma("recursos/key.png", 710,10, (30,50))

