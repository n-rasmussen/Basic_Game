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


class Stopwatch:  # this class creates a timer to control the speed of enemies
    def __int__(self, start):
        self._start = start

    def get_seconds(self): # this method tracks how long the game has been going on for
        return time.time() - self._start


def run_game():  # main Game Loop
    pg.init()  # initializes imported pygame modules
    t = Stopwatch()  # create game timer object
    t._start = time.time()  # sets the start time on the game timer
    SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800  # sets screen dimensions
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # makes screen
    pg.display.set_caption("Basic Game!") # makes window name
    # Creates "Player"
    player = Characters.Player(SCREEN_WIDTH, SCREEN_HEIGHT)  # creates player object
    enemies = pg.sprite.Group()  # makes a bucket to hold enemies
    all_sprites = pg.sprite.Group()  # makes a bucket to hold enemies and player
    all_sprites.add(player)  # adds player to bucket holding all Sprites

    counter, text = 0, '0'  # initalize the timer in game
    font = pg.font.SysFont('Consolas', 30)  # sets fond and size of in game timer

    ADDENEMY = pg.USEREVENT + 1  # Create an event called ADDENEMY and asigns it to the next available event int
    pg.time.set_timer(ADDENEMY, 200)  # places the event (ADDENEMY) in the event queue every 200 ms
    timer = pg.USEREVENT + 2   # Create an event called timer and asigns it to the next available event int
    pg.time.set_timer(timer, 1000)  # places the event (timer) in the event queue every 1 s

    while True:
        for event in pg.event.get():  # iterate through the event queue
            if event.type == KEYDOWN:  # if event is escape quite program
                if event.key == K_ESCAPE:
                    sys.exit()
            elif event.type == QUIT:  # if event is quit window quit program
                sys.exit()

            elif event.type == ADDENEMY:  # if event is ADDENEMY generate a new enemy
                new_enemy = Characters.Enemy(SCREEN_WIDTH, SCREEN_HEIGHT, t.get_seconds())
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            if event.type == timer:  # if event is timer, add 1 sec to the displayed timer
                counter += 1
                text = str(counter)

        pressed_keys = pg.key.get_pressed()  # get state of all keyboard buttons
        player.update_player(pressed_keys)  # puts keyboard states into the player method to move player

        enemies.update()  # moves the enemies

        screen.fill((150, 150, 150))  # paints screen Black

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)  # puts all the Sprites on the screen

        if pg.sprite.spritecollideany(player, enemies):  # if the player collides with an enemy
            player.kill()  # Kill Player
            break  # break game loop to go to menu screen

        screen.blit(font.render(text, True, (255, 255, 255)), (SCREEN_WIDTH - 50, 10))  # display the timer on screen

        pg.display.flip()  # send the screen output to monitor

    return text

