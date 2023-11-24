from recursos.personaje2.animaciones_personaje import *
from Clase_bola_energia import *
from Clase_Objeto import Objeto
from configuraciones import *
import time

class Personaje (Objeto):
    def __init__(self, imagen, x_inicial, y_inicial):
        '''
        brief: es el contstructor padre
        parametros: imagen: sobre la cual se creará la superficie
        x/y_inicial: posicion inicial del objeto en las cooredenadas x/y
        return: 
        '''
        super().__init__(imagen, x_inicial, y_inicial)

        self.nivel_actual = ''

        self.velocidad = 5

        self.velocidad_animacion = 10

        self.que_hace = 'quieto'
        self.lado_mirando = 'derecha'

        self.gravedad = 1
        self.potencia_salto = -12
        self.limite_velocidad_caida = 10
        self.desplazamiento_y = 0
        self.esta_saltando = False

        self.vidas = 3
        self.vida_a_mostrar = 0

        self.lista_proyectiles = []
        self.poderes_disponibles = 4
        self.poderes_a_mostrar = 0

        self.puntaje = 0
        self.puntaje_a_mostrar = 0

        self.salto_reproducido = False
        self.caminar_reproducido = False



    def gestionar_colisiones_piso_plat(self, plataforma):
        '''
        brief: maneja las colisiones del personaje estando este en el piso
        parametros: plataforma: la plataforma a chocar
        return:
        '''
        if self.rectangulos['right'].colliderect(plataforma.rectangulos['left']):
            self.rectangulos['principal'].right = plataforma.rectangulos['principal'].left
            self.rectangulos['top'].topright = self.forma_fisica.topright
            self.rectangulos['left'].bottomleft = self.forma_fisica.bottomleft
            self.rectangulos['right'].bottomright = self.forma_fisica.bottomright
            self.rectangulos['bottom'].bottomright = self.forma_fisica.bottomright

        elif self.rectangulos['left'].colliderect(plataforma.rectangulos['right']):
            self.rectangulos['principal'].left = plataforma.rectangulos['principal'].right
            self.rectangulos['top'].topright = self.forma_fisica.topright
            self.rectangulos['left'].bottomleft = self.forma_fisica.bottomleft
            self.rectangulos['right'].bottomright = self.forma_fisica.bottomright
            self.rectangulos['bottom'].bottomright = self.forma_fisica.bottomright



    def gestionar_colisiones_salto_plat(self, lista_plataforma):
        '''
        brief: maneja las colisiones del personaje estando este en saltando
        parametros: lista_plataformas: la lista de plataformas a colisionar
        return:
        '''
        for plataforma in lista_plataforma:

            if self.rectangulos['bottom'].colliderect(plataforma.rectangulos['top']):
                self.esta_saltando = False
                self.desplazamiento_y = 0

                self.rectangulos['principal'].bottom = plataforma.rectangulos['principal'].top+1
                self.rectangulos['top'].top = self.forma_fisica.top
                self.rectangulos['left'].bottomleft = self.forma_fisica.bottomleft
                self.rectangulos['right'].bottomright = self.forma_fisica.bottomright
                self.rectangulos['bottom'].bottom = self.forma_fisica.bottom
                break

            elif self.rectangulos['top'].colliderect(plataforma.rectangulos['bottom']):
                self.rectangulos['principal'].top = plataforma.rectangulos['principal'].bottom-1
                self.rectangulos['top'].top = self.forma_fisica.top
                self.rectangulos['left'].bottomleft = self.forma_fisica.bottomleft
                self.rectangulos['right'].bottomright = self.forma_fisica.bottomright
                self.rectangulos['bottom'].bottom = self.forma_fisica.bottom

            elif self.rectangulos['right'].colliderect(plataforma.rectangulos['left']):
                self.rectangulos['principal'].right = plataforma.rectangulos['principal'].left
                self.rectangulos['top'].topright = self.forma_fisica.topright
                self.rectangulos['left'].bottomleft = self.forma_fisica.bottomleft
                self.rectangulos['right'].bottomright = self.forma_fisica.bottomright
                self.rectangulos['bottom'].bottomright = self.forma_fisica.bottomright

            elif self.rectangulos['left'].colliderect(plataforma.rectangulos['right']):
                self.rectangulos['principal'].left = plataforma.rectangulos['principal'].right
                self.rectangulos['top'].topright = self.forma_fisica.topright
                self.rectangulos['left'].bottomleft = self.forma_fisica.bottomleft
                self.rectangulos['right'].bottomright = self.forma_fisica.bottomright
                self.rectangulos['bottom'].bottomright = self.forma_fisica.bottomright
            else:
                self.esta_saltando = True
            self.gestionar_colisiones_piso_plat(plataforma)


    def efectuar_daño_personaje(self):
        '''
        brief: quita una vida al personaje, y realiza el efecto de sonido
        parametros: pantalla: sobre la cual se dibuja la animacion
        return:
        '''
        self.vidas -= 1
        efecto_colision_enemigo.play()



    def gestionar_colision_limite_pantalla(self, posicion_inicial_personaje_lvl):
        '''
        brief: si el personaje cae mas abajo de la pantalla, lo mata
        parametros: posicion_inicial_personaje_lvl: punto de aparicion del perosnaje
        return:
        '''
        if self.forma_fisica.y > 800:
            self.nivel_actual = "menu"



    def aplicar_gravedad(self, pantalla, lista_plataformas, 
                        posicion_inicial_personaje_lvl, lista_salto_der, lista_salto_izq):
        '''
        brief:aplica las colisiones, animaciones y la gravedad del personaje
        parametros: pantalla: sobre la cual se dibuja el obejto.
        lista_plataformas: la lista de plataformas a colisionar. 
        posicion_inicial_personaje_lvl: punto de aparicion del perosnaje
        lista_salto_der/izq: listas que dan ilusion de salto
        return:
        '''
        for plataforma in lista_plataformas:
            self.gestionar_colisiones_piso_plat(plataforma)

        if self.esta_saltando == True:
            if not self.salto_reproducido:
                efecto_salto.play()
                self.salto_reproducido = True
            if self.lado_mirando == "derecha":
                super().animar_accion(lista_salto_der, pantalla)
            elif self.lado_mirando == "izquierda":
                super().animar_accion(lista_salto_izq, pantalla)

            for rect in self.rectangulos:
                self.rectangulos[rect].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        else:
            self.salto_reproducido = False

        self.gestionar_colisiones_salto_plat(lista_plataformas)
        self.gestionar_colision_limite_pantalla(posicion_inicial_personaje_lvl)



    def actuar_personaje(self, lista_movimiento_quieto_der, lista_movimiento_quieto_izq,
                        lista_movimiento_caminar_der, lista_movimiento_caminar_izq,
                        velocidad, pantalla):
        '''
        brief: mueve al personaje correctamente
        parametros:lista_movimiento_quieto_der, lista_movimiento_quieto_izq,
                        lista_movimiento_caminar_der, lista_movimiento_caminar_izq,
                        lista_movimiento_daño_der: listas que dan ilusion de movimiento
                        velocidad: a la que se mueve. pantalla: sobre la cual se dibujara
        return:
        '''
        match self.que_hace:
            case "quieto":
                if self.esta_saltando == False:
                    if self.lado_mirando == "derecha":
                        super().animar_accion(lista_movimiento_quieto_der, pantalla)
                    elif self.lado_mirando == "izquierda":
                        super().animar_accion(lista_movimiento_quieto_izq, pantalla)
            case "derecha":
                self.mover_personaje(velocidad)
                if not self.caminar_reproducido:
                    self.caminar_reproducido = True
                else:
                    self.caminar_reproducido = False
                if self.esta_saltando == False:
                    super().animar_accion(lista_movimiento_caminar_der, pantalla)
            case "izquierda":
                self.mover_personaje(velocidad*-1)
                if not self.caminar_reproducido:
                    self.caminar_reproducido = True
                else:
                    self.caminar_reproducido = False

                if self.esta_saltando == False:
                    super().animar_accion(lista_movimiento_caminar_izq, pantalla)
            case "salta":
                if self.esta_saltando == False:
                    self.esta_saltando = True 
                    self.desplazamiento_y = self.potencia_salto



    def actuar_segun_movimiento(self, pantalla, lista_plataformas,
                            fondo, posicion_inicial_personaje_lvl, sfx):
        '''
        brief: reune las anteriores funciones y da vida al personaje 
        parametros: pantalla: sobre la cual se dibuja el obejto.
        lista_plataformas: la lista de plataformas a colisionar. 
        fondo: imagen de background del nivel. posicion_inicial_personaje_lvl:
        aparicion personaje
        return:
        '''
        pantalla.blit(fondo, (0,0))
        self.actuar_personaje(lista_quieto_derecha, lista_quieto_izquierda, 
                            lista_caminar_derecha, lista_caminar_izquierda,
                            self.velocidad, pantalla)
        self.aplicar_gravedad(pantalla, lista_plataformas, posicion_inicial_personaje_lvl,
                            lista_salto_derecha, lista_salto_izquierda)
        self.mostrar_vidas(pantalla, posicion_inicial_personaje_lvl, 
                        vidas3, vidas2, vidas1, (10,10))
        self.mostrar_puntaje(pantalla)
        self.mostrar_poderes(pantalla)
        self.colisionar_bola_con_plataforma(lista_plataformas)
        self.mutear_efectos(sfx)


    def mover_personaje(self, velocidad):
        '''
        brief: mueve los rectangulos del objeto
        parametros: velocidad: a la que se mueve
        return:
        '''
        for rect in self.rectangulos:
            self.rectangulos[rect].x += velocidad
        self.rectangulos['bottom'].centerx = self.rectangulos['principal'].centerx
        self.rectangulos['bottom'].bottom = self.rectangulos['principal'].bottom



    def mostrar_vidas(self, pantalla, posicion_inicial_personaje_lvl, 
                    vidas_3, vidas_2, vidas_1, ubicacion):
        '''
        brief: muestra una imagen diferente segun las vidas
        parametros: pantalla: sobre la cual se dibuja el obejto.
        posicion_inicial_personaje_lvl: aparicion personaje
        vidas_3, vidas_2, vidas_1: imagenes a mostrar en cada caso
        ubicacion: de las imagenes
        return:
        '''
        if self.vidas == 3:
            self.vida_a_mostrar = vidas_3
        elif self.vidas == 2:
            self.vida_a_mostrar = vidas_2
        elif self.vidas == 1:
            self.vida_a_mostrar = vidas_1
        elif self.vidas < 1:
            efecto_muerte.play()
            self.nivel_actual = "menu"
        pantalla.blit(self.vida_a_mostrar, ubicacion)



    def mostrar_puntaje(self, pantalla):
        '''
        brief: muestra una imagen diferente segun el puntaje
        parametros: pantalla: sobre la cual se dibuja el obejto.
        return:
        '''
        if self.puntaje == 0:
            self.puntaje_a_mostrar = puntaje0
        elif self.puntaje == 1:
            self.puntaje_a_mostrar = puntaje1
        elif self.puntaje == 2:
            self.puntaje_a_mostrar = puntaje2
        elif self.puntaje == 3:
            self.puntaje_a_mostrar = puntaje3
        elif self.puntaje == 4:
            self.puntaje_a_mostrar = puntaje4
        elif self.puntaje == 5:
            self.puntaje_a_mostrar = puntaje5
            
        pantalla.blit(self.puntaje_a_mostrar, (280,10))



    def mostrar_poderes(self, pantalla):
        '''
        brief: muestra una imagen diferente segun los poderes disponibles
        parametros: pantalla: sobre la cual se dibuja el obejto.
        return:
        '''
        if self.poderes_disponibles == 4:
            self.poderes_a_mostrar = poderes4
        elif self.poderes_disponibles == 3:
            self.poderes_a_mostrar = poderes3
        elif self.poderes_disponibles == 2:
            self.poderes_a_mostrar = poderes2
        elif self.poderes_disponibles == 1:
            self.poderes_a_mostrar = poderes1
        elif self.poderes_disponibles == 0:
            self.poderes_a_mostrar = poderes0
        pantalla.blit(self.poderes_a_mostrar, (150,10))



    def reaparecer_personaje(self, posicion_inicial_personaje_lvl):
        '''
        brief: cambia la ubicacion del objeto
        parametros: posicion_inicial_personaje_lvl: ubicacion del personaje
        return:
        '''
        for rect in self.rectangulos:
            self.rectangulos
            self.rectangulos[rect].x = posicion_inicial_personaje_lvl[0]
            self.rectangulos[rect].y = posicion_inicial_personaje_lvl[1]
        self.vidas = 3



    def atacar(self, x,y):
        '''
        brief: crea una bola de energia que derrota a los enemigos
        parametros: x,y: ubicacion de aparicion del poder
        return:
        '''
        proyectil = Bola_Energia(lista_bola_img_der[0], x, y)
        self.lista_proyectiles.append(proyectil)
        efecto_poder.play()



    def eliminar_proyectil(self, proyectil):
        '''
        brief: elimina de pantalla un proyectil ya no necesario
        parametros: proyectil: a eliminar
        return:
        '''
        self.lista_proyectiles.remove(proyectil)



    def verificar_disparo(self, x, y):
        '''
        brief: verifica si el personaje puede atacar.
        parametros: x,y: ubicacion a aparecer el proyectil
        return:
        '''
        if self.poderes_disponibles <= 4 and self.poderes_disponibles > 0:
            self.poderes_disponibles -= 1
            self.atacar(x, y)
            self.que_hace = "quieto"



    def mover_proyectil(self, mirando_personaje, x, limite):
        '''
        brief: mueve correctamente el proyectil
        parametros: mirando_personaje: lado al que mira el personaje 
        a la hora de disparar 
        x: eje x sobre el cual se movera la bola
        limite: para que desaparezca la bola si lo supera
        return:
        '''
        for proyectil in self.lista_proyectiles:
            if mirando_personaje == 'derecha':
                proyectil.animar_bola(lista_bola_img_der, PANTALLA)
                proyectil.trayectoria(-10)
                if proyectil.forma_fisica.x > (x+limite):
                    proyectil.animar_bola(lista_bola_choque, PANTALLA)
                    self.eliminar_proyectil(proyectil)
            elif mirando_personaje == 'izquierda':
                proyectil.animar_bola(lista_bola_img_izq, PANTALLA)
                proyectil.trayectoria(10)
                if proyectil.forma_fisica.x < (x-limite):
                    proyectil.animar_bola(lista_bola_choque, PANTALLA)
                    self.eliminar_proyectil(proyectil)



    def daño_por_bola(self, lista_bolas, nemesis):
        '''
        brief: si una bola colisiona con el objeto, le quita una vida
        parametros: lista_bolas: que efectuan el daño. pantalla: donde se dibuja
        el objeto. nemesis: quien dispara la bola
        return:
        '''
        for bola in lista_bolas:
            if bola.forma_fisica.colliderect(self.forma_fisica):
                self.efectuar_daño_personaje()
                nemesis.eliminar_proyectil(bola)
            else:
                for bola_propia in self.lista_proyectiles:
                    if bola_propia.forma_fisica.colliderect(bola.forma_fisica):
                        nemesis.eliminar_proyectil(bola)
                        self.eliminar_proyectil(bola_propia)



    def colisionar_bola_con_plataforma(self, lista_plataformas):
        '''
        brief: desaparece la bola si esta choca contra una plataforma
        parametros: lista_plataformas: lista de plataformas a chequear colision
        return:
        '''
        for plataforma in lista_plataformas:
            for proyectil in self.lista_proyectiles:
                if proyectil.forma_fisica.colliderect(plataforma.forma_fisica):
                    self.eliminar_proyectil(proyectil)



    def mutear_efectos(self, sfx):
        '''
        brief: segun un parametro, da volumen o mutea los efectos de sonido
        parametros: sfx: formulario con el boton para apagar los efectos
        return:
        '''
        if sfx == True:
            efecto_colision_enemigo.set_volume(0.5)
            efecto_colision_cherry.set_volume(0.1)
            efecto_pineapple.set_volume(0.2)
            efecto_enemy.set_volume(0.2)
            efecto_coin.set_volume(0.2)
            efecto_salto.set_volume(0.2)
            efecto_muerte.set_volume(0.5)
            efecto_paso.set_volume(0.2)
            efecto_poder.set_volume(0.2)
        elif sfx == False:
            efecto_colision_enemigo.set_volume(0)
            efecto_colision_cherry.set_volume(0)
            efecto_pineapple.set_volume(0)
            efecto_enemy.set_volume(0)
            efecto_coin.set_volume(0)
            efecto_salto.set_volume(0)
            efecto_muerte.set_volume(0)
            efecto_paso.set_volume(0)
            efecto_poder.set_volume(0)