import pygame           #import required packages/modules
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from pygame.sprite import RenderUpdates
import random

from how_to import info_text

GREEN = (0,255,0)       # Save colors as tuples based on RGB values
BLUE = (0,0,255)
PURPLE = (137,7,223)
YELLOW = (222,255,0)
ORANGE = (255,154,0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

levels = ["Easy", "Medium", "Hard"]     #list of possible difficulties

"""Classes"""

class PlayerInfo:               #Class to store player info
    def __init__(self, num_rounds=1, difficulty="Easy"):        
        self.num_rounds = num_rounds
        self.difficulty = difficulty

class Button(Sprite):           #Class to create menu buttons

    def __init__(self, center_pos, text, font_size, bg_color, text_color, action=None):

        self.mouse_over = False  # indicates if the mouse over the element

        # image with mouse_over
        default_img = create_text_surface(
            text=text, font_size=font_size, text_color=text_color, bg_color=bg_color
        )

        # image w/o mouseover
        highlighted = create_text_surface(
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

class State(Enum):              #Class to determine the game state
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


class GameButton(Sprite):       #Class to create game buttons

    def __init__(self, center_pos, text, font_size, bg_color, text_color, action=None):

        self.mouse_over = False  # indicates if the mouse over the element

        default_img = create_text_surface(
            text=text, font_size=font_size, text_color=text_color, bg_color=bg_color
        )

        self.images = default_img
        self.rects = default_img.get_rect(center=center_pos)

        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images

    @property
    def rect(self):
        return self.rects

    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        

"""Helper Functions"""

def create_text_surface(text, font_size, text_color, bg_color):     #Render a text surface
    font = pygame.freetype.SysFont("Comic Sans MS", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_color, bgcolor=bg_color)
    return surface.convert_alpha()

def count_down(screen, curr_round):      #Starts the countdown timer to signal a round start
    displayText(screen, f"Round {curr_round} Starts in 3...", 40, 175, 150)
    pygame.time.wait(1000)
    screen.fill(BLACK)
    displayText(screen, f"Round {curr_round} Starts in 2...", 40, 175, 150)
    pygame.time.wait(1000)
    screen.fill(BLACK)
    displayText(screen, f"Round {curr_round} Starts in 1...", 40, 175, 150)
    pygame.time.wait(1000)
    screen.fill(BLACK)

def reaction_time(screen, buttons, results):        #Measures reaction time after a mouse click
    start = pygame.time.get_ticks()

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
            if game_action is not None and game_action != State.IGNORE:
                stop=pygame.time.get_ticks()
                results.append(stop - start)
                return game_action
        buttons.draw(screen)
        pygame.display.update()       

def level_easy():       #Create buttons for the Easy level, position them in a random location
    pos = [(250,300),(600,300)]
    loc = random.sample(pos,2)

    greenbtn = make_game_button(loc[0],70,GREEN)
    redbtn = make_game_button(loc[1],70,RED)
    loc.clear()        
    buttons = RenderUpdates(greenbtn,redbtn)
    return buttons

def level_medium():     #Create buttons for the Medium level, position them in a random location
    pos = [(125,150),(575,150),(125,450),(575,450)]
    loc = random.sample(pos,4)

    greenbtn = make_game_button(loc[0],70,GREEN)
    redbtn = make_game_button(loc[1],70,RED)
    bluebtn = make_game_button(loc[2],70,BLUE)
    purplebtn = make_game_button(loc[3],70,PURPLE)

    loc.clear()
    buttons = RenderUpdates(greenbtn,redbtn, bluebtn, purplebtn)
    return buttons

def level_hard():       #Create buttons for the Hard level, position them in a random location
    pos = [(150,150),(150,300),(150,450),(650,150),(650,300),(650,450)]
    loc = random.sample(pos,6)
    #make buttons
    greenbtn = make_game_button(loc[0],70,GREEN)
    redbtn = make_game_button(loc[1],70,RED)
    bluebtn = make_game_button(loc[2],70,BLUE)
    purplebtn = make_game_button(loc[3],70,PURPLE)
    yellowbtn = make_game_button(loc[4],70,YELLOW)
    orangebtn = make_game_button(loc[5],70,ORANGE)
    #create the buttons list
    loc.clear()
    buttons = RenderUpdates(greenbtn,redbtn, bluebtn, purplebtn, yellowbtn, orangebtn)
    return buttons

def make_game_button(center, size, color):      #Create a game button, set state to IGNORE if not green
    if color == GREEN:
        btn = GameButton(
        center_pos=center,
        font_size=size,
        bg_color=color,
        text_color=color,
        text="CLICK",
        action= State.BEGIN_GAME
        )
    else:
        btn = GameButton(
        center_pos=center,
        font_size=size,
        bg_color=color,
        text_color=color,
        text="CLICK",
        action= State.IGNORE
        )
    return btn

def draw_buttons(screen, buttons, text="", size=0, xpos=0, ypos=0):      #display buttons to screen; pass in 0 for size if no text to display
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
        
        if (size != 0):
            displayText(screen, text, size, xpos, ypos)

        if (text == info_text):     #this case should only be reached if text to display is the info text
            #display text line by line
            height = 150
            for line in info_text:
                if line == info_text[0]:
                    myText = create_text_surface(line, 50, WHITE, BLACK)
                    screen.blit(myText,(250,height-100))
                else:
                    myText = create_text_surface(line, 20, WHITE, BLACK)
                    screen.blit(myText,(55,height))

                    if line == info_text[-2]:
                        height = height + 75
                    elif line == info_text[1]:
                        height = height + 75
                    elif line == info_text[4]:
                        height = height + 75
                    else:
                        height = height + 25

        pygame.display.update()

def displayText(screen, text, sz, xpos, ypos):      #Display text to the screen
    myText = create_text_surface(text, sz, WHITE, BLACK)
    screen.blit(myText,(xpos,ypos))
    pygame.display.update()

def update_diff(diff):      #Function to update the difficulty based on an existing difficulty
    if diff == "Easy":
        diff = "Medium"
    elif diff == "Medium":
        diff = "Hard"
    elif diff == "Hard":
        diff = "Easy"
    return diff     