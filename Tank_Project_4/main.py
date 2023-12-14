import pygame
import sys

# Загрузка классов
from Classes.Tank_class import Tank
from Classes.Enemy_class import Enemy
from Classes.Bullet_class import Bullet
from Classes.Coin_class import Coin

# Загрузка функций
from Menus.Evolve_menu import evolve_menu
from Menus.Main_menu import main_menu
from functions.Display_buttons import display_buttons
from Menus.Death_menu import death_menu_one, death_menu_two
from Menus.Pause_control_menu import control_menu_one, control_menu_two, pause_menu_two, pause_menu_one

# Инициализация библиотеки
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

# Размеры экрана
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

# загрузка звуковых эффектов
s = pygame.mixer.Sound('sfx/shoot.wav')
p = pygame.mixer.Sound('sfx/hit.wav')
b = pygame.mixer.Sound('sfx/button.wav')
coin_sound = pygame.mixer.Sound('sfx/coin_sound.wav')

# загрузка изображений танков
yellow_tank = pygame.transform.scale(pygame.image.load('images/tank_imgs/yellow_tank.png'), (64, 64))
red_tank = pygame.transform.scale(pygame.image.load('images/tank_imgs/red_tank.png'), (64, 64))
yellow_tank_3_bullets = pygame.transform.scale(pygame.image.load('images/tank_imgs/yellow_tank_3_bullets.png'), (64, 64))

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

# загрузка кнопок клавиатуры (для управления игроками)
w_button = pygame.transform.scale(pygame.image.load('images/button_images/w.png'), (96, 96))
a_button = pygame.transform.scale(pygame.image.load('images/button_images/a.png'), (96, 96))
s_button = pygame.transform.scale(pygame.image.load('images/button_images/s.png'), (96, 96))
d_button = pygame.transform.scale(pygame.image.load('images/button_images/d.png'), (96, 96))
space = pygame.transform.scale(pygame.image.load('images/button_images/space.png'), (384, 96))
up_button = pygame.transform.scale(pygame.image.load('images/button_images/up.png'), (96, 96))
down_button = pygame.transform.scale(pygame.image.load('images/button_images/down.png'), (96, 96))
right_button = pygame.transform.scale(pygame.image.load('images/button_images/right.png'), (96, 96))
left_button = pygame.transform.scale(pygame.image.load('images/button_images/left.png'), (96, 96))
q_button = pygame.transform.scale(pygame.image.load('images/button_images/q.png'), (96, 96))
m_button = pygame.transform.scale(pygame.image.load('images/button_images/m.png'), (96, 96))

# загрузка кнопок улучшений и 'эволюции' в одиночной игре
upgrade_up = pygame.transform.scale(pygame.image.load('images/button_images/upgrade_up.png'), (32, 32))
upgrade_down = pygame.transform.scale(pygame.image.load('images/button_images/upgrade_down.png'), (32, 32))
shield_up = pygame.image.load('images/other_imgs/shield_up.png')
shield_down = pygame.image.load('images/other_imgs/shield_down.png')
three_bullets_up = pygame.image.load('images/other_imgs/3_bullets_up.png')
three_bullets_down = pygame.image.load('images/other_imgs/3_bullets_down.png')

# загрузка других изображений
bullet_image = pygame.image.load('images/other_imgs/bullet.png')
heart_image = pygame.transform.scale(pygame.image.load('images/other_imgs/heart.png'), (32, 32))
missil_image = pygame.transform.scale(pygame.image.load('images/other_imgs/missil.png'), (32, 32))
coin_image = pygame.transform.scale(pygame.image.load('images/other_imgs/coin.png'), (32, 32))
enemy_1_image = pygame.transform.scale(pygame.image.load('images/other_imgs/enemy_1.png'), (64, 64))
enemy_2_image = pygame.image.load('images/other_imgs/enemy_2.png')
reload_image = pygame.transform.scale(pygame.image.load('images/other_imgs/reload.png'), (80, 16))
bullets_image = pygame.transform.scale(pygame.image.load('images/other_imgs/bullets.png'), (80, 16))
speed_image = pygame.transform.scale(pygame.image.load('images/other_imgs/speed.png'), (52, 16))
rotation_image = pygame.transform.scale(pygame.image.load('images/other_imgs/rotation.png'), (80, 16))
boss = pygame.image.load('images/other_imgs/boss.png')
coin_drop = pygame.image.load('images/other_imgs/coin_drop.png')
shield_1 = pygame.transform.scale(pygame.image.load('images/other_imgs/shield_1.png'), (128, 128))
shield_2 = pygame.transform.scale(pygame.image.load('images/other_imgs/shield_2.png'), (128, 128))
shield_3 = pygame.transform.scale(pygame.image.load('images/other_imgs/shield_3.png'), (128, 128))
shield_mask = pygame.mask.from_surface(shield_1)
shield_image = pygame.transform.scale(pygame.image.load('images/other_imgs/shield_image.png'), (32, 32))


