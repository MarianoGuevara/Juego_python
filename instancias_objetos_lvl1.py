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
from recursos.coin.animaciones_coin import *
from recursos.slime.animacion_slime import *
from configuraciones import *


reescalar_imagenes(lista_animaciones_personaje, 50, 60)
reescalar_imagenes(lista_animaciones_bola, 90, 50)

personaje = Personaje(lista_caminar_derecha[0], posicion_inicial_personaje_lvl1[0],
                    posicion_inicial_personaje_lvl1[1])

piso_pasto_mediano_1 = Plataforma(plataforma_pasto_mediano, 0, 525, (75,40))
piso_pasto_mediano_2 = Plataforma(plataforma_pasto_mediano, 750, 80, (75,40))
piso_pasto_mediano_3 = Plataforma(plataforma_pasto_mediano, 5, 245, (80,40))

piso_pasto_chiquito_1 = Plataforma(plataforma_pasto_1, 150, 590, (40,40))
piso_pasto_chiquito_2 = Plataforma(plataforma_pasto_1, 270, 525, (40,40))
piso_pasto_chiquito_3 = Plataforma(plataforma_pasto_1, 370, 450, (40,40))
piso_pasto_chiquito_4 = Plataforma(plataforma_pasto_1, 260, 380, (40,40))
piso_pasto_chiquito_5 = Plataforma(plataforma_pasto_1, 150, 310, (40,40))
piso_pasto_chiquito_7 = Plataforma(plataforma_pasto_1, 150, 170, (40,40))
piso_pasto_chiquito_8 = Plataforma(plataforma_pasto_1, 300, 170, (40,40))
piso_pasto_chiquito_9 = Plataforma(plataforma_pasto_1, 760, 350, (40,40))
piso_pasto_chiquito_10 = Plataforma(plataforma_pasto_1, 880, 350, (40,40))
piso_pasto_chiquito_11 = Plataforma(plataforma_pasto_1, 1000, 350, (40,40))
piso_pasto_chiquito_12 = Plataforma(plataforma_pasto_1, 1120, 350, (40,40))
piso_pasto_chiquito_13 = Plataforma(plataforma_pasto_1, 340, 590, (40,40))

piso_pasto_largo_1 = Plataforma(plataforma_pasto_largo_estat, 410, 100, (340,40))
piso_pasto_largo_2 = Plataforma(plataforma_pasto_largo_flot, 825, 65, (380,40))
piso_pasto_largo_3 = Plataforma(plataforma_pasto_largo_flot, 880, 180, (380,40))
piso_pasto_largo_4 = Plataforma(plataforma_pasto_largo_estat, 750, 570, (415,40))

pared_vertical_largo_1 = Plataforma(plataforma_roca_largo, 410, 140, (40,525))
pared_vertical_largo_2 = Plataforma(plataforma_roca_largo, 710, 140, (40,525))
pared_vertical_largo_3 = Plataforma(plataforma_roca_largo, 1125, 605, (40,525))

png_techo = Plataforma(png_vacio, 0, -50, (ANCHO_PANTALLA,40))

fondo_plano = Plataforma(piso_plano, 450, 135, (260,550))
fondo_plano2 = Plataforma(piso_plano, 710, 610, (415,40))

png_pared_izq = Plataforma(png_vacio, -50, 0, (40,ALTO_PANTALLA))

lista_plataformas_lvl1 = [
                    piso_pasto_chiquito_1, piso_pasto_chiquito_2, piso_pasto_chiquito_3, 
                    piso_pasto_chiquito_4, piso_pasto_chiquito_5, 
                    piso_pasto_chiquito_7, piso_pasto_chiquito_8,
                    piso_pasto_chiquito_9, piso_pasto_chiquito_10, 
                    piso_pasto_chiquito_11, piso_pasto_chiquito_12, piso_pasto_chiquito_13,

                    piso_pasto_mediano_1, piso_pasto_mediano_2, piso_pasto_mediano_3,

                    piso_pasto_largo_1, piso_pasto_largo_2, piso_pasto_largo_3, 
                    piso_pasto_largo_4,

                    pared_vertical_largo_1, pared_vertical_largo_2, pared_vertical_largo_3,
                    
                    png_techo, 

                    fondo_plano, fondo_plano2,

                    png_pared_izq
                    ]


