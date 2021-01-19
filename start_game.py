from helpers import *
from title import *

def start_round(screen,player, curr_round): #Start round by either displaying countdown timer or Game Over screen
    if curr_round > player.num_rounds:
        return State.GAME_OVER
    else:
        count_down(screen, curr_round)
        return State.PLAY
            
def play_round(screen, player, results):    #Play the round and store the resulting reaction time
    if player.difficulty == "Easy":
        buttons = level_easy()
    if player.difficulty == "Medium":
        buttons = level_medium()
    if player.difficulty == "Hard":
        buttons = level_hard()

    return reaction_time(screen,buttons,results)

def game_over(screen, results, player):     #Display Game Over screen and player's avg reaction time
    Back = Button(
        center_pos=(170, 570),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text="Return to Main Menu",
        action= State.MAIN_MENU
    )
    Replay = Button(
        center_pos=(370, 570),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text="Replay",
        action= State.BEGIN_GAME
    )   
    NewGame = Button(
        center_pos=(570, 570),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text="Start a New Game",
        action= State.NEW_GAME
    ) 
    buttons = RenderUpdates(Back, Replay, NewGame)

    avg = sum(results) / len(results)
    myavg = str(round(avg,2))
    
    if player.num_rounds == 1:     
        return draw_buttons(screen, buttons,f"Your reaction time was: {myavg} ms" , 20, 215, 300)
    else:
        return draw_buttons(screen, buttons,f"Your average reaction time was: {myavg} ms" , 20, 175, 300)
        