# Создание врага 1-го типа в одиночной игре
def create_enemy_1():
    enemy_1 = Enemy(enemy_1_image, W, H)
    enemies.append(enemy_1)


# Создание врага 2-го типа в одиночной игре
def create_enemy_2():
    enemy_2 = Enemy(enemy_2_image, W, H)
    enemies.append(enemy_2)


# Создание танков для игры
tank_1 = Tank(100, 400, 90, yellow_tank)
tank_2 = Tank(900, 400, 90, red_tank)

# Списки, в которых будут храниться объекты классов Bullet, Enemy и Coin
bullets = []
enemies = []
money = []


# игровой цикл для одиночной игры
def game_for_one():

    click = False
    t = 0

    running = True
    while running:

        screen.fill(c_1)

        t += 1

        if t < 600:

            draw_text('Get ready! ' + str((600 - t) // 60) + ' s', font, c_2, screen, 400, 50)


        if 600 < t < 4200:
            draw_text('Wave 1: ' + str((4200 - t) // 60) + ' s', font, c_2, screen, 400, 50)

            if t % 120 == 0:
                tank_1.points += 10

            if t % 300 == 0:
                create_enemy_1()

        if t == 4200:
            evolve_menu(screen, clock, fps, three_bullets_down, b, tank_1, yellow_tank_3_bullets,
                three_bullets_up, shield_down, shield_up)

        if 4200 < t < 5100:
            draw_text('Cooldown: ' + str((5100 - t) // 60) + ' s', font, c_2, screen, 400, 50)

        if 5100 < t < 8700:
            draw_text('Wave 2: ' + str((8700 - t) // 60) + ' s', font, c_2, screen, 400, 50)

            if t % 120 == 0:
                tank_1.points += 10

            if t % 450 == 0:
                create_enemy_1()

            if t % 600 == 0:
                create_enemy_2()

        if 8700 < t < 8880:
            draw_text('Evolution time!', font, c_2, screen, 400, 50)

        if t == 8880:
            evolve_menu(screen, clock, fps, three_bullets_down, b, tank_1, yellow_tank_3_bullets,
                        three_bullets_up, shield_down, shield_up)

        if 8880 < t < 9780:
            draw_text('Get ready! ' + str((9780 - t) // 60) + ' s', font, c_2, screen, 400, 50)

        if 9780 < t < 13380:
            draw_text('Wave 3: ' + str((13380 - t) // 60) + ' s', font, c_2, screen, 400, 50)

            if t % 120 == 0:
                tank_1.points += 10

            if t % 200 == 0:
                create_enemy_1()

            if t % 300 == 0:
                create_enemy_2()

        if t > 13380:
            draw_text('Have fun!', font, c_2, screen, 400, 50)

            if t % 100 == 0 or t % 450 == 0:
                create_enemy_1()

            if t % 150 == 0:
                create_enemy_2()


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    if tank_1.lives > 0 and tank_1.missiles > 0:
                        if tank_1.fire_mode == 1:
                            s.play()
                            bullet = tank_1.fire(Bullet, tank_1, bullet_image)
                            bullets.append(bullet)
                        if tank_1.fire_mode == 3:
                            s.play()
                            b1, b2, b3 = tank_1.fire(Bullet, tank_1, bullet_image)
                            bullets.append(b1)
                            bullets.append(b2)
                            bullets.append(b3)
                if e.key == pygame.K_ESCAPE:
                    pause_menu_one(screen, c_1, one_player_down, b, control_menu_one, one_player_up, tank_1, game_for_one,
                                   two_players_down, control_menu_two, yellow_tank, bullets, money, enemies,
                                   two_players_up, clock, quit_down, quit_up, fps, retry_down, retry_up, continue_down,
                                   continue_up, main_menu_down, main_menu, main_menu_up, tank_2,
                                   red_tank, game_for_two, q_button,
                                   w_button, a_button, s_button, d_button, space, draw_text, font, c_2,
                                   up_button, left_button,
                                   down_button, right_button, m_button)
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True
            else:
                click = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            tank_1.rotate_r()
        if keys[pygame.K_a]:
            tank_1.rotate_l()
        if keys[pygame.K_w]:
            tank_1.move_forward()
        if keys[pygame.K_s]:
            tank_1.move_back()

        tank_1.reload()
        tank_1.render_coins(screen, coin_image, c_2, font, draw_text)

        for m in money:
            m.render(screen, coin_drop)
            m.hittest(tank_1.mask, tank_1, coin_sound)

        for enemy in enemies:
            if enemy.hittest(tank_1, shield_mask):
                p.play()
                enemies.remove(enemy)
            enemy.targetting(tank_1)
            enemy.render(screen)
            enemy.move()


        for bul in bullets:
            if bul.life >= 100:
                bullets.remove(bul)
            bul.hittest_enemy(enemies, p, Coin, money, coin_drop)
            bul.move()
            bul.render(screen, bullet_image)
            bul.hittest_tank_1(tank_1.mask, tank_1, p)

        tank_1.render_hearts_tank_1(screen, heart_image)
        tank_1.render_missiles_tank_1(screen, missil_image)
        tank_1.render_points(draw_text, font, c_2, screen)
        tank_1.render(screen, shield_1, shield_2, shield_3)
        tank_1.render_shield(screen, shield_image)

        display_buttons(screen, tank_1, speed_image, rotation_image, bullets_image, reload_image, coin_image, upgrade_down,
                    click, b, upgrade_up)

        if tank_1.lives == 0:
            running = False
            death_menu_one(screen, c_5, draw_text, tank_1, font, c_2, retry_down, retry_up,  yellow_tank, bullets, money,
                   enemies, c_1, one_player_down, b, control_menu_one, one_player_up, two_players_down, control_menu_two,
                   two_players_up, clock, quit_down, quit_up, fps, game_for_one, main_menu_down, main_menu, main_menu_up)



        clock.tick(fps)
        pygame.display.update()


# игровой цикл для кооперативного режима
def game_for_two():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if tank_1.lives > 0 and tank_1.missiles > 0:
                        s.play()
                        bullet = tank_1.fire(Bullet, tank_1, bullet_image)
                        bullets.append(bullet)
                if event.key == pygame.K_m:
                    if tank_2.lives > 0 and tank_2.missiles:
                        s.play()
                        bullet = tank_2.fire(Bullet, tank_1, bullet_image)
                        bullets.append(bullet)
                if event.key == pygame.K_ESCAPE:
                    pause_menu_two(screen, c_1, one_player_down, b, control_menu_one, one_player_up, tank_1,
                                   two_players_down, control_menu_two, yellow_tank, bullets, money, enemies,
                                   two_players_up, clock, quit_down, quit_up, fps, retry_down, retry_up, continue_down,
                                   continue_up, main_menu_down, main_menu, main_menu_up, tank_2, red_tank, game_for_two, q_button, game_for_one,
                                   w_button, a_button, s_button, d_button, space, draw_text, font, c_2,
                                   up_button, left_button,
                                   down_button, right_button, m_button)

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

        for bul in bullets:
            if bul.life >= 100:
                bullets.remove(bul)
            bul.move()
            bul.render(screen, bullet_image)
            bul.hittest_tank_1(tank_1.mask, tank_1, p)
            bul.hittest_tank_2(tank_2.mask, tank_2, p)

        tank_1.render(screen, shield_1, shield_2, shield_3)
        tank_2.render(screen, shield_1, shield_2, shield_3)
        tank_1.reload()
        tank_2.reload()
        tank_1.render_hearts_tank_1(screen, heart_image)
        tank_2.render_hearts_tank_2(screen, heart_image)
        tank_1.render_missiles_tank_1(screen, missil_image)
        tank_2.render_missiles_tank_2(screen, missil_image)
        tank_1.hittest(tank_2)

        if tank_1.lives == 0:
            running = False
            death_menu_two(screen, c_5, tank_1, retry_down, retry_up,  yellow_tank, bullets, money,
                           enemies, c_1, one_player_down, b, control_menu_one, one_player_up, two_players_down, control_menu_two,
                           two_players_up, clock, quit_down, quit_up, fps, main_menu_down, main_menu, main_menu_up,
                           tank_2, red_tank, game_for_two)
        if tank_2.lives == 0:
            running = False
            death_menu_two(screen, c_5, tank_1, retry_down, retry_up,  yellow_tank, bullets, money,
                           enemies, c_1, one_player_down, b, control_menu_one, one_player_up, two_players_down, control_menu_two,
                           two_players_up, clock, quit_down, quit_up, fps, main_menu_down, main_menu, main_menu_up,
                           tank_2, red_tank, game_for_two)

        clock.tick(fps)
        pygame.display.update()


# шрифт и функция для написания текста на экране
font = pygame.font.SysFont('None', 50)


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)



main_menu(screen, c_1, one_player_down, b, control_menu_one, one_player_up, two_players_down, control_menu_two,
              two_players_up,  clock, quit_down, quit_up, fps, tank_1, yellow_tank, bullets, money, enemies, tank_2,
              red_tank, game_for_two, q_button, game_for_one,
              w_button, a_button, s_button, d_button, space, draw_text, font, c_2,
              up_button, left_button,
              down_button, right_button, m_button)
