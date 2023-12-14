import pygame
from math import *

# Класс танка (игрока)


class Tank:

    def __init__(self, x, y, a, img):

        # Местоположение и угол поворота
        self.x = x
        self.y = y
        self.a = a

        # Местоположение реального центра танка
        self.rx = 0
        self.ry = 0
        self.w = 0
        self.h = 0
        self.img = img

        # Линейная и угловая скорость
        self.v = 2
        self.av = 2

        # Кол-во жизней, патронов, монет, очков
        self.lives = 3
        self.missiles = 6
        self.coins = 0
        self.points = 0

        # Объект типа mask, который совпадает с изображением танка в данный момент
        self.mask = pygame.mask.from_surface(self.img)

        # Индикатор независимого времени самого танка
        self.time = 0

        # Скорость перезарядки, макс. кол-во снарядов и индикаторы "прокачки"
        self.reload_speed = 1
        self.max_missiles = 6
        self.sp = 0
        self.rotsp = 0
        self.misl = 0
        self.reld = 0
        self.fire_mode = 1
        self.shield = 0
        self.defence = 0
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    # Экран имеет размеры 1024x768 (начало отсчёта расположено в верхнем левом углу экрана), размер танка 32x32. Деление на 57.3 - перевод угла поворота из градусов в радианы.
    # Когда танк находится вблизи границ экрана (992 = 1024-32 и 736 = 768-32) его дальнейшее движение в эти стороны должно прекратиться.
    # Движение танка вперёд
    def move_forward(self):
        if self.lives > 0:
            if 32 < self.x < 992:
                self.x += self.v * cos(self.a/57.3)
            elif self.x < 32:
                self.x += self.v
            elif self.x > 992:
                self.x -= self.v
            if 32 < self.y < 736:
                self.y -= self.v*sin(self.a/57.3)
            elif self.y < 32:
                self.y += self.v
            elif self.y > 736:
                self.y -= self.v

    # Движение танка назад
    def move_back(self):
        if self.lives > 0:
            if 32 < self.x < 992:
                self.x -= self.v * cos(self.a/57.3)
            elif self.x < 32:
                self.x += self.v
            elif self.x > 992:
                self.x -= self.v
            if 32 < self.y < 736:
                self.y += self.v * sin(self.a/57.3)
            elif self.y < 32:
                self.y += self.v
            elif self.y > 736:
                self.y -= self.v

    # Поворот танка в пространстве
    def rotate_r(self):
        if self.lives > 0:
            self.a -= self.av

    def rotate_l(self):
        if self.lives > 0:
            self.a += self.av

    # Перезарядка патронов
    def reload(self):
        self.time += 1
        if self.time % (240 - self.reld*15) == 0 and self.missiles < self.max_missiles:
            self.missiles += 1
        if self.time % 400 == 0 and self.defence == 1 and self.shield < 3:
            self.shield += 1
        if self.time == 3600:
            self.time = 0

    # Отображение картинки танка на экране
    def render(self, screen, img1, img2, img3):
        if self.lives > 0:
            rotated_img = pygame.transform.rotate(self.img, self.a)
            self.w = rotated_img.get_width() // 2
            self.h = rotated_img.get_height() // 2
            self.rx = self.x - self.w
            self.ry = self.y - self.h
            self.mask = pygame.mask.from_surface(rotated_img)
            screen.blit(rotated_img, (self.rx, self.ry))
            if self.shield == 1:
                rotated_shield = pygame.transform.rotate(img1, self.a)
                screen.blit(rotated_shield, (self.rx - self.w, self.ry - self.h))
            if self.shield == 2:
                rotated_shield = pygame.transform.rotate(img2, self.a)
                screen.blit(rotated_shield, (self.rx - self.w, self.ry - self.h))
            if self.shield == 3:
                rotated_shield = pygame.transform.rotate(img3, self.a)
                screen.blit(rotated_shield, (self.rx - self.w, self.ry - self.h))

    # Отображение кол-ва монет и значка монетки на экране в одиночном режиме (координата x зависит от кол-ва монет)
    def render_coins(self, screen, img, c_2, font, draw_text):
        if self.coins < 10:
            screen.blit(img, (30, 90))
        if 10 <= self.coins < 100:
            screen.blit(img, (55, 90))
        if 100 <= self.coins < 1000:
            screen.blit(img, (80, 90))
        if 1000 <= self.coins < 10000:
            screen.blit(img, (105, 90))
        draw_text(str(self.coins), font, c_2, screen, 8, 88)

        draw_text('10', font, c_2, screen, 905, 268)

    # Отображение на экране кол-ва патронов 1-го и 2-го танков (Так как патроны должны отображаться в определённых
    # частях экрана, эти методы разбиты на отдельные для каждого танка)
    def render_missiles_tank_1(self, screen, img):
        if self.lives > 0:
            for i in range(self.missiles):
                screen.blit(img, (i*32, 50))

    def render_missiles_tank_2(self, screen, img):
        if self.lives > 0:
            for i in range(self.missiles):
                screen.blit(img, (830 + i*32, 50))

    # Аналогично, отображение на экране кол-ва жизней каждого танка
    def render_hearts_tank_1(self, screen, img):
        for i in range(self.lives):
            screen.blit(img, (5 + i*32, 10))

    def render_shield(self, screen, img):
        for i in range(self.shield):
            screen.blit(img, (101 + i*32, 10))

    def render_hearts_tank_2(self, screen, img):
        for i in range(self.lives):
            screen.blit(img, (930 + i*32, 10))

    # Стрельба (создание и добавление в список нового патрона)
    def fire(self, class_1, tank_1, bullet_image):
        if self.lives > 0:
            if self.fire_mode == 1:
                if self.missiles != 0:
                    self.missiles -= 1
                    bullet = class_1(self.x, self.y, self.a, tank_1, bullet_image)
                    return bullet
            if self.fire_mode == 3:
                if self.missiles != 0:
                    self.missiles -= 1
                    b1, b2, b3 = (class_1(self.x, self.y, self.a-3, tank_1, bullet_image),
                                  class_1(self.x, self.y, self.a+3, tank_1, bullet_image),
                                  class_1(self.x, self.y, self.a, tank_1, bullet_image))
                    return b1, b2, b3

    # Проверка на столкновение с объектом
    def hittest(self, obj):
        if self.mask.overlap(obj.mask, (obj.rx - self.rx, obj.ry - self.ry)):
            self.lives, obj.lives = 0, 0

    # Отображение кол-ва очков в одиночном режиме
    def render_points(self, draw_text, font, c_2, screen):
        draw_text(str(self.points), font, c_2, screen, 900, 20)

    def set_zero(self, x, y, a, img, bullets, money, enemies):
        self.x = x
        self.y = y
        self.a = a
        self.rx = 0
        self.ry = 0
        self.v = 2
        self.av = 2
        self.lives = 3
        self.missiles = 6
        self.coins = 0
        self.points = 0
        self.mask = pygame.mask.from_surface(self.img)
        self.time = 0
        self.reload_speed = 1
        self.max_missiles = 6
        self.sp = 0
        self.rotsp = 0
        self.misl = 0
        self.reld = 0
        self.img = img
        self.fire_mode = 1
        self.shield = 0
        self.defence = 0
        bullets.clear()
        money.clear()
        enemies.clear()
