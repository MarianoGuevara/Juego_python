import random
from Clase_Objeto import Objeto
from Clase_Personaje import Personaje

class Trampa_Dinamica_x (Objeto):
    def __init__(self, imagen, x_inicial, y_inicial, vel_random_inicial, vel_random_final, direccion):
        '''
        brief: es el constructor de la clase
        parametros: imagen: sobre la cual se creará la superficie
        x/y_inicial: posicion inicial del objeto en las cooredenadas x/y
        vel_random_inicial/vel_random_final: velocidades que puede tener la trampa
        direccion: a la cual se dirige la trampa
        return: 
        '''
        super().__init__(imagen, x_inicial, y_inicial)

        self.velocidad_animacion = 5
        self.velocidad = random.randrange(vel_random_inicial, vel_random_final, 1)

        self.vidas = 1

        self.direccion = direccion



    def animar_trampa(self, lista_imagenes, pantalla):
        '''
        brief: anima el objeto
        parametros: lista_imagenes: lista de imagenes que dan la impresion
        de movimiento. Pantalla: Sobre la cual se dibujara el objeto
        return: 
        '''
        super().animar_accion(lista_imagenes, pantalla)



    def mover_trampa(self):
        '''
        brief: mueve los rectangulos del objeto
        parametros: 
        return:
        '''
        for rect in self.rectangulos:
            self.rectangulos[rect].x += self.velocidad



    def spawnear_trampa(self, coordenada_aparicion):
        '''
        brief: spawnea el objeto
        parametros: coordenada_aparicion: donde spawnea el objeto
        return:
        '''
        for rect in self.rectangulos:
                self.rectangulos[rect].x = coordenada_aparicion



    def dibujar_objeto(lista_trampa, lista_movimiento, personaje, pantalla,
                    aparicion_x_min, aparicion_x_max, limite, lista_bolas): 
        '''
        brief: da vida a la trampa
        parametros: lista_trampa: lista con todas las trampas
        lista_movimiento: que da la ilusion de movimiento. personaje: principal;jugable
        pantalla: donde se dibujara el objeto. aparicion_x_min/aparicion_x_max: donde 
        aparecera el objeto en el eje x. limite: hasta donde llega el objeto en el eje x }
        lista_bolas: lista de proyectiles para chequear colisiones
        return:
        '''
        for trampa in lista_trampa:
            trampa.animar_trampa(lista_movimiento, pantalla)
            trampa.reutilizar_trampa(personaje, limite, aparicion_x_min, 
                                    aparicion_x_max, lista_bolas, pantalla)



    def gestionar_colisiones_bolas(self, lista_bolas, personaje, coordenada_aparicion):
        '''
        brief: gestiona lo que sucede si la trampa choca con el jugador
        parametros: lista_bolas: lista de proyectiles para chequear colisiones
        personaje: principal;jugable. coordenada_aparicion: donde spawnea el objeto
        return:
        '''
        for bola in lista_bolas:
            if self.forma_fisica.colliderect(bola.forma_fisica):
                self.vidas -= 1
                self.spawnear_trampa(coordenada_aparicion)
                personaje.eliminar_proyectil(bola)



    def reutilizar_trampa(self, personaje, limite, aparicion_x_min, 
                        aparicion_x_max, lista_bolas, pantalla):
        '''
        brief: reutiliza la trampa en el caso correspondiente
        parametros: personaje: principal;jugable. 
        personaje: principal;jugable
        pantalla: donde se dibujara el objeto. aparicion_x_min/aparicion_x_max: donde 
        aparecera el objeto en el eje x. limite: hasta donde llega el objeto en el eje x 
        lista_bolas: lista de proyectiles para chequear colisiones
        return:
        '''
        self.mover_trampa()

        coordenada_aparicion = random.randrange(aparicion_x_min, aparicion_x_max, 1) 
        
        if self.direccion == 'izquierda':
            if self.forma_fisica.x < limite:
                self.spawnear_trampa(coordenada_aparicion)
            elif self.forma_fisica.colliderect(personaje.forma_fisica):
                Personaje.efectuar_daño_personaje(personaje)
                self.spawnear_trampa(coordenada_aparicion)
            self.gestionar_colisiones_bolas(lista_bolas, personaje, coordenada_aparicion)
        elif self.direccion == 'derecha':
            if self.forma_fisica.x > limite:
                self.spawnear_trampa(coordenada_aparicion)
            elif self.forma_fisica.colliderect(personaje.forma_fisica):
                Personaje.efectuar_daño_personaje(personaje)
                self.spawnear_trampa(coordenada_aparicion)
            self.gestionar_colisiones_bolas(lista_bolas, personaje, coordenada_aparicion)