import sys
import pygame as pg
import random

# import constants so it is less typing later
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Player(pg.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        # self.surf = pg.Surface((75, 25))
        # self.surf.fill((255, 255, 255))
        # self.rect = self.surf.get_rect()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.surf = pg.image.load("car.png").convert()  # loads the image of the racecar
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)  # set the white colour to transparent (background of car)
        self.surf = pg.transform.scale(self.surf, (75, 25))  # scales the image
        self.rect = self.surf.get_rect(center=(0, SCREEN_HEIGHT/2))  # draws the rectangle for the shape at location

    def update_player(self, pressed_keys):  # Method to move the player with arrow key press
        if pressed_keys[K_UP]:  # takes input from key.get_pressed
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:  # conditions to keep player within the viewable screen
            self.rect.left = 0
        if self.rect.right > self.SCREEN_WIDTH:
            self.rect.right = self.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.SCREEN_HEIGHT:
            self.rect.bottom = self.SCREEN_HEIGHT


class Enemy(pg.sprite.Sprite):  # Class to create an enemy object
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, t):  # Method to generate enemy
        super().__init__()
        self.surf = pg.image.load("cone.png").convert()  # loads the image of the traffic cone
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)  # makes the white of the image transparent
        self.surf = pg.transform.scale(self.surf, (75, 75))   # scales the image
        self.rect = self.surf.get_rect(  # randomly generates the object and places it off the screen to the right
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(1, 5) * (t / 100 + 0.25)  # sets the speed at which the object will move

    def update(self):  # method to move the enemy to the left at specified speed
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()  # Kills the enemy once it moves off the screen






