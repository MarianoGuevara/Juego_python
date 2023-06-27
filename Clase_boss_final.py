from recursos.boss_final.animaciones_boss_final import *
from configuraciones import *
from Clase_Personaje import Personaje

class Boss_Final(Personaje):
    def __init__(self, imagen, x_inicial, y_inicial):
        '''
        brief: es el constructor de la clase
        parametros: imagen: sobre la cual se creará la superficie
                    x/y_inicial: posicion inicial del objeto en las cooredenadas x/y
        return: 
        '''
        super().__init__(imagen, x_inicial, y_inicial)

        self.velocidad_animacion = 18

        self.lado_mirando = 'izquierda'
        self.que_hace = 'quieto'

        self.divisor = 10
        self.velocidad = 20

        self.activacion = 'desactivado'

        self.atacando = False



    def actuar_boss(self, pantalla):
        ''' 
        brief: mueve al personaje y lo anima
        parametros: pantalla: sobre la cual se dibujara el objeto
        return:
        '''
        super().actuar_personaje(lista_quieto_derecha_boss, 
                                lista_quieto_izquierda_boss,
                                lista_caminar_derecha_boss, 
                                lista_caminar_izquierda_boss,
                                self.velocidad, pantalla)



    def animar_boss(self, lista_movimiento, pantalla, 
                    lista_plataformas, posicion_inicial_personaje_lvl):
        '''
        brief: funcion que aplica la gravedad, anima y mueve al boss final
        parametros: lista_movimientos: los cuales animan al boss. pantalla: sobre
        la cual se dibuja el objeto. lista_plataformas: sobre las cuales puede chocar
        el boss. posicion_inicial_personaje_lvl: punto de aparicion del boss.
        return:
        '''
        super().aplicar_gravedad(pantalla, lista_plataformas, posicion_inicial_personaje_lvl,
                                lista_salto_derecha_boss, lista_salto_izquierda_boss)
        self.actuar_boss(pantalla)



    def atacar_boss(self, x, y):
        '''
        brief: hace que el boss final active el ataque
        parametros: x, y: donde se creará el proyectil
        return:
        '''
        if self.que_hace == 'quieto':
            super().atacar(x, y)



    def ataque_boss(self, lado_mirando, x):
        '''
        brief: se encarga de mover correctamente el proyectil
        parametros: lado_mirando: lado mirando del personaje para animar 
        correctamente. x: eje x sobre el cual se movera la bola
        return:
        '''
        super().mover_proyectil(lado_mirando, x)



    def limitar_movimiento(self):
        '''
        brief: limita el movimiento del boss final
        parametros:
        return:
        '''
        if self.forma_fisica.x <= 605:
            self.lado_mirando = 'derecha'
            self.que_hace = 'derecha'
            self.velocidad = 20
        if self.que_hace == 'derecha' and self.forma_fisica.x >= 1220:
            self.lado_mirando = 'izquierda'
            self.que_hace = 'quieto'



    def mover_enemigo(self, lista_movimiento, pantalla, 
                    lista_plataformas, posicion_inicial_personaje_lvl, lista_bolas, nemesis):
        '''
        brief: reune las funciones anteriores y le da vida al boss final
        parametros: lista_movimiento: lista de imagenes que dan la impresion de movimiento
        pantalla: sobre la cual se dibujara el objeto. lista_plataformas: sobre las 
        cuales puede chocar el boss. posicion_inicial_personaje_lvl: punto de aparicion del boss.
        lista_bolas: proyectiles que pueden dañar al boss. Nemesis: el personaje principal
        return:
        '''
        super().mostrar_vidas(pantalla, posicion_inicial_personaje_lvl, boss_vidas3, 
                            boss_vidas2, boss_vidas1, (1130,590))
        self.animar_boss(lista_movimiento, pantalla, lista_plataformas, 
                        posicion_inicial_personaje_lvl)
        super().daño_por_bola(lista_bolas, nemesis)
        self.hacer_daño_personaje(nemesis, pantalla)

        tiempo_pasado_literal = pygame.time.get_ticks()
        tiempo_pasado_segundos = tiempo_pasado_literal // 1000

        if (tiempo_pasado_segundos % self.divisor) == 0:
            self.que_hace = 'izquierda'

        self.limitar_movimiento()
        self.ganar_juego(nemesis)



    def hacer_daño_personaje(self, personaje, pantalla):
        '''
        brief: daña al personaje principal con una embestida
        parametros: personaje: el personaje principal. pantalla: sobre 
        la cual se dibujara el objeto.
        return:
        '''
        if self.que_hace == 'izquierda':
            if not self.atacando and self.forma_fisica.colliderect(personaje.forma_fisica):
                self.atacando = True
                Personaje.efectuar_daño_personaje(personaje)
            elif not self.forma_fisica.colliderect(personaje.forma_fisica):
                self.atacando = False



    def ganar_juego(self, personaje):
        '''
        brief: regresa el personaje al menu luego de ganarle al boss
        parametros: personaje: el personaje principal
        return:
        '''
        if self.vidas == 0:
            personaje.nivel_actual = 'menu'