#!/usr/bin/python
# -*- coding: utf-8 -*-
from ctypes import windll
import pygame as pg
from project.code.Entity import Entity
from project.code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self. game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        print("Entidades carregadas:", len(self.entity_list))

    def run(self):
        clock = pg.time.Clock()
        while True:
            self.window.fill((0, 0, 0))
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pg.display.flip()
            clock.tick(60)  # 60 FPS
            pg.draw.rect(self.window, (255, 0, 0), (0, 0, 50, 50))  # retângulo vermelho
