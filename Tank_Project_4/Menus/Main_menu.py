import pygame
import sys


# главное меню
def main_menu(screen, c_1, one_player_down, b, control_menu_one, one_player_up, two_players_down, control_menu_two,
              two_players_up,  clock, quit_down, quit_up, fps, tank_1, yellow_tank, bullets, money, enemies, tank_2,
              red_tank, game_for_two, q_button, game_for_one,
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


        button_arcade = pygame.Rect(300, 100, 384, 96)
        button_play_two = pygame.Rect(300, 250, 384, 96)
        button_quit = pygame.Rect(300, 400, 384, 96)

        mx, my = pygame.mouse.get_pos()
        if button_arcade.collidepoint((mx, my)):
            screen.blit(one_player_down, button_arcade)
            if click:
                b.play()
                control_menu_one(screen, c_1, tank_1, b, game_for_one, yellow_tank, bullets, money, enemies,
                     w_button, a_button, s_button, d_button, space, draw_text, font, c_2, clock, fps)
        else:
            screen.blit(one_player_up, button_arcade)
        if button_play_two.collidepoint((mx, my)):
            screen.blit(two_players_down, button_play_two)
            if click:
                b.play()
                control_menu_two(screen, c_1, tank_1, b, yellow_tank, bullets, money, enemies, tank_2, red_tank, game_for_two, q_button,
                     w_button, a_button, s_button, d_button, space, draw_text, font, c_2, clock, fps, up_button, left_button,
                     down_button, right_button, m_button)
        else:
            screen.blit(two_players_up, button_play_two)
        if button_quit.collidepoint((mx, my)):
            screen.blit(quit_down, button_quit)
            if click:
                b.play()
                pygame.quit()
                sys.exit()
        else:
            screen.blit(quit_up, button_quit)

        clock.tick(fps)
        pygame.display.update()