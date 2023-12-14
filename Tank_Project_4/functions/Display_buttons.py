import pygame


# Функция, отображающая кнопки улучшений на экране в одиночной игре
def display_buttons(screen, tank_1, speed_image, rotation_image, bullets_image, reload_image, coin_image, upgrade_down,
                    click, b, upgrade_up):

    # Расположение и размер кнопок
    button_upgrade_speed = pygame.Rect(860, 80, 32, 32)
    button_upgrade_rotation_speed = pygame.Rect(860, 130, 32, 32)
    button_upgrade_missiles = pygame.Rect(860, 180, 32, 32)
    button_upgrade_reload = pygame.Rect(860, 230, 32, 32)

    # Координаты курсора мышки
    mx, my = pygame.mouse.get_pos()

    # Отображение шкал улучшений, которые заполняются в зависимости от степени "прокачки"
    screen.blit(
        pygame.transform.scale(pygame.image.load('images/scale_imgs/scale_' + str(tank_1.sp) + '.png'), (96, 32)),
        (900, 80)
    )
    screen.blit(
        pygame.transform.scale(pygame.image.load('images/scale_imgs/scale_' + str(tank_1.rotsp) + '.png'),
                               (96, 32)),
        (900, 130)
    )
    screen.blit(
        pygame.transform.scale(pygame.image.load('images/scale_imgs/scale_' + str(tank_1.misl) + '.png'), (96, 32)),
        (900, 180)
    )
    screen.blit(
        pygame.transform.scale(pygame.image.load('images/scale_imgs/scale_' + str(tank_1.reld) + '.png'), (96, 32)),
        (900, 230)
    )

    # Отображение подписей к каждому из улучшений
    screen.blit(speed_image, pygame.Rect(900, 64, 52, 8))
    screen.blit(rotation_image, pygame.Rect(896, 114, 80, 8))
    screen.blit(bullets_image, pygame.Rect(891, 164, 80, 8))
    screen.blit(reload_image, pygame.Rect(891, 214, 80, 8))
    screen.blit(coin_image, pygame.Rect(950, 270, 32, 32))

    # При выполнении следующих 3 условий: нахождении курсора в области кнопки, нажатия на кнопку мыши
    # и достаточного кол-ва монет будет срабатывать определённое улучшение

    if tank_1.coins >= 10:
        if button_upgrade_speed.collidepoint((mx, my)):
            screen.blit(upgrade_down, button_upgrade_speed)
            if click:
                if tank_1.sp < 10:
                    b.play()
                    tank_1.v += 0.5
                    tank_1.coins -= 10
                    tank_1.sp += 1
        else:
            screen.blit(upgrade_up, button_upgrade_speed)

    if tank_1.coins >= 10:
        if button_upgrade_rotation_speed.collidepoint((mx, my)):
            screen.blit(upgrade_down, button_upgrade_rotation_speed)
            if click:
                if tank_1.rotsp < 10:
                    b.play()
                    tank_1.av += 0.2
                    tank_1.coins -= 10
                    tank_1.rotsp += 1
        else:
            screen.blit(upgrade_up, button_upgrade_rotation_speed)

    if tank_1.coins >= 10:
        if button_upgrade_missiles.collidepoint((mx, my)):
            screen.blit(upgrade_down, button_upgrade_missiles)
            if click:
                if tank_1.misl < 10:
                    b.play()
                    tank_1.max_missiles += 1
                    tank_1.coins -= 10
                    tank_1.misl += 1
        else:
            screen.blit(upgrade_up, button_upgrade_missiles)

        if tank_1.coins >= 10:
            if button_upgrade_reload.collidepoint((mx, my)):
                screen.blit(upgrade_down, button_upgrade_reload)
                if click:
                    if tank_1.reld < 10:
                        b.play()
                        tank_1.reload_speed += 0.5
                        tank_1.coins -= 10
                        tank_1.reld += 1
            else:
                screen.blit(upgrade_up, button_upgrade_reload)

        click = False
