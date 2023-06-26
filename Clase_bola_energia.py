from Clase_Objeto import Objeto

class Bola_Energia (Objeto):
    def __init__(self, imagen, x_inicial, y_inicial):
        '''
        brief: es el constructor de la clase bola energia
        parametros: imagen: sobre la cual se creará la superficie
                    x/y_inicial: posicion inicial del objeto en las cooredenadas x/y
        return: 
        '''
        super().__init__(imagen, x_inicial, y_inicial)

        self.velocidad_animacion = 5
        self.forma_fisica.left = x_inicial
        self.forma_fisica.top = y_inicial



    def animar_bola(self, lista_imagenes, pantalla):
        '''
        brief: anima la bola
        parametros: lista_imagenes: lista de imagenes que dan la impresion
        de movimiento. Pantalla: Sobre la cual se dibujara el objeto
        return: 
        '''
        super().animar_accion(lista_imagenes, pantalla)



    def trayectoria(self, velocidad):
        '''
        brief: mueve todas las superficies fisicas del objeto en una direccion
        parametros: velocidad: la velocidad a la que se mueve
        return: 
        '''
        for rectangulo in self.rectangulos:
            self.rectangulos[rectangulo].left = self.rectangulos[rectangulo].left - velocidad


