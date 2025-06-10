#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pygame as pg
from pygame.font import Font
from pygame import Surface, Rect
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Const import COLOR_ORANGE
from code.Const import COLOR_WRITE
from code.Const import MENU_OPTION

class Menu:
    def __init__(self, window):
        self.window = window
        
# -----------------------------------------------------------------------------------------------

         # Definindo caminho da imagam
        img = os.path.join(os.path.dirname(__file__), '..', 'asset', 'Menu.png')
        img = os.path.normpath(img)

        # Carregando a imagem
        self.surf = pg.image.load(img)
        self.rect = self.surf.get_rect(left=0, top=0)        
        
# -----------------------------------------------------------------------------------------------
    # MENU
    def run(self, ):
        #music
        menu_sound = os.path.join(os.path.dirname(__file__), '..', 'asset', 'Menu.wav')
        menu_sound = os.path.normpath(menu_sound)
        pg.mixer.music.load(menu_sound)
        pg.mixer.music.play(-1)
        
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, "Mountain", (COLOR_ORANGE), ((WIN_WIDTH / 2), 70))
            self.menu_text(60, "Shooter", (COLOR_ORANGE), ((WIN_WIDTH / 2), 120))
            
            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], (COLOR_WRITE), ((WIN_WIDTH / 2), 200 + 25 * i))

            #display
            pg.display.flip()
            
            # Check of all events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit() # Close Window
                    quit()    # end pygame

    # Formatação do menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)