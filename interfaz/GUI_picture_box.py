import pygame
from pygame.locals import *
from interfaz.GUI_widget import *

class PictureBox(Widget):
    def __init__(self, screen, x,y,w,h, path_image):
        super().__init__(screen, x,y,w,h)
        
        self.esta_prendido = False
        
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))

        self._slave = aux_image
        
        self.render()



    def render(self):
        self.slave_rect = self._slave.get_rect()

        self.slave_rect.x = self._x
        self.slave_rect.y = self._y



    def update(self, lista_eventos):
        self.draw()



    def set_imagen(self, imagen: pygame.Surface):
        self._slave = imagen