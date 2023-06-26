from Clase_plataforma import Plataforma

class Trampa_Estatica (Plataforma):
    def __init__(self, ruta, x_inicial, y_inicial, tamaño) -> None:
        '''
        brief: es el constructor de la clase
        parametros: ruta: de la imagen que dara apariencia a la plataforma
        x/y_inicial: posicion inicial del objeto en las cooredenadas x/y
        tamaño: de la imagen de la plataforma
        return: 
        '''
        super().__init__(ruta, x_inicial, y_inicial, tamaño)



    def gestionar_colision(self, personaje):
        '''
        brief: gestiona las colisiones del personaje con la trampa
        parametros: personaje: sobre el cual gestiona la colision
        return: 
        '''
        if self.rectangulos['top'].colliderect(personaje.rectangulos['bottom']):
            personaje.vidas = 0



    def dibujar_objeto(lista_objeto, pantalla, personaje):
        '''
        brief: dibuja el objeto en la pantalla y acciona su funcion
        parametros: lista_objeto: la lista que contiene todos los objetos del tipo
        pantalla: sobre la cual se dibuja el objeto. personaje: sobre el cual hace
        un efecto
        return: 
        '''
        for trampa in lista_objeto:
            trampa.gestionar_colision(personaje)
            pantalla.blit(trampa.forma_visual, trampa.forma_fisica)