reescalar_imagenes(lista_animaciones_slime, 45, 45)
slime1 = Enemigo_movimiento_x(lista_movimiento_slime_izq[0], 410, 55)
slime2 = Enemigo_movimiento_x(lista_movimiento_slime_izq[0], 810, 20)
slime3 = Enemigo_movimiento_x(lista_movimiento_slime_izq[0], 910, 135)

lista_slimes_lvl1 = [slime1, slime2, slime3]

png_slime = Plataforma(png_vacio, 360, 50, (50,50))
png_slime2 = Plataforma(png_vacio, 750, 50, (50,50))

png_slime3 = Plataforma(png_vacio, 1210, 15, (50,50))
png_slime4 = Plataforma(png_vacio, 770, 15, (50,50))

png_slime5 = Plataforma(png_vacio, 830, 135, (50,50))
png_slime6 = Plataforma(png_vacio, 1265, 135, (50,50))

lista_plataformas_limite_slime_lvl1 = [
    png_slime, png_slime2,

    png_slime3, png_slime4,

    png_slime5, png_slime6,
]


pinchos = Trampa_Estatica(pinchos_imagen, 760, 400, (100,35))
pinchos2 = Trampa_Estatica(pinchos_imagen, 860, 400, (100,35))
pinchos3 = Trampa_Estatica(pinchos_imagen, 960, 400, (100,35))
pinchos4 = Trampa_Estatica(pinchos_imagen, 1060, 400, (100,35))

lista_trampas_pinchos_lvl1 = [pinchos, pinchos2, pinchos3, pinchos4]


reescalar_imagenes(lista_animaciones_trampa_fuego, 50,40)
trampa_fuego1 = Trampa_Dinamica_x(lista_movimiento_trampa_fuego_izq[0], random.randrange(415, 565, 1), 260, -6,-4, 'izquierda')
trampa_fuego2 = Trampa_Dinamica_x(lista_movimiento_trampa_fuego_izq[0], random.randrange(415, 565, 1), 135, -6,-4, 'izquierda')
trampa_fuego3 = Trampa_Dinamica_x(lista_movimiento_trampa_fuego_izq[0], random.randrange(415, 565, 1), 410, -6,-4, 'izquierda')
trampa_fuego4 = Trampa_Dinamica_x(lista_movimiento_trampa_fuego_izq[0], random.randrange(415, 565, 1), 550, -6,-4, 'izquierda')

lista_trampas_fuego_lvl1 = [trampa_fuego1, trampa_fuego2, trampa_fuego3, trampa_fuego4]


reescalar_imagenes(lista_animaciones_cherry, 50, 50)
cherry1 = Objeto_Consumible(lista_movimiento_cherry[0], 740, 21)
cherry2 = Objeto_Consumible(lista_movimiento_cherry[0], 5, 186)

lista_cherrys_lvl1 = [cherry1, cherry2]


reescalar_imagenes(lista_animaciones_pineapple, 30, 40)
pineapple1 = Objeto_Consumible(lista_movimiento_pineapple[0], 1165, 15)
pineapple2 = Objeto_Consumible(lista_movimiento_pineapple[0], 765, 305)

lista_pineapples_lvl1 = [pineapple1, pineapple2]


reescalar_imagenes(lista_animaciones_coin, 30, 30)
coin1 = Objeto_Consumible(lista_movimiento_coin[0], 1065, 20)
coin2 = Objeto_Consumible(lista_movimiento_coin[0], 885, 305)
coin3 = Objeto_Consumible(lista_movimiento_coin[0], 60, 200)
coin4 = Objeto_Consumible(lista_movimiento_coin[0], 790, 35)
coin5 = Objeto_Consumible(lista_movimiento_coin[0], 345, 550)

lista_coins_lvl1 = [coin1, coin2, coin3, coin4, coin5]


key = Plataforma("recursos/key.png", 760,500, (30,50))
# key_lvl2 = Plataforma("recursos/key.png", 760,500, (30,50))