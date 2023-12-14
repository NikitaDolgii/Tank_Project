import pygame
import sys


# Меню выбора улучшения для танка в одиночной игре
def evolve_menu(screen, clock, fps, three_bullets_down, b, tank_1, yellow_tank_3_bullets,
                three_bullets_up, shield_down, shield_up):
    ind = True
    while ind:
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        button_3_bullets = pygame.Rect(120, 150, 384, 384)
        button_shield = pygame.Rect(520, 150, 384, 384)

        mx, my = pygame.mouse.get_pos()
        if button_3_bullets.collidepoint((mx, my)):
            screen.blit(three_bullets_down, button_3_bullets)
            if click:
                b.play()
                tank_1.img = yellow_tank_3_bullets
                tank_1.fire_mode = 3
                ind = False

        else:
            screen.blit(three_bullets_up, button_3_bullets)
        if button_shield.collidepoint((mx, my)):
            screen.blit(shield_down, button_shield)
            if click:
                b.play()
                tank_1.defence = 1
                tank_1.shield = 3
                ind = False

        else:
            screen.blit(shield_up, button_shield)

        click = False

        clock.tick(fps)
        pygame.display.update()
