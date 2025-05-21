import random
from models.player import Player
from constants import CARDS, RELICS, MAX_ROUNDS, DANGER_CARDS

class GameManager:
    def __init__(self):
        self.players = []
        self.relics_exit = []  # Reliques qui ont été collectées

    def create_players(self, nb_players):
        """Crée le nombre spécifié de joueurs"""
        self.players = [Player() for _ in range(nb_players)]

    def reset_round(self):
        """Réinitialise tous les joueurs pour une nouvelle manche"""
        for player in self.players:
            player.reset_for_round()

    def handle_card(self, card, active_players, traps, rubis_au_sol, relics_in_play):
        """Gère les effets d'une carte tirée"""
        # Gère les cartes pièges
        if card in DANGER_CARDS:
            if card in traps:
                print(f"💥 Deuxième piège {card} ! Tous les joueurs encore dans la grotte perdent leurs rubis.")
                for player in active_players:
                    player.mon_sac = 0
                    player.is_active = False
                return False
            else:
                traps.append(card)
        # Gère les cartes rubis
        elif card.isdigit():
            value = int(card)
            if active_players:
                # Partage les rubis entre les joueurs actifs
                share = value // len(active_players)
                remainder = value % len(active_players)
                for player in active_players:
                    player.mon_sac += share
                rubis_au_sol += remainder
        # Gère les cartes reliques
        else:
            relics_in_play.append(card)
        return True

    def play_round(self, round_id, strategies):
        """Joue une manche du jeu"""
        # Prépare le tas pour cette manche
        deck = CARDS.copy()
        for k in range(round_id):
            if RELICS[k] not in self.relics_exit:
                deck.append(RELICS[k])
        random.shuffle(deck)

        # Initialise la manche
        discard_pile = []
        traps = []
        rubis_au_sol = 0
        relics_in_play = []
        self.reset_round()

        # Boucle principale de la manche
        while True:
            # Les joueurs décident de rester ou partir
            leaving_players = []
            for i, player in enumerate(self.players):
                if player.is_active:
                    strategy = strategies[i]
                    if strategy.play(player.mon_coffre, player.mon_sac, rubis_au_sol, 
                                   round_id, self.players, deck, discard_pile):
                        player.leave_round(round_id)
                        leaving_players.append(player)

            # Gère les récompenses des joueurs partants
            if leaving_players:
                # Partage les rubis restants
                share = rubis_au_sol // len(leaving_players)
                for player in leaving_players:
                    player.mon_coffre[round_id] += share

                # Si un seul joueur part, il obtient toutes les reliques
                if len(leaving_players) == 1:
                    for relic in relics_in_play:
                        leaving_players[0].mon_coffre[round_id] += int(relic[2:])
                        self.relics_exit.append(relic)

            # Vérifie si la manche doit se terminer
            if not any(player.is_active for player in self.players):
                break

            # Tire et gère la prochaine carte
            if not deck:
                break
            card = deck.pop()
            discard_pile.append(card)
            if not self.handle_card(card, 
                                  [p for p in self.players if p.is_active],
                                  traps, rubis_au_sol, relics_in_play):
                break

            print(f"Carte tirée : {card}")

        # Affiche les résultats de la manche
        print(f"\nFin de la manche {round_id + 1}")
        for i, player in enumerate(self.players):
            total_round = player.mon_coffre[round_id]
            print(f" - Joueur {i+1}: {total_round} rubis stockés dans le coffre")

    def play_game(self, strategies):
        """Joue une partie complète"""
        for round_id in range(MAX_ROUNDS):
            self.play_round(round_id, strategies)

        # Affiche les résultats finaux
        print("\n🎉 Fin de partie ! Résultats finaux :")
        for i, player in enumerate(self.players):
            total = player.get_total_score()
            print(f"Joueur {i+1} : {total} rubis") 