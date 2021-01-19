from helpers import *
from title import *
from start_game import *

def main():     #game loop
    pygame.init()   #initialize the pygame library
    curr_round = 1
    results = []    #list to store the reaction times after each round
    screen = pygame.display.set_mode((800, 600))    #create the screen with dimesions of 800x600

    game_state = State.MAIN_MENU    #set the initial state as main menu
    pygame.display.set_caption('Reaction Time') #set the window caption

    while True:
        if game_state == State.MAIN_MENU:   #display the main menu
            game_state = main_menu(screen)

        if game_state == State.INFO:    #display the game's instructions
            game_state = get_info(screen)
        
        if game_state == State.NEW_GAME:
            player = PlayerInfo()
            game_state = set_rounds(screen,player)
            curr_round = 1
            results.clear()
        
        if game_state == State.NEXT_ROUND:  #update the number of rounds accordingly, limit is 10 rounds.
            if player.num_rounds < 10:      
                player.num_rounds += 1
            else:
                player.num_rounds = 1
            game_state = set_rounds(screen, player)

        if game_state == State.NEXT_DIFF:   #update difficulty from the 3 possible difficulties.
            player.difficulty = update_diff(player.difficulty)

            game_state = set_rounds(screen, player)
        
        if game_state == State.BEGIN_GAME:  #start the game with a countdown to signal beginning of a round
            game_state = start_round(screen, player, curr_round) 
    
        if game_state == State.PLAY:    #play the round and measure the resulting reaction time
            game_state = play_round(screen, player, results)
            curr_round += 1

        if game_state == State.GAME_OVER:   #end the game
            game_state = game_over(screen, results, player)
            curr_round = 1


        
        if game_state == State.QUIT:
            pygame.quit()
            return

if __name__ == "__main__":
    main()