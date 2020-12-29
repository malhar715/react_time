from title import *
from start_game import *

def main():     #game loop
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    game_state = State.MAIN_MENU
    pygame.display.set_caption('Reaction Time')
    while True:
        if game_state == State.MAIN_MENU:
            game_state = main_menu(screen)
        
        if game_state == State.NEW_GAME:
            player = PlayerInfo()
            game_state = set_rounds(screen,player)
        
        if game_state == State.NEXT_ROUND:
            if player.num_rounds < 10:
                player.num_rounds += 1
            else:
                player.num_rounds = 1
            game_state = set_rounds(screen, player)

        if game_state == State.NEXT_DIFF:
            if player.difficulty == "Easy":
                player.difficulty = "Medium"
            elif player.difficulty == "Medium":
                player.difficulty = "Hard"
            elif player.difficulty == "Hard":
                player.difficulty = "Easy"

            game_state = set_rounds(screen, player)
        
        if game_state == State.BEGIN_GAME:
            game_state = play_game(screen, player) #IN PROGRESS

        if game_state == State.INFO:
            game_state = get_info(screen)
        
        if game_state == State.QUIT:
            pygame.quit()
            return

if __name__ == "__main__":
    main()