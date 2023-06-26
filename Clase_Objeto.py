import pygame

class Objeto:
    def __init__(self, imagen, x_inicial, y_inicial):
        '''
        brief: es el contstructor padre
        parametros: imagen: sobre la cual se creará la superficie
        x/y_inicial: posicion inicial del objeto en las cooredenadas x/y
        return: 
        '''
        self.imagen = imagen
        self.forma_fisica = self.imagen.get_rect()

        self.forma_fisica.x = x_inicial
        self.forma_fisica.y = y_inicial

        self.rectangulos = Objeto.obtener_rectangulos(self.forma_fisica)

        self.contador_pasos = 0 



    def obtener_rectangulos(principal:pygame.Rect)->dict:
        '''
        brief: obtiene una serie se superficies mas especificas sobre una general
        parametros: principal: superficie general
        return:
        '''
        diccionario = {}
        diccionario['principal'] = principal
        diccionario['top'] = pygame.Rect(principal.left, principal.top,
                                        principal.width, 6)
        diccionario['bottom'] = pygame.Rect(principal.left, principal.bottom-6, 
                                            principal.width, 6)
        diccionario['left'] = pygame.Rect(principal.left, principal.top,
                                        6, principal.height)
        diccionario['right'] = pygame.Rect(principal.right-2, 
                                        principal.top, 6, principal.height)
        return diccionario



    def animar_accion(self, movimiento, pantalla):
        '''
        brief: anima una serie de imagenes dandole ilusion de movimiento
        parametros: movimiento: imagenes que debe animar, pantalla: donde se 
        dibuja
        return:
        '''
        cant_imagenes = len(movimiento)
        if self.contador_pasos >= (cant_imagenes * self.velocidad_animacion):
            self.contador_pasos = 0

        frecuencia_actualizacion = self.contador_pasos // self.velocidad_animacion

        pantalla.blit(movimiento[frecuencia_actualizacion], self.forma_fisica)
        self.contador_pasos += 1



    def reestablecer_posicion(personaje, coordenada_x, coordenada_y):
        for rectangulo in personaje.rectangulos:
            personaje.rectangulos[rectangulo].x = coordenada_x
            personaje.rectangulos[rectangulo].y = coordenada_y