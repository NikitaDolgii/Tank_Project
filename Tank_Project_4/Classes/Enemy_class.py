import pygame
import random
from math import *


# Класс врагов, атакующих игрока в одиночном режиме
class Enemy:
    def __init__(self, img, W, H):
        self.x, self.y = random.choice(
            [(-50, random.randint(0, H)),
                (W + 50, random.randint(0, H)),
                (random.randint(0, W), -50),
                (random.randint(0, W), H + 50)]
        )
        self.a = 1
        self.v = 2
        self.vx = self.v * cos(self.a / 57.3)
        self.vy = self.v * sin(self.a / 57.3)
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def render(self, screen):
        self.mask = pygame.mask.from_surface(self.img)
        screen.blit(self.img, (self.x, self.y))

    def targetting(self, tank_1):
        if tank_1.rx > self.x:
            self.a = atan(-(tank_1.ry - self.y) / (tank_1.rx - self.x)) * 57.3 + 90
        elif tank_1.rx < self.x:
            self.a = atan(-(tank_1.ry - self.y) / (tank_1.rx - self.x)) * 57.3 + 270
        else:
            self.a = atan((tank_1.ry - self.y) / (tank_1.rx - self.x + 0.00001)) * 57.3 + 270

    def move(self):
        self.vx = self.v * sin(self.a / 57.3)
        self.vy = self.v * cos(self.a / 57.3)
        self.x += self.vx
        self.y += self.vy

    def hittest(self, tank_1, shield_mask):
        if tank_1.shield > 0:
            if self.mask.overlap(shield_mask, (tank_1.rx - tank_1.w - self.x, tank_1.ry - tank_1.h - self.y)):
                tank_1.shield -= 1
                return True
        elif self.mask.overlap(tank_1.mask, (tank_1.rx - self.x, tank_1.ry - self.y)):
            tank_1.lives -= 1
            return True
