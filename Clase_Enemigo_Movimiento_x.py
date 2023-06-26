from recursos.slime.animacion_slime import *
from recursos.bat.animaciones_bat import *
from Clase_Objeto import Objeto
from Clase_Personaje import Personaje
from configuraciones import efecto_enemy

class Enemigo_movimiento_x (Objeto):
    def __init__(self, imagen, x_inicial, y_inicial) -> None:
        '''
        brief: es el constructor de la clase
        parametros: imagen: sobre la cual se creará la superficie
                    x/y_inicial: posicion inicial del objeto en las cooredenadas x/y
        return: 
        '''
        super().__init__(imagen, x_inicial, y_inicial)

        self.velocidad_animacion = 5

        self.recorrido = 0

        self.direccion = "derecha"
        self.posicion_y = 0

        self.enemigo = ""

        self.atacando = False

        self.vidas = 1



    def animar_slime(self, lista_imagenes, pantalla):
        '''
        brief: anima el objeto
        parametros: lista_imagenes: lista de imagenes que dan la impresion
        de movimiento. Pantalla: Sobre la cual se dibujara el objeto
        return: 
        '''
        super().animar_accion(lista_imagenes, pantalla)



    def movimiento_objeto(self, velocidad):
        '''
        brief: mueve todas las superficies fisicas del objeto en una direccion
        parametros: velocidad: la velocidad a la que se mueve
        return: 
        '''
        for rect in self.rectangulos:
            self.rectangulos[rect].x += velocidad



    def mover_enemigo(self, pantalla, velocidad, enemigo_tipo):
        '''
        brief: mueve y anima correctamente el objeto
        parametros: pantalla: sobre la cual se dibujara. velocidad: a la que 
        se moverá. enemigo_tipo: string que representa si es el slime o el bat
        return: 
        '''
        self.enemigo = enemigo_tipo
        if self.enemigo == 'slime':
            if self.direccion == 'derecha':
                self.movimiento_objeto(velocidad)
                self.animar_slime(lista_movimiento_slime_der, pantalla)
            elif self.direccion == 'izquierda':
                self.movimiento_objeto(-velocidad)
                self.animar_slime(lista_movimiento_slime_izq, pantalla)
        if self.enemigo == 'bat':
            if self.direccion == 'derecha':
                self.movimiento_objeto(velocidad)
                self.animar_slime(lista_movimiento_bat_der, pantalla)
            elif self.direccion == 'izquierda':
                self.movimiento_objeto(-velocidad)
                self.animar_slime(lista_movimiento_bat_izq, pantalla)



    def gestionar_colisiones_plataformas(self, objeto):
        '''
        brief: gestiona las colisiones con las plataformas limite
        parametros: objeto: la plataforma limite
        return:
        '''
        if self.rectangulos['left'].colliderect(objeto.rectangulos['right']):
            self.direccion = 'derecha'
        elif self.rectangulos['right'].colliderect(objeto.rectangulos['left']):
            self.direccion = 'izquierda'



    def gestionar_colisiones_personaje(self, personaje, pantalla):
        '''
        brief: daña al personaje si este choca con el objeto
        parametros: personaje: el personaje en cuestion. Pantalla: sobre la cual
        se dibuja el objeto
        return:
        '''
        if not self.atacando and self.forma_fisica.colliderect(personaje.forma_fisica):
            self.atacando = True
            Personaje.efectuar_daño_personaje(personaje)
        elif not self.forma_fisica.colliderect(personaje.forma_fisica):
            self.atacando = False



    def gestionar_colisiones_bolas(self, lista_bolas, personaje):
        '''
        brief: recorre la lista de proyectiles y si alguno choca con el 
        objeto, lo daña
        parametros: lista_bolas: la lista de bolas que lo daña. Peronaje:
        el personaje principal en cuestión
        return:
        '''
        for bola in lista_bolas:
            if self.forma_fisica.colliderect(bola.forma_fisica):
                self.vidas -= 1
                efecto_enemy.play()
                personaje.eliminar_proyectil(bola)



    def desaparecer_enemigo(self, lista):
        '''
        brief: si las vidas del objeto son 0, lo desaparece
        parametros: lista: lista que contiene todos los objetos de este tipo
        return:
        '''
        if self.vidas == 0:
            lista.remove(self)



    def dibujar_objeto(lista_enemigos, lista_plataformas_limite, lista_bolas, personaje, 
                    pantalla, velocidad, enemigo_tipo):
        '''
        brief: reune las funciones previas y da vida al objeto
        parametros: lista_enemigos:lista que contiene todos los objetos de este tipo. 
        lista_plataformas_limite: con las que colisiona el objeto. lista_bolas: que lo dañan.
        personaje: principal. pantalla: sobre la cual se dibuja. velocidad: a la cual se mueve.
        enemigo_tipo: o slime o bat
        return:
        '''
        for enemigo in lista_enemigos:
            enemigo.desaparecer_enemigo(lista_enemigos)
            enemigo.gestionar_colisiones_personaje(personaje, pantalla)
            enemigo.gestionar_colisiones_bolas(lista_bolas, personaje)
            for plataforma in lista_plataformas_limite:
                enemigo.gestionar_colisiones_plataformas(plataforma)
            enemigo.mover_enemigo(pantalla, velocidad, enemigo_tipo)



