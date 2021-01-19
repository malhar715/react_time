from helpers import *
from how_to import *

def main_menu(screen):      #Create the Main Menu screen
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

    return draw_buttons(screen, buttons, "Reaction Time Game", 40, 200, 100)

def set_rounds(screen, player):     #Create the Game Options screen

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

    return draw_buttons(screen,buttons)

def get_info(screen):       #Create the Instructions screen
    Back = Button(
        center_pos=(150, 570),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text="Return to Main Menu",
        action= State.MAIN_MENU
    )
    buttons = RenderUpdates(Back)
    return draw_buttons(screen, buttons, info_text)
    



