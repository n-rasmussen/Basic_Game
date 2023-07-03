import sys
import pygame as pg
from pygame.locals import *
from test import *


pg.init()
pg.display.set_caption('game base')

screen = pg.display.set_mode((1200, 800), 0, 32)


def make_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x,y))
    surface.blit(text_obj, text_rect)
    return text_rect


def button(text, font, color, surface, x, y):
    r = make_text(text, font, color, surface, x, y)
    l,w = r.size
    new_button = pg.Rect(x-l/2-5, y-w/2-5, l+10, w+10)
    pg.draw.rect(surface, (255, 0, 0), new_button)
    r = make_text(text, font, color, surface, x, y)
    return new_button


def main_menu(surface, SCREEN_WIDTH, SCREEN_HEIGHT):
    last_score = str(0)
    while True:
        screen.fill((0, 0, 0))
        font = pg.font.SysFont('Consolas', 60)
        make_text('Main Menu', font, (225, 225, 225), surface, SCREEN_WIDTH / 2, 100)
        mx, my = pg.mouse.get_pos()
        button_1 = button("Play", font, (0, 0, 0), surface, SCREEN_WIDTH / 2, 225)
        button_2 = button("Quit", font, (0, 0, 0), surface, SCREEN_WIDTH / 2, 375)
        make_text('last score:', font, (225, 225, 225), surface, SCREEN_WIDTH / 2, 500)
        make_text(last_score + ' sec!', font, (225, 225, 225), surface, SCREEN_WIDTH / 2, 600)
        click = False
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            if button_1.collidepoint((mx, my)):
                if click:
                    last_score = str(run_game())

            if button_2.collidepoint((mx, my)):
                if click:
                    pg.quit()
                    sys.exit()

        pg.display.update()


main_menu(screen, 1200, 800)

