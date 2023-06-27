import pygame
from pygame.locals import *

from interfaz.GUI_button_image import *
from interfaz.GUI_form import *
from interfaz.GUI_label import *
from interfaz.GUI_slider import *
from interfaz.GUI_label import *
from interfaz.GUI_widget import *
from interfaz.GUI_picture_box import *
from configuraciones import *


class Form_Menu_Principal (Form):
    def __init__(self, screen, x, y, w, h, 
                color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True

        self.nivel_actual = 'menu_principal'


        self.label_volumen = Label(self._slave, 700,400, 40,40, '20%', 
                                'Comic Sans', 15, 'Black', "interfaz/base.png")
        self.slider_volumen = Slider(self._slave, x,y, 480,410, 200,15,
                                    self.volumen, 'Gray', 'White')

        self.picture_box = PictureBox(self._slave, 250, 80, 750, 500,
                                    "interfaz/imagen_interfaz.png")
        self.btn_niveles = Button_Image(self._slave, x,y, 470,220, 285,150,
                                        "interfaz/base.png", 
                                    self.btn_play_selector_lvls, 'No entiendo nada')
        self.btn_quit = Button_Image(self._slave, x,y, 580,465,
                                    50,50, "interfaz/home.png", self.btn_play_quit, 'No entiendo nada')

        self.lista_widgets.append(self.picture_box)
        self.lista_widgets.append(self.btn_niveles)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_quit)

        self.render()



    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)



    def render(self):
        self._slave.fill(self._color_background)



    def btn_play_menu(self, param):
        self.end_dialog()



    def btn_play_selector_lvls(self):
        if self.flag_play:
            self.nivel_actual = 'selector'
            self.flag_play = False
        self.flag_play = True



    def btn_play_quit(self):
        if self.flag_play:
            self.nivel_actual = 'quit'
            self.flag_play = False
        self.flag_play = True



    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)