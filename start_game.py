from title import *
GREEN = (0,255,0)


def play_game(screen,player):
    running = True
    curr_round = 1

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

    while running:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True    
            screen.fill(BLACK)
            if event.type == pygame.QUIT:
                running = False

        while curr_round <= player.num_rounds:
            countDown(screen, curr_round)
            game_loop
            screen.fill(BLACK)
            curr_round += 1

#Game Over Screen
        for button in buttons:
            screen.fill(BLACK)
            game_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if game_action is not None:
                return game_action
            buttons.draw(screen)
        displayText(screen, "Your average reaction time is N/A", 30, 95, 150)
        
        


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

