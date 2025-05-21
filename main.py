from game.game_manager import GameManager
from strategies.strategies import BasicStrategy, RandomStrategy

def main():
    # Create game manager
    game = GameManager()
    
    # Get number of players
    nb_players = int(input("Nombre de joueurs : "))
    game.create_players(nb_players)
    
    # Create strategies for each player
    strategies = []
    for i in range(nb_players):
        if i == 0:
            strategies.append(BasicStrategy())
        else:
            strategies.append(RandomStrategy())
    
    # Play the game
    game.play_game(strategies)

if __name__ == '__main__':
    main() 