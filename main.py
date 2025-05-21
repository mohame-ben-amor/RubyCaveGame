from game.game_manager import GameManager
from strategies.strategies import BasicStrategy, RandomStrategy

def main():
    # Crée le gestionnaire de jeu
    game = GameManager()
    
    # Demande le nombre de joueurs
    nb_players = int(input("Nombre de joueurs : "))
    game.create_players(nb_players)
    
    # Crée les stratégies pour chaque joueur
    strategies = []
    for i in range(nb_players):
        if i == 0:
            strategies.append(BasicStrategy())
        else:
            strategies.append(RandomStrategy())
    
    # Lance la partie
    game.play_game(strategies)

if __name__ == '__main__':
    main() 