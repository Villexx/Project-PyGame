#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pygame as pg
from pygame.font import Font
from pygame import Surface, Rect
from project.code.Const import WIN_WIDTH
from project.code.Const import MENU_OPTION
from project.code.Const import COLOR_WHITE
from project.code.Const import COLOR_YELLOW
from project.code.Const import COLOR_ORANGE


class Menu:
    def __init__(self, window):
        self.window = window

        # -----------------------------------------------------------------------------------------------

        # Definindo caminho da imagem
        img = os.path.join(os.path.dirname(__file__), '..', 'asset', 'Menu.png')
        img = os.path.normpath(img)

        # Carregando a imagem
        self.surf = pg.image.load(img)
        self.rect = self.surf.get_rect(left=0, top=0)

    # -----------------------------------------------------------------------------------------------
    # MENU

    def run(self, ):
        menu_option = 0
        # music
        menu_sound = os.path.join(os.path.dirname(__file__), '..', 'asset', 'Menu.wav')
        menu_sound = os.path.normpath(menu_sound)
        pg.mixer.music.load(menu_sound)
        pg.mixer.music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(60, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            # display
            pg.display.flip()

            # Check of all events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN: # tecla para baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pg.K_UP: # para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pg.K_RETURN: # ENTER
                        return MENU_OPTION[menu_option]

    # Formatação do menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
