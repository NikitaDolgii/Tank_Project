import pygame
from math import *


class Bullet:
    def __init__(self, x, y, a, tank_1, bullet_image):
        self.x = x
        self.y = y
        self.v = tank_1.v + 10
        self.a = a
        self.vx = self.v * cos(self.a/57.3)
        self.vy = self.v * sin(self.a/57.3)
        self.mask = pygame.mask.from_surface(bullet_image)
        self.life = 0
        self.rect = pygame.Rect(self.x-4, self.y-4, 8, 8)

    def render(self, screen, bullet_image):
        self.rect = pygame.Rect(self.x, self.y, 3, 3)
        self.mask = pygame.mask.from_surface(bullet_image)
        screen.blit(bullet_image, (self.x, self.y))
        self.life += 1

    def hittest_tank_1(self, obj, tank_1, p):
        if self.mask.overlap(obj, (tank_1.rx - self.x, tank_1.ry - self.y)) and self.life > 3:
            self.x, self.y = 10000, 10000
            p.play()
            tank_1.lives -= 1

    def hittest_tank_2(self, obj, tank_2, p):
        if self.mask.overlap(obj, (tank_2.rx - self.x, tank_2.ry - self.y)) and self.life > 3:
            self.x, self.y = 10000, 10000
            p.play()
            tank_2.lives -= 1

    def hittest_enemy(self, enemies, p, class_0, money, coin_drop):
        for en in enemies:
            if self.mask.overlap(en.mask, (en.x - self.x, en.y - self.y)):
                p.play()
                coin = class_0(en.x, en.y, coin_drop)
                money.append(coin)
                enemies.remove(en)
                self.life = 150



    def move(self):
        self.x += self.vx
        self.y -= self.vy
        self.a = 1
