from recursos.cherry.animacion_cherry import *
from Clase_Objeto import Objeto
from configuraciones import *

class Objeto_Consumible (Objeto):
    def __init__(self, imagen, x_inicial, y_inicial):
        '''
        brief: es el constructor de la clase
        parametros: imagen: sobre la cual se creará la superficie
                    x/y_inicial: posicion inicial del objeto en las cooredenadas x/y
        return: 
        '''
        super().__init__(imagen, x_inicial, y_inicial)

        self.velocidad_animacion = 5

        self.objeto_actual = ''



    def animar_objeto_consumible(self, movimiento, pantalla, personaje, objeto_actual):
        '''
        brief: segun el tipo de objeto que sea, lo anima y genera su efecto
        parametros: movimiento: las imagenes que dan la ilusion de movimineto. pantalla:
        sobre la cual se dibujará. personaje: el principal. objeto_actual: string que 
        dice que objeto es el instanciado
        return:
        '''
        self.objeto_actual = objeto_actual
        if self.objeto_actual == 'cherry':
            self.animar_accion(movimiento, pantalla)
            self.generar_efecto_cherry(personaje)
        elif self.objeto_actual == 'pineapple':
            self.animar_accion(movimiento, pantalla)
            self.generar_efecto_pineapple(personaje)
        elif self.objeto_actual == 'coin':
            self.animar_accion(movimiento, pantalla)
            self.generar_efecto_coin(personaje)



    def sacar_objeto_de_pantalla(self):
        '''
        brief: saca de pantalla el objeto una vez se usó
        parametros: 
        return:
        '''
        for rect in self.rectangulos:
            self.rectangulos[rect].x = -100



    def dibujar_objeto(lista_objeto, lista_movimiento, pantalla, 
                    personaje, objeto_actual):
        ''' 
        brief: recorre la lista de todos los objetos y los dibuja en pantalla
        parametros: lista_objeto: lista que contiene todos los objetos del tipo
        lista_movimientos: que generar la ilusion de movimiento. pantalla: sobre la
        cual se dibujara. personaje: el principal. objeto_actual: string que dice 
        que objeto es
        return:
        '''
        for objeto in lista_objeto:
            objeto.animar_objeto_consumible(lista_movimiento, pantalla, personaje, 
                                            objeto_actual)



    def generar_efecto_cherry(self, personaje):
        '''
        brief: cherry. genera el efecto correspondiente
        parametros: personaje: el personaje jugable
        return:
        '''
        if self.forma_fisica.colliderect(personaje.forma_fisica):
            if personaje.vidas != 3:
                personaje.vidas += 1
                efecto_colision_cherry.play()
                self.sacar_objeto_de_pantalla()



    def generar_efecto_pineapple(self, personaje):
        '''
        brief: cherry. genera el efecto correspondiente
        parametros: personaje: el personaje jugable
        return:
        '''
        if self.forma_fisica.colliderect(personaje.forma_fisica):
            if personaje.poderes_disponibles != 4:
                personaje.poderes_disponibles += 1
                efecto_pineapple.play()
                self.sacar_objeto_de_pantalla()



    def generar_efecto_coin(self, personaje):
        '''
        brief: cherry. genera el efecto correspondiente
        parametros: personaje: el personaje jugable
        return:
        '''
        if self.forma_fisica.colliderect(personaje.forma_fisica):
            personaje.puntaje += 1
            efecto_coin.play()
            self.sacar_objeto_de_pantalla()