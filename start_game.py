from title import *
import time
import random

GREEN = (0,255,0)


def start_round(screen,player, curr_round):
    if curr_round > player.num_rounds:
        return State.GAME_OVER
    else:
        countDown(screen, curr_round)
        return State.PLAY
            
def play_round(screen, player, results):
    Click = Button(
        center_pos=(400, 400),
        font_size=20,
        bg_color=BLACK,
        text_color=WHITE,
        text="CLICK ME",
        action= State.BEGIN_GAME
    )
    buttons = RenderUpdates(Click)
    return reaction_time(screen,buttons,results)
#Game Over Screen
def game_over(screen, results):
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
    return button_w_text(screen, buttons,f"Your average reaction time is: {myavg} ms" , 20, 100, 100)      
        
        


"""Helper Functions"""
def displayText(screen, text, sz, xpos, ypos):
    myText = create_test_surface(text, sz, WHITE, BLACK)
    screen.blit(myText,(xpos,ypos))
    pygame.display.update()

def countDown(screen, curr_round):
    displayText(screen, f"Round {curr_round} Starts in 3", 40, 125, 150)
    pygame.time.wait(1000)
    screen.fill(BLACK)
    displayText(screen, f"Round {curr_round} Starts in 2", 40, 125, 150)
    pygame.time.wait(1000)
    screen.fill(BLACK)
    displayText(screen, f"Round {curr_round} Starts in 1", 40, 125, 150)
    pygame.time.wait(1000)
    screen.fill(BLACK)

def button_w_text(screen, buttons, text, size, xpos, ypos):
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
        buttons.draw(screen)
        
        displayText(screen, text, size, xpos, ypos)

        pygame.display.update()

def reaction_time(screen, buttons, results):
    start = pygame.time.get_ticks()

    while True:     #loop to check if mouse down event has occurred
        mouse_up = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLACK)

        for button in buttons:
            game_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if game_action is not None:
                stop=pygame.time.get_ticks()
                results.append(stop - start)
                return game_action
        buttons.draw(screen)
        pygame.display.update()       
