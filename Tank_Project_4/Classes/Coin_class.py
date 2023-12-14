import pygame


class Coin:
    def __init__(self, x, y, coin_drop):
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(coin_drop)
        self.life = 1

    def render(self, screen, coin_drop):
        if self.life:
            screen.blit(coin_drop, (self.x, self.y))

    def hittest(self, obj, tank_1, coin_sound):
        if self.life:
            if self.mask.overlap(obj, (tank_1.rx - self.x, tank_1.ry - self.y)):
                coin_sound.play()
                tank_1.coins += 5
                self.life = 0
