import random
from constants import DANGER_CARDS

class BasicStrategy:
    def play(self, mon_coffre, mon_sac, rubis_au_sol, id_manche, les_joueurs, tas_tri, defausse):
        # Prise de décision basée sur des facteurs simples
        decision = 1000
        choix = random.randint(0, 1000)
        
        # Réduit la décision en fonction du nombre de cartes jouées
        decision = decision - (len(defausse) * 80)
        
        # Réduit la décision en fonction du nombre de pièges
        pieges = sum(1 for card in defausse if card in DANGER_CARDS)
        decision = decision - (pieges * 100)
        
        # Réduit la décision en fonction des rubis au sol
        decision = decision - (rubis_au_sol * 10)
        
        return choix > decision

class RandomStrategy:
    def play(self, mon_coffre, mon_sac, rubis_au_sol, id_manche, les_joueurs, tas_tri, defausse):
        # Compte les joueurs actifs
        joueurs_actifs = sum(1 for j in les_joueurs if j.is_active)
        
        # Prise de décision simple
        if mon_sac >= 15:  # Quitte si assez de rubis
            return True
            
        if len(tas_tri) < 10:  # Plus susceptible de quitter quand le tas est presque vide
            return random.random() < 0.4
            
        # Probabilité de base qui augmente avec le numéro de la manche
        return random.random() < (0.2 + id_manche * 0.05) 