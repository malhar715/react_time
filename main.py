from title import *

def main():     #game loop
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    game_state = State.MAIN_MENU
    pygame.display.set_caption('Reaction Time')
    while True:
        if game_state == State.MAIN_MENU:
            game_state = main_menu(screen)
        
        if game_state == State.NEW_GAME:
            game_state = set_rounds(screen)
        
        if game_state == State.INFO:
            game_state = get_info(screen)
        
        if game_state == State.QUIT:
            pygame.quit()
            return

if __name__ == "__main__":
    main()