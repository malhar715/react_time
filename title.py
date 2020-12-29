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

levels = ["Easy", "Medium", "Hard"]

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
    NEXT_ROUND = 3
    NEXT_DIFF = 4
    BEGIN_GAME = 5
    GAME_OVER = 6
    PLAY = 7
    IGNORE = 8

def main_menu(screen):
    Start = Button(
        center_pos=(400, 300),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text="Start",
        action= State.NEW_GAME
    )

    Instructions = Button(
        center_pos=(400, 400),
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

    buttons = RenderUpdates(Start, Instructions, Quit)

    return button_w_text(screen, buttons, "Reaction Time Game", 40, 200, 100)

def set_rounds(screen, player):

    Back = Button(
        center_pos=(150, 570),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text="Return to Main Menu",
        action= State.MAIN_MENU
    )

    BeginGame = Button(
        center_pos=(400, 450),
        font_size=40,
        bg_color=BLACK,
        text_color=WHITE,
        text="Begin",
        action= State.BEGIN_GAME
    )

    AddRound = Button(
        center_pos=(400, 200),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text=f"Number of rounds ({player.num_rounds})",
        action= State.NEXT_ROUND
    )

    IncDiff = Button(
        center_pos=(400, 300),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text=f"Difficulty ({player.difficulty})",
        action= State.NEXT_DIFF
    )

    buttons = RenderUpdates(Back, BeginGame, AddRound, IncDiff)

    return game_loop(screen, buttons)

def get_info(screen):
    Back = Button(
        center_pos=(150, 570),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text="Return to Main Menu",
        action= State.MAIN_MENU
    )
    buttons = RenderUpdates(Back)
    return btn_w_line(screen, buttons, info_text)
    


""" HELPER FUNCTIONS """
def game_loop(screen, buttons):
    while True:     #loop to check if mouse down event has occurred
        mouse_up = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                return State.QUIT
        screen.fill(BLACK)

        for button in buttons:
            game_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if game_action is not None:
                return game_action
        buttons.draw(screen)

        pygame.display.update()

def btn_w_line(screen, buttons, lines):
    while True:     #loop to check if mouse down event has occurred
        mouse_up = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                return State.QUIT
        screen.fill(BLACK)

        for button in buttons:
            game_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if game_action is not None:
                return game_action
        buttons.draw(screen)
        
        #display text line by line
        height = 150
        for line in info_text:
            if line == info_text[0]:
                myText = create_test_surface(line, 50, WHITE, BLACK)
                screen.blit(myText,(250,height-100))
            else:
                myText = create_test_surface(line, 20, WHITE, BLACK)
                screen.blit(myText,(55,height))

                if line == info_text[-2]:
                    height = height + 75
                elif line == info_text[1]:
                    height = height + 75
                elif line == info_text[4]:
                    height = height + 75
                else:
                    height = height + 25

        pygame.display.flip()

def button_w_text(screen, buttons, text, size, xpos, ypos):
    while True:     #loop to check if mouse down event has occurred
        mouse_up = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                return State.QUIT
        screen.fill(BLACK)

        for button in buttons:
            game_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if game_action is not None:
                return game_action
        buttons.draw(screen)
        
        displayText(screen, text, size, xpos, ypos)

        pygame.display.update()

def displayText(screen, text, sz, xpos, ypos):
    myText = create_test_surface(text, sz, WHITE, BLACK)
    screen.blit(myText,(xpos,ypos))
    pygame.display.update()
