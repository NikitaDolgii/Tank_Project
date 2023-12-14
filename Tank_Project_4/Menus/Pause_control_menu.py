import pygame
import sys


def control_menu_one(screen, c_1, tank_1, b, game_for_one, yellow_tank, bullets, money, enemies,
                     w_button, a_button, s_button, d_button, space, draw_text, font, c_2, clock, fps):
    while True:
        screen.fill(c_1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tank_1.set_zero(500, 400, 90, yellow_tank, bullets, money, enemies)
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


def control_menu_two(screen, c_1, tank_1, b, yellow_tank, bullets, money, enemies, tank_2, red_tank, game_for_two, q_button,
                     w_button, a_button, s_button, d_button, space, draw_text, font, c_2, clock, fps, up_button, left_button,
                     down_button, right_button, m_button):
    while True:
        screen.fill(c_1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tank_1.set_zero(50, 700, 90, yellow_tank, bullets, money, enemies)
                    tank_2.set_zero(900, 150, 270, red_tank, bullets, money, enemies)
                    b.play()
                    game_for_two()

        screen.blit(w_button, (190, 100))
        screen.blit(a_button, (40, 250))
        screen.blit(s_button, (190, 250))
        screen.blit(d_button, (340, 250))
        screen.blit(q_button, (190, 400))

        screen.blit(up_button, (750, 100))
        screen.blit(left_button, (600, 250))
        screen.blit(down_button, (750, 250))
        screen.blit(right_button, (900, 250))
        screen.blit(m_button, (750, 400))

        draw_text('1st Player', font, c_2, screen, 150, 50)
        draw_text('2nd Player', font, c_2, screen, 700, 50)
        screen.blit(space, (320, 550))
        draw_text('Press to start', font, c_2, screen, 400, 660)

        clock.tick(fps)
        pygame.display.update()


# меню паузы для одного игрока
def pause_menu_one(screen, c_1, one_player_down, b, control_menu_one, one_player_up, tank_1, game_for_one,
                   two_players_down, control_menu_two, yellow_tank, bullets, money, enemies,
                   two_players_up, clock, quit_down, quit_up, fps, retry_down, retry_up, continue_down,
                   continue_up, main_menu_down, main_menu, main_menu_up, tank_2,
                  red_tank, game_for_two, q_button,
                  w_button, a_button, s_button, d_button, space, draw_text, font, c_2,
                  up_button, left_button,
                  down_button, right_button, m_button):
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
                tank_1.set_zero(500, 400, 90, yellow_tank, bullets, money, enemies)
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
                main_menu(screen, c_1, one_player_down, b, control_menu_one, one_player_up, two_players_down, control_menu_two,
              two_players_up,  clock, quit_down, quit_up, fps, tank_1, yellow_tank, bullets, money, enemies, tank_2,
              red_tank, game_for_two, q_button, game_for_one,
              w_button, a_button, s_button, d_button, space, draw_text, font, c_2,
              up_button, left_button,
              down_button, right_button, m_button)
        else:
            screen.blit(main_menu_up, button_main_menu)

        clock.tick(fps)
        pygame.display.update()


def pause_menu_two(screen, c_1, one_player_down, b, control_menu_one, one_player_up, tank_1,
                   two_players_down, control_menu_two, yellow_tank, bullets, money, enemies,
                   two_players_up, clock, quit_down, quit_up, fps, retry_down, retry_up, continue_down,
                   continue_up, main_menu_down, main_menu, main_menu_up, tank_2, red_tank, game_for_two, q_button, game_for_one,
                   w_button, a_button, s_button, d_button, space, draw_text, font, c_2,
                   up_button, left_button,
                   down_button, right_button, m_button):
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
                tank_1.set_zero(50, 700, 90, yellow_tank, bullets, money, enemies)
                tank_2.set_zero(900, 150, 270, red_tank, bullets, money, enemies)
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
                main_menu(screen, c_1, one_player_down, b, control_menu_one, one_player_up, two_players_down, control_menu_two,
                          two_players_up,  clock, quit_down, quit_up, fps, tank_1, yellow_tank, bullets, money, enemies, tank_2,
                          red_tank, game_for_two, q_button, game_for_one,
                          w_button, a_button, s_button, d_button, space, draw_text, font, c_2,
                          up_button, left_button,
                          down_button, right_button, m_button)
        else:
            screen.blit(main_menu_up, button_main_menu)

        clock.tick(fps)
        pygame.display.update()