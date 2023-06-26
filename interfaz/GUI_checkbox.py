import pygame
from pygame.locals import *
from interfaz.GUI_widget import *

FPS = 18

class CheckBox(Widget):
    def __init__(self, screen,master_x,master_y, x,y,w,h, path_image_on, path_image_off, ):
        super().__init__(screen, x,y,w,h)

        self.esta_prendido = False
        self._master_x = master_x
        self._master_y = master_y
        
        aux_image_on = pygame.image.load(path_image_on)
        aux_image_on = pygame.transform.scale(aux_image_on,(w,h))
        self.image_on = aux_image_on

        aux_image_off = pygame.image.load(path_image_off)
        aux_image_off = pygame.transform.scale(aux_image_off,(w,h))
        self.image_off = aux_image_off

        self._slave = self.image_off

        self.isclicked = False
        self.contador_click = 0

        self.sfx_bool = True

        self.render()



    def render(self):
        self.slave_rect = self._slave.get_rect()

        self.slave_rect.x = self._x
        self.slave_rect.y = self._y
        
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self._master_x
        self.slave_rect_collide.y += self._master_y



    def update(self, lista_eventos):
        self.isclicked = False
        if self.contador_click > FPS/2:
            for evento in lista_eventos:
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.slave_rect_collide.collidepoint(evento.pos):
                        self.esta_prendido = not self.esta_prendido
                        self.contador_click = 0
                        self.sfx_bool = not self.sfx_bool
        else:
            self.contador_click += 1

        if self.esta_prendido:
            self._slave = self.image_on
        else:
            self._slave = self.image_off

        self.draw()



    def get_esta_prendido(self):
        return self.esta_prendido