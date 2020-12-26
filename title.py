from how_to import *

import pygame           #import required libraries/files
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from pygame.sprite import RenderUpdates

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


def create_test_surface(text, font_size, text_color, bg_color):
    font = pygame.freetype.SysFont("Comic Sans MS", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_color, bgcolor=bg_color)
    return surface.convert_alpha()

class PlayerInfo:
    def __init__(self, num_rounds=1, difficulty="Easy"):
        self.num_rounds = num_rounds
        self.difficulty = difficulty

class Button(Sprite):

    def __init__(self, center_pos, text, font_size, bg_color, text_color, action=None):

        self.mouse_over = False  # indicates if the mouse over the element

        # image with mouse_over
        default_img = create_test_surface(
            text=text, font_size=font_size, text_color=text_color, bg_color=bg_color
        )

        # image w/o mouseover
        highlighted = create_test_surface(
            text=text, font_size=font_size * 1.2, text_color=RED, bg_color=bg_color
        )

        self.images = [default_img, highlighted]
        self.rects = [
            default_img.get_rect(center=center_pos),
            highlighted.get_rect(center=center_pos),
        ]

        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class State(Enum):
    QUIT = -1
    MAIN_MENU = 0
    NEW_GAME = 1
    INFO = 2

def main_menu(screen):
    Start = Button(
        center_pos=(400, 100),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text="Start",
        action= State.NEW_GAME
    )

    Instructions = Button(
        center_pos=(400, 200),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text="How to Play",
        action= State.INFO
    )    

    Quit = Button(
        center_pos=(400, 500),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text="Quit",
        action = State.QUIT
    )

    buttons = [Start,Instructions, Quit]

    while True:     #loop to check if mouse down event has occurred
        mouse_up = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLACK)

        for button in buttons:
            game_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if game_action is not None:
                return game_action
            button.draw(screen)

        pygame.display.flip()

def set_rounds(screen):

    Back = Button(
        center_pos=(150, 570),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text="Return to Main Menu",
        action= State.MAIN_MENU
    )

    while True:     #loop to check if mouse up event has occurred
        mouse_up = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLACK)

        #for button in buttons:
        game_action = Back.update(pygame.mouse.get_pos(), mouse_up)
        if game_action is not None:
            return game_action
        Back.draw(screen)

        pygame.display.flip()

def get_info(screen):
    Back = Button(
        center_pos=(150, 570),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text="Return to Main Menu",
        action= State.MAIN_MENU
    )

    while True:     #loop to check if mouse down event has occurred
        mouse_up = False


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLACK)

        #for button in buttons:
        game_action = Back.update(pygame.mouse.get_pos(), mouse_up)
        if game_action is not None:
            return game_action
        Back.draw(screen)

        #display game instructions line by line
        height = 100
        for line in info_text:
            myText = create_test_surface(line, 20, WHITE, BLACK)
            screen.blit(myText,(30,height))
            if line == info_text[-2]:
                height = height + 75
            else:
                height = height + 25
        
        pygame.display.flip()
