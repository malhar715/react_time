from title import *
import time
import random

GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (137,7,223)
YELLOW = (222,255,0)
ORANGE = (255,154,0)

class GameButton(Sprite):

    def __init__(self, center_pos, text, font_size, bg_color, text_color, action=None):

        self.mouse_over = False  # indicates if the mouse over the element

        # image with mouse_over
        default_img = create_test_surface(
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

def start_round(screen,player, curr_round):
    if curr_round > player.num_rounds:
        return State.GAME_OVER
    else:
        countDown(screen, curr_round)
        return State.PLAY
            
def play_round(screen, player, results):
    if player.difficulty == "Easy":
        buttons = level_easy()
    if player.difficulty == "Medium":
        buttons = level_medium()
    if player.difficulty == "Hard":
        buttons = level_hard()

    
    return reaction_time(screen,buttons,results)
#Game Over Screen
def game_over(screen, results, player):
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
        return button_w_text(screen, buttons,f"Your reaction time was: {myavg} ms" , 20, 215, 300)
    else:
        return button_w_text(screen, buttons,f"Your average reaction time was: {myavg} ms" , 20, 175, 300)
        
"""Helper Functions"""

def countDown(screen, curr_round):
    displayText(screen, f"Round {curr_round} Starts in 3...", 40, 175, 150)
    pygame.time.wait(1000)
    screen.fill(BLACK)
    displayText(screen, f"Round {curr_round} Starts in 2...", 40, 175, 150)
    pygame.time.wait(1000)
    screen.fill(BLACK)
    displayText(screen, f"Round {curr_round} Starts in 1...", 40, 175, 150)
    pygame.time.wait(1000)
    screen.fill(BLACK)



def reaction_time(screen, buttons, results):
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

def level_easy():
    pos = [(250,300),(600,300)]
    loc = random.sample(pos,2)

    greenbtn = makeButton(loc[0],70,GREEN)
    redbtn = makeButton(loc[1],70,RED)
    loc.clear()        
    buttons = RenderUpdates(greenbtn,redbtn)
    return buttons

def level_medium():
    pos = [(125,150),(575,150),(125,450),(575,450)]
    loc = random.sample(pos,4)

    greenbtn = makeButton(loc[0],70,GREEN)
    redbtn = makeButton(loc[1],70,RED)
    bluebtn = makeButton(loc[2],70,BLUE)
    purplebtn = makeButton(loc[3],70,PURPLE)

    loc.clear()
    buttons = RenderUpdates(greenbtn,redbtn, bluebtn, purplebtn)
    return buttons

def level_hard():
    pos = [(150,150),(150,300),(150,450),(650,150),(650,300),(650,450)]
    loc = random.sample(pos,6)
    #make buttons
    greenbtn = makeButton(loc[0],70,GREEN)
    redbtn = makeButton(loc[1],70,RED)
    bluebtn = makeButton(loc[2],70,BLUE)
    purplebtn = makeButton(loc[3],70,PURPLE)
    yellowbtn = makeButton(loc[4],70,YELLOW)
    orangebtn = makeButton(loc[5],70,ORANGE)
    #create the buttons list
    loc.clear()
    buttons = RenderUpdates(greenbtn,redbtn, bluebtn, purplebtn, yellowbtn, orangebtn)
    return buttons

def makeButton(center, size, color):
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