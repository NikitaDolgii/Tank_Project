import pygame
import sys


# меню смерти для одного игрока
def death_menu_one(screen, c_5, draw_text, tank_1, font, c_2, retry_down, retry_up,  yellow_tank, bullets, money,
                   enemies, c_1, one_player_down, b, control_menu_one, one_player_up, two_players_down, control_menu_two,
                   two_players_up, clock, quit_down, quit_up, fps, game_for_one, main_menu_down, main_menu, main_menu_up):
    while True:
        screen.fill(c_5)
        draw_text("You've got " + str(tank_1.points + tank_1.coins) + " points!", font, c_2, screen, 340, 100)
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        button_retry = pygame.Rect(340, 200, 384, 96)
        button_main_menu = pygame.Rect(340, 350, 384, 96)

        mx, my = pygame.mouse.get_pos()
        if button_retry.collidepoint((mx, my)):
            screen.blit(retry_down, button_retry)
            if click:
                tank_1.set_zero(500, 400, 90, yellow_tank, bullets, money, enemies)
                b.play()
                game_for_one()
        else:
            screen.blit(retry_up, button_retry)
        if button_main_menu.collidepoint((mx, my)):
            screen.blit(main_menu_down, button_main_menu)
            if click:
                b.play()
                main_menu(screen, c_1, one_player_down, b, control_menu_one, one_player_up, two_players_down, control_menu_two,
                          two_players_up, clock, quit_down, quit_up, fps)
        else:
            screen.blit(main_menu_up, button_main_menu)
        clock.tick(fps)
        pygame.display.update()


# меню смерти для двух игроков
def death_menu_two(screen, c_5, tank_1, retry_down, retry_up,  yellow_tank, bullets, money,
                   enemies, c_1, one_player_down, b, control_menu_one, one_player_up, two_players_down, control_menu_two,
                   two_players_up, clock, quit_down, quit_up, fps, main_menu_down, main_menu, main_menu_up,
                   tank_2, red_tank, game_for_two):
    while True:
        screen.fill(c_5)
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        button_retry = pygame.Rect(340, 200, 384, 96)
        button_main_menu = pygame.Rect(340, 350, 384, 96)

        mx, my = pygame.mouse.get_pos()
        if button_retry.collidepoint((mx, my)):
            screen.blit(retry_down, button_retry)
            if click:
                tank_1.set_zero(50, 700, 90, yellow_tank, bullets, money, enemies)
                tank_2.set_zero(900, 150, 270, red_tank, bullets, money, enemies)
                b.play()
                game_for_two()
        else:
            screen.blit(retry_up, button_retry)
        if button_main_menu.collidepoint((mx, my)):
            screen.blit(main_menu_down, button_main_menu)
            if click:
                b.play()
                main_menu(screen, c_1, one_player_down, b, control_menu_one,
                          one_player_up, two_players_down, control_menu_two,
                          two_players_up,
                          clock, quit_down, quit_up, fps)
        else:
            screen.blit(main_menu_up, button_main_menu)

        clock.tick(fps)
        pygame.display.update()

