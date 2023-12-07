import pygame
from math import *
import sys
import random

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

W, H = 1024, 768
screen = pygame.display.set_mode((W, H))

# Цвета для игры
c_1 = (78, 205, 196)
c_2 = (26, 83, 92)
c_3 = (247, 255, 247)
c_4 = (255, 107, 107)
c_5 = (255, 230, 109)


# ФПС и часы для отсчёта времени
fps = 60
clock = pygame.time.Clock()


# Класс танка (игрока)
class Tank:
    def __init__(self, x, y, a):
        self.x = x
        self.y = y
        self.a = a
        self.v = 2
        self.rx = 0
        self.ry = 0
        self.lives = 3
        self.missiles = 6
        self.time = 0
        self.mask = pygame.mask.from_surface(green_tank)
        self.coins = 0
        self.points = 0
        self.av = 2
        self.max_missiles = 6
        self.sp = 0
        self.rotsp = 0
        self.misl = 0


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

    def move_back(self):
        if self.lives > 0:
            if 0 < self.x < 1024:
                self.x -= self.v * cos(self.a/57.3)
            elif self.x < 0:
                self.x += self.v
            elif self.x > 1024:
                self.x -= self.v
            if 0 < self.y < 768:
                self.y += self.v * sin(self.a/57.3)
            elif self.y < 0:
                self.y += self.v
            elif self.y > 768:
                self.y -= self.v

    def rotate_r(self):
        if self.lives > 0:
            self.a -= self.av

    def rotate_l(self):
        if self.lives > 0:
            self.a += self.av

    def render(self, img):
        if self.lives > 0:
            rotated_img = pygame.transform.rotate(img, self.a)
            screen.blit(rotated_img, (self.x - rotated_img.get_width() // 2, self.y - rotated_img.get_height() // 2))
            self.mask = pygame.mask.from_surface(rotated_img)
            self.rx = self.x - rotated_img.get_width() // 2
            self.ry = self.y - rotated_img.get_height() // 2
            if self.time < 200:
                self.time += 1
            else:
                self.time = 0

    def render_coins(self):
        if self.coins < 10:
            screen.blit(coin_image, (30, 90))
        if 10 <= self.coins < 100:
            screen.blit(coin_image, (55, 90))
        if 100 <= self.coins < 1000:
            screen.blit(coin_image, (80, 90))
        if 1000 <= self.coins < 10000:
            screen.blit(coin_image, (105, 90))
        draw_text(str(self.coins), font, c_2, screen, 8, 88)

    def render_missiles_tank_1(self):
        if self.lives > 0:
            for i in range(self.missiles):
                screen.blit(missil_image, (i*32, 50))

    def render_missiles_tank_2(self):
        if self.lives > 0:
            for i in range(self.missiles):
                screen.blit(missil_image, (830 + i*32, 50))

    def render_hearts_tank_1(self):
        for i in range(self.lives):
            screen.blit(heart_image, (5 + i*32, 10))
        if self.lives <= 0:
            rotated_img = pygame.transform.rotate(green_tank_broken, self.a)
            screen.blit(rotated_img, (self.x - rotated_img.get_width() // 2, self.y - rotated_img.get_height() // 2))


    def render_hearts_tank_2(self):
        for i in range(self.lives):
            screen.blit(heart_image, (930 + i*32, 10))
        if self.lives <= 0:
            rotated_img = pygame.transform.rotate(brown_tank_broken, self.a)
            screen.blit(rotated_img, (self.x - rotated_img.get_width() // 2, self.y - rotated_img.get_height() // 2))

    def render_points(self):
        draw_text(str(self.points), font, c_2, screen, 900, 20)



# загрузка звуковых эффектов
s = pygame.mixer.Sound('sfx\\shoot.wav')
p = pygame.mixer.Sound('sfx/hit.wav')
b = pygame.mixer.Sound('sfx/button.wav')


# загрузка изображений танков
green_tank = pygame.transform.scale(pygame.image.load('images/tank_imgs/green_tank.png'), (64, 64))
green_tank_broken = pygame.transform.scale(pygame.image.load('images/tank_imgs/green_tank_broken.png'), (64, 64))
brown_tank = pygame.transform.scale(pygame.image.load('images/tank_imgs/brown_tank.png'), (64, 64))
brown_tank_broken = pygame.transform.scale(pygame.image.load('images/tank_imgs/brown_tank_broken.png'), (64, 64))

# загрузка изображений кнопок главного меню
one_player_up = pygame.transform.scale(pygame.image.load('images/button_images/1_player_up.png'), (384, 96))
one_player_down = pygame.transform.scale(pygame.image.load('images/button_images/1_player_down.png'), (384, 96))
two_players_up = pygame.transform.scale(pygame.image.load('images/button_images/2_players_up.png'), (384, 96))
two_players_down = pygame.transform.scale(pygame.image.load('images/button_images/2_players_down.png'), (384, 96))
quit_up = pygame.transform.scale(pygame.image.load('images/button_images/quit_up.png'), (384, 96))
quit_down = pygame.transform.scale(pygame.image.load('images/button_images/quit_down.png'), (384, 96))

# загрузка изображений кнопок меню смерти/паузы в одиночной игре
retry_up = pygame.transform.scale(pygame.image.load('images/button_images/retry_up.png'), (384, 96))
retry_down = pygame.transform.scale(pygame.image.load('images/button_images/retry_down.png'), (384, 96))
main_menu_up = pygame.transform.scale(pygame.image.load('images/button_images/main_menu_up.png'), (384, 96))
main_menu_down = pygame.transform.scale(pygame.image.load('images/button_images/main_menu_down.png'), (384, 96))
continue_up = pygame.transform.scale(pygame.image.load('images/button_images/continue_up.png'), (384, 96))
continue_down = pygame.transform.scale(pygame.image.load('images/button_images/continue_down.png'), (384, 96))
w_button = pygame.transform.scale(pygame.image.load('images/button_images/w.png'), (96, 96))
a_button = pygame.transform.scale(pygame.image.load('images/button_images/a.png'), (96, 96))
s_button = pygame.transform.scale(pygame.image.load('images/button_images/s.png'), (96, 96))
d_button = pygame.transform.scale(pygame.image.load('images/button_images/d.png'), (96, 96))
space = pygame.transform.scale(pygame.image.load('images/button_images/space.png'), (384, 96))

# загрузка других изображений
bullet_image = pygame.image.load('images/other_imgs/bullet.png')
heart_image = pygame.transform.scale(pygame.image.load('images/other_imgs/heart.png'), (32, 32))
missil_image = pygame.transform.scale(pygame.image.load('images/other_imgs/missil.png'), (32, 32))
coin_image = pygame.transform.scale(pygame.image.load('images/other_imgs/coin.png'), (32, 32))
enemy_1_image = pygame.image.load('images/other_imgs/enemy_1.png')
reload_image = pygame.transform.scale(pygame.image.load('images/other_imgs/reload.png'), (80, 16))
bullets_image = pygame.transform.scale(pygame.image.load('images/other_imgs/bullets.png'), (80, 16))
speed_image = pygame.transform.scale(pygame.image.load('images/other_imgs/speed.png'), (52, 16))
rotation_image = pygame.transform.scale(pygame.image.load('images/other_imgs/rotation.png'), (80, 16))
cost_10 = pygame.transform.scale(pygame.image.load('images/other_imgs/cost_10.png'), (32, 20))



tank_1 = Tank(100, 400, 90)
tank_2 = Tank(900, 400, 90)

# игровой цикл для одиночной игры
def game_for_one():

    click = False
    t = 0

    running = True
    while running:

        t += 1

        if t % 60 == 0:
            tank_1.points += 10

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    if tank_1.lives > 0:
                        s.play()
                if e.key == pygame.K_ESCAPE:
                    pause_menu_one()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            tank_1.rotate_r()
        if keys[pygame.K_a]:
            tank_1.rotate_l()
        if keys[pygame.K_w]:
            tank_1.move_forward()
        if keys[pygame.K_s]:
            tank_1.move_back()

        screen.fill(c_1)

#########################################################################
        mx, my = pygame.mouse.get_pos()

        screen.blit(
            pygame.transform.scale(pygame.image.load('images/scale_imgs/scale_' + str(tank_1.sp) + '.png'), (96, 32)),
            (900, 80)
        )
        screen.blit(
            pygame.transform.scale(pygame.image.load('images/scale_imgs/scale_' + str(tank_1.rotsp) + '.png'), (96, 32)),
            (900, 130)
        )
        screen.blit(
            pygame.transform.scale(pygame.image.load('images/scale_imgs/scale_' + str(tank_1.misl) + '.png'), (96, 32)),
            (900, 180)
        )

        screen.blit(speed_image, pygame.Rect(900, 64, 52, 8))
        screen.blit(rotation_image, pygame.Rect(896, 114, 80, 8))
        screen.blit(bullets_image, pygame.Rect(891, 164, 80, 8))
        screen.blit(cost_10, pygame.Rect(910, 225, 32, 20))
        screen.blit(coin_image, pygame.Rect(950, 220, 32, 32))


####################################################################

        tank_1.render_coins()
        tank_1.render_hearts_tank_1()
        tank_1.render_missiles_tank_1()
        tank_1.render_points()
        tank_1.render(green_tank)

        if tank_1.lives == 0:
            running = False
            death_menu_one()

        clock.tick(fps)
        pygame.display.update()


# игровой цикл 1 на 1
def game_for_two():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    s.play()
                if event.key == pygame.K_m:
                    s.play()
                if event.key == pygame.K_ESCAPE:
                    pause_menu_two()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            tank_1.rotate_r()
        if keys[pygame.K_a]:
            tank_1.rotate_l()
        if keys[pygame.K_w]:
            tank_1.move_forward()
        if keys[pygame.K_s]:
            tank_1.move_back()
        if keys[pygame.K_RIGHT]:
            tank_2.rotate_r()
        if keys[pygame.K_LEFT]:
            tank_2.rotate_l()
        if keys[pygame.K_UP]:
            tank_2.move_forward()
        if keys[pygame.K_DOWN]:
            tank_2.move_back()

        screen.fill(c_1)

        tank_1.render(green_tank)
        tank_2.render(brown_tank)
        tank_1.render_hearts_tank_1()
        tank_2.render_hearts_tank_2()
        tank_1.render_missiles_tank_1()
        tank_2.render_missiles_tank_2()

        if tank_1.lives == 0:
            running = False
            death_menu_two()
        if tank_2.lives == 0:
            running = False
            death_menu_two()

        clock.tick(fps)
        pygame.display.update()


# шрифт и функция для написания текста на экране
font = pygame.font.SysFont('None', 50)


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


# главное меню
def main_menu():

    while True:
        screen.fill(c_1)
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        button_arcade = pygame.Rect(50, 100, 384, 96)
        button_play_two = pygame.Rect(50, 250, 384, 96)
        button_quit = pygame.Rect(50, 400, 384, 96)

        mx, my = pygame.mouse.get_pos()
        if button_arcade.collidepoint((mx, my)):
            screen.blit(one_player_down, button_arcade)
            if click:
                b.play()
                control_menu_one()
        else:
            screen.blit(one_player_up, button_arcade)
        if button_play_two.collidepoint((mx, my)):
            screen.blit(two_players_down, button_play_two)
            if click:
                tank_1.x = 50
                tank_1.y = 700
                tank_1.lives = 3
                tank_1.coins = 0
                tank_1.points = 0
                tank_1.a = 90
                tank_2.x = 950
                tank_2.y = 150
                tank_2.lives = 3
                tank_2.coins = 0
                tank_2.points = 0
                tank_2.a = 270
                b.play()
                game_for_two()
        else:
            screen.blit(two_players_up, button_play_two)
        if button_quit.collidepoint((mx, my)):
            screen.blit(quit_down, button_quit)
            if click:
                b.play()
                pygame.time.delay(100)
                pygame.quit()
                sys.exit()
        else:
            screen.blit(quit_up, button_quit)

        clock.tick(fps)
        pygame.display.update()


def control_menu_one():
    while True:
        screen.fill(c_1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tank_1.x = 500
                    tank_1.y = 400
                    tank_1.lives = 5
                    tank_1.coins = 0
                    tank_1.points = 0
                    tank_1.a = 90
                    tank_1.sp = 0
                    tank_1.rotsp = 0
                    tank_1.misl = 0
                    b.play()
                    game_for_one()

        screen.blit(w_button, (250, 200))
        screen.blit(a_button, (100, 350))
        screen.blit(s_button, (250, 350))
        screen.blit(d_button, (400, 350))
        screen.blit(space, (400, 500))

        draw_text('W - move forward', font, c_2, screen, 600, 200)
        draw_text('S - move back', font, c_2, screen, 600, 250)
        draw_text('A, D - rotate', font, c_2, screen, 600, 300)
        draw_text('Space - shoot', font, c_2, screen, 600, 350)
        draw_text('Escape - pause', font, c_2, screen, 600, 400)
        draw_text('Press to start', font, c_2, screen, 470, 620)

        clock.tick(fps)
        pygame.display.update()


# меню паузы для одного игрока
def pause_menu_one():
    while True:

        screen.fill(c_1)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        button_retry = pygame.Rect(340, 350, 384, 96)
        button_continue = pygame.Rect(340, 200, 384, 96)
        button_main_menu = pygame.Rect(340, 500, 384, 96)

        mx, my = pygame.mouse.get_pos()
        if button_retry.collidepoint((mx, my)):
            screen.blit(retry_down, button_retry)
            if click:
                tank_1.x = 500
                tank_1.y = 400
                tank_1.lives = 5
                tank_1.coins = 0
                tank_1.points = 0
                tank_1.a = 90
                tank_1.sp = 0
                tank_1.rotsp = 0
                tank_1.misl = 0
                b.play()
                game_for_one()
        else:
            screen.blit(retry_up, button_retry)
        if button_continue.collidepoint((mx, my)):
            screen.blit(continue_down, button_continue)
            if click:
                b.play()
                game_for_one()
        else:
            screen.blit(continue_up, button_continue)
        if button_main_menu.collidepoint((mx, my)):
            screen.blit(main_menu_down, button_main_menu)
            if click:
                b.play()
                main_menu()
        else:
            screen.blit(main_menu_up, button_main_menu)

        clock.tick(fps)
        pygame.display.update()

def pause_menu_two():
    while True:

        screen.fill(c_1)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        button_retry = pygame.Rect(340, 350, 384, 96)
        button_continue = pygame.Rect(340, 200, 384, 96)
        button_main_menu = pygame.Rect(340, 500, 384, 96)

        mx, my = pygame.mouse.get_pos()
        if button_retry.collidepoint((mx, my)):
            screen.blit(retry_down, button_retry)
            if click:
                tank_1.x = 50
                tank_1.y = 700
                tank_1.lives = 3
                tank_1.coins = 0
                tank_1.points = 0
                tank_1.a = 90
                tank_2.x = 950
                tank_2.y = 150
                tank_2.lives = 3
                tank_2.coins = 0
                tank_2.points = 0
                tank_2.a = 270
                b.play()
                game_for_two()
        else:
            screen.blit(retry_up, button_retry)
        if button_continue.collidepoint((mx, my)):
            screen.blit(continue_down, button_continue)
            if click:
                b.play()
                game_for_two()
        else:
            screen.blit(continue_up, button_continue)
        if button_main_menu.collidepoint((mx, my)):
            screen.blit(main_menu_down, button_main_menu)
            if click:
                b.play()
                main_menu()
        else:
            screen.blit(main_menu_up, button_main_menu)

        clock.tick(fps)
        pygame.display.update()


main_menu()
