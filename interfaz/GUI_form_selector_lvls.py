import pygame
from pygame.locals import *
from interfaz.GUI_button_image import *
from interfaz.GUI_form import *
from interfaz.GUI_label import *
from interfaz.GUI_slider import *
from interfaz.GUI_label import *
from interfaz.GUI_widget import *
from interfaz.GUI_picture_box import *


class Form_Manejador_Lvls (Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1,active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True

        self.nivel_actual = 'menu'
        
        self.lvl1_completed = False
        self.lvl2_completed = False
        self.lvl3_completed = False

        self.picture_box = PictureBox(self._slave, 250, 80, 750,
                                    500, "interfaz/imagen_interfaz.png")
        self.btn_lvl1 = Button_Image(self._slave, x,y, 525,130, 185,75, 
                            "interfaz/base.png", self.btn_play_lvl1, 'No entiendo nada')
        self.btn_lvl2_red = Button_Image(self._slave, x,y, 525,230, 185,75, 
                                        "interfaz/base_roja.png", 
                                    self.btn_msj_incompleted, 'No entiendo nada')
        self.btn_lvl3_red = Button_Image(self._slave, x,y, 525,330, 185,75, 
                                "interfaz/base_roja.png", self.btn_msj_incompleted,
                                'No entiendo nada')
        self.btn_quit = Button_Image(self._slave, x,y, 355,435, 50,50, 
                                    "interfaz/home.png",
                                    self.btn_play_menu_principal, 'No entiendo nada')

        self.btn_lvl2_gray = Button_Image(self._slave, x,y, 525,230, 
                                        185,75, "interfaz/base.png", 
                                        self.btn_play_lvl2, 'No entiendo nada')
        self.btn_lvl3_gray = Button_Image(self._slave, x,y, 525,330, 185,75,
                                    "interfaz/base.png", self.btn_play_lvl3, 'No entiendo nada')

        self.label_volumen = Label(self._slave, 700,450, 40,40, '20%',
                                    'Comic Sans', 15, 'White', "interfaz/Table.png")
        self.slider_volumen = Slider(self._slave, x,y, 480,460, 200,15,
                                    self.volumen, 'Blue', 'White')

        self.lista_widgets.append(self.picture_box)
        self.lista_widgets.append(self.btn_lvl1)
        self.lista_widgets.append(self.btn_lvl2_red)
        self.lista_widgets.append(self.btn_lvl3_red)
        self.lista_widgets.append(self.btn_quit)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_lvl3_gray)

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



    def cambiar_boton(self):
        if self.lvl1_completed == True:
            self.lista_widgets.append(self.btn_lvl2_gray)
        if self.lvl2_completed == True:
            self.lista_widgets.append(self.btn_lvl3_gray)



    def render(self):
        self._slave.fill(self._color_background)



    def btn_play_menu_principal(self):
        if self.flag_play:
            self.nivel_actual = 'menu_principal'
            self.flag_play = False
        self.flag_play = True



    def btn_play_menu(self):
        if self.flag_play:
            self.nivel_actual = 'menu'
            self.flag_play = False
        self.flag_play = True


    def btn_play_lvl1(self):
        pygame.mixer.music.stop() 
        if self.flag_play:
            self.nivel_actual = 'uno'
            self.flag_play = False
        self.flag_play = True


    def btn_play_lvl2(self):
            pygame.mixer.music.stop() 
            if self.flag_play:
                self.nivel_actual = 'dos'
                self.flag_play = False
            self.flag_play = True



    def btn_play_lvl3(self):
            pygame.mixer.music.stop() 
            if self.flag_play:
                self.nivel_actual = 'tres'
                self.flag_play = False
            self.flag_play = True



    def btn_msj_incompleted(self):
        print("nivel no disponible")



    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)