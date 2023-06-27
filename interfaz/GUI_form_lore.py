import pygame
from pygame.locals import *
from interfaz.GUI_button_image import *
from interfaz.GUI_form import *
from interfaz.GUI_label import *
from interfaz.GUI_slider import *
from interfaz.GUI_label import *
from interfaz.GUI_widget import *
from interfaz.GUI_picture_box import *
from interfaz.GUI_checkbox import *

class Form_lore (Form):
    def __init__(self, screen, x, y, w, h, color_background, 
                color_border="Black", border_size=-1,active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.flag_play = True
        self.jugar = False
        self.menu = False

        self.btn_play = Button_Image(self._slave, x,y, 505,410,
                                        200,75, "interfaz/base.png", 
                                        self.btn_play_game, 'No entiendo nada')

        self.lista_widgets.append(self.btn_play)

        self.render()



    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)



    def render(self):
        self._slave.fill(self._color_background)



    def btn_play_game(self):
        if self.flag_play:
            self.jugar = True
            self.menu = True
            self.flag_play = False
        self.flag_play = True


    def btn_MENU(self):
        if self.flag_play:
            
            self.flag_play = False
        self.flag_play = True

