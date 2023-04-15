import sys
import pygame as pg

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


def run_game():  # main Game Loop this check if the game has been closed
    pg.init()
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Basic Game!")
    # Creates "Player"
    player = Characters.Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    enemies = pg.sprite.Group()
    all_sprites = pg.sprite.Group()
    all_sprites.add(player)

    ADDENEMY = pg.USEREVENT + 1
    pg.time.set_timer(ADDENEMY, 250)

    while True:
        for event in pg.event.get(): # looks for event to close game
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            elif event.type == QUIT:
                sys.exit()

            elif event.type == ADDENEMY:
                new_enemy = Characters.Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        pressed_keys = pg.key.get_pressed()
        player.update_player(pressed_keys)

        enemies.update()

        screen.fill((0, 0, 0)) # paints screen Black

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pg.sprite.spritecollideany(player,enemies):
            player.kill()
            sys.exit()

        pg.display.flip()


run_game()
