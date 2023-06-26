import pygame

class Plataforma:
    def __init__(self, ruta, x_inicial, y_inicial, tamaño) -> None:
        '''
        brief: es el constructor de la clase
        parametros: ruta: de la imagen que dara apariencia a la plataforma
        x/y_inicial: posicion inicial del objeto en las cooredenadas x/y
        tamaño: de la imagen de la plataforma
        return: 
        '''
        self.forma_visual = pygame.image.load(ruta)
        self.forma_visual = pygame.transform.scale(self.forma_visual, (tamaño[0],tamaño[1]))
        self.forma_fisica = self.forma_visual.get_rect()

        self.forma_fisica.x = x_inicial
        self.forma_fisica.y = y_inicial

        self.rectangulos = Plataforma.obtener_rectangulos(self.forma_fisica)



    def obtener_rectangulos(principal:pygame.Rect)->dict:
        '''
        brief: obtiene una serie se superficies mas especificas sobre una general
        parametros: principal: superficie general
        return:
        '''
        diccionario = {}
        diccionario['principal'] = principal
        diccionario['top'] = pygame.Rect(principal.left, principal.top, principal.width, 6)
        diccionario['bottom'] = pygame.Rect(principal.left, principal.bottom-6, principal.width, 6)
        diccionario['left'] = pygame.Rect(principal.left, principal.top, 6, principal.height)
        diccionario['right'] = pygame.Rect(principal.right-2, principal.top, 6, principal.height)
        return diccionario



    def dibujar_objeto(lista_objeto, pantalla):
        '''
        brief: dibuja el objeto en pantalla
        parametros: lista_objeto: lista de objetos a dibujar. pantalla: donde se dibujara
        return:
        '''
        for plataforma in lista_objeto:
            pantalla.blit(plataforma.forma_visual, plataforma.forma_fisica)



    def crear_png_boss_final(self, pantalla, personaje, enemigo):
        '''
        brief: es la funcion de la plataforma si la cual colisiona con el
        personaje activa los disparos del boss final
        parametros: pantalla: donde se dibuja el objeto
        personaje: jugable; el protagonista. enemigo: el boss final
        return:
        '''
        if personaje.forma_fisica.colliderect(self.forma_fisica):
            enemigo.activacion = 'activado'
            pantalla.blit(self.forma_visual, self.forma_fisica)



    def funcionar_key_paso_lvl(self, personaje, pantalla, nivel, pausa_form):
        pantalla.blit(self.forma_visual, self.forma_fisica)
        if self.forma_fisica.colliderect(personaje.forma_fisica):
            personaje.nivel_actual = 'menu'
            if nivel == 1:
                pausa_form.lvl1_completed = True
            elif nivel == 2:
                pausa_form.lvl2_completed = True
            elif nivel == 3:
                pausa_form.lvl1_completed = True