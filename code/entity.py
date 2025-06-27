#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import pygame as pg
import os

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, '..', 'asset', name + '.png')
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Imagem '{name}.png' não encontrada no caminho: {image_path}")
        self.surf = pg.image.load(image_path)
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod #decorator
    def move(self, ):
        pass


# base_path = os.path.dirname(__file__)
# image_path = os.path.join(base_path, '..', 'asset', name + '.png')
# if not os.path.exists(image_path):
#     raise FileNotFoundError(f"Imagem '{name}.png' não encontrada no caminho: {image_path}")
# self.surf = pg.image.load(image_path)