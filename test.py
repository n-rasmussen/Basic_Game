import sys
import pygame as pg
import time as time
import Characters


# import constants so it is less typing later
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Stopwatch():
    def __int__(self, start):
        self._start = start

    def get_seconds(self):
        return time.time() - self._start


def run_game():  # main Game Loop this check if the game has been closed
    pg.init()
    t = Stopwatch()
    t._start = time.time()
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Basic Game!")
    # Creates "Player"
    player = Characters.Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    enemies = pg.sprite.Group()
    all_sprites = pg.sprite.Group()
    all_sprites.add(player)

    counter, text = 0, '0'
    font = pg.font.SysFont('Consolas', 30)

    ADDENEMY = pg.USEREVENT + 1
    pg.time.set_timer(ADDENEMY, 200)
    timer = pg.USEREVENT + 2
    pg.time.set_timer(timer, 1000)

    while True:
        for event in pg.event.get(): # looks for event to close game
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            elif event.type == QUIT:
                sys.exit()

            elif event.type == ADDENEMY:
                new_enemy = Characters.Enemy(SCREEN_WIDTH, SCREEN_HEIGHT, t.get_seconds())
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            if event.type == timer:
                counter += 1
                text = str(counter)

        pressed_keys = pg.key.get_pressed()
        player.update_player(pressed_keys)

        enemies.update()

        screen.fill((0, 0, 0))  # paints screen Black

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pg.sprite.spritecollideany(player, enemies):
            player.kill()
            break

        screen.blit(font.render(text, True, (255, 255, 255)), (SCREEN_WIDTH - 50, 10))

        pg.display.flip()

    return text

