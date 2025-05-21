import random
from models.player import Player
from constants import CARDS, RELICS, MAX_ROUNDS, DANGER_CARDS

class GameManager:
    def __init__(self):
        self.players = []
        self.relics_exit = []  # Relics that have been collected

    def create_players(self, nb_players):
        """Create the specified number of players"""
        self.players = [Player() for _ in range(nb_players)]

    def reset_round(self):
        """Reset all players for a new round"""
        for player in self.players:
            player.reset_for_round()

    def handle_card(self, card, active_players, traps, rubis_au_sol, relics_in_play):
        """Handle the effects of a drawn card"""
        # Handle trap cards
        if card in DANGER_CARDS:
            if card in traps:
                print(f"💥 Deuxième piège {card} ! Tous les joueurs encore dans la grotte perdent leurs rubis.")
                for player in active_players:
                    player.mon_sac = 0
                    player.is_active = False
                return False
            else:
                traps.append(card)
        # Handle ruby cards
        elif card.isdigit():
            value = int(card)
            if active_players:
                # Share rubies among active players
                share = value // len(active_players)
                remainder = value % len(active_players)
                for player in active_players:
                    player.mon_sac += share
                rubis_au_sol += remainder
        # Handle relic cards
        else:
            relics_in_play.append(card)
        return True

    def play_round(self, round_id, strategies):
        """Play a single round of the game"""
        # Prepare deck for this round
        deck = CARDS.copy()
        for k in range(round_id):
            if RELICS[k] not in self.relics_exit:
                deck.append(RELICS[k])
        random.shuffle(deck)

        # Initialize round
        discard_pile = []
        traps = []
        rubis_au_sol = 0
        relics_in_play = []
        self.reset_round()

        # Main round loop
        while True:
            # Players decide to stay or leave
            leaving_players = []
            for i, player in enumerate(self.players):
                if player.is_active:
                    strategy = strategies[i]
                    if strategy.play(player.mon_coffre, player.mon_sac, rubis_au_sol, 
                                   round_id, self.players, deck, discard_pile):
                        player.leave_round(round_id)
                        leaving_players.append(player)

            # Handle rewards for leaving players
            if leaving_players:
                # Share remaining rubies
                share = rubis_au_sol // len(leaving_players)
                for player in leaving_players:
                    player.mon_coffre[round_id] += share

                # If only one player left, they get all relics
                if len(leaving_players) == 1:
                    for relic in relics_in_play:
                        leaving_players[0].mon_coffre[round_id] += int(relic[2:])
                        self.relics_exit.append(relic)

            # Check if round should end
            if not any(player.is_active for player in self.players):
                break

            # Draw and handle next card
            if not deck:
                break
            card = deck.pop()
            discard_pile.append(card)
            if not self.handle_card(card, 
                                  [p for p in self.players if p.is_active],
                                  traps, rubis_au_sol, relics_in_play):
                break

            print(f"Card drawn: {card}")

        # Show round results
        print(f"\nFin de la manche {round_id + 1}")
        for i, player in enumerate(self.players):
            total_round = player.mon_coffre[round_id]
            print(f" - Joueur {i+1}: {total_round} rubis stockés dans le coffre")

    def play_game(self, strategies):
        """Play a complete game"""
        for round_id in range(MAX_ROUNDS):
            self.play_round(round_id, strategies)

        # Show final results
        print("\n🎉 Fin de partie ! Résultats finaux :")
        for i, player in enumerate(self.players):
            total = player.get_total_score()
            print(f"Joueur {i+1} : {total} rubis") 