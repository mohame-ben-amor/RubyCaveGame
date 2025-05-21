import random
from constants import DANGER_CARDS

class BasicStrategy:
    def play(self, mon_coffre, mon_sac, rubis_au_sol, id_manche, les_joueurs, tas_tri, defausse):
        # Simple decision making based on basic factors
        decision = 1000
        choix = random.randint(0, 1000)
        
        # Reduce decision based on number of cards played
        decision = decision - (len(defausse) * 80)
        
        # Reduce decision based on number of traps
        traps = sum(1 for card in defausse if card in DANGER_CARDS)
        decision = decision - (traps * 100)
        
        # Reduce decision based on rubies on the ground
        decision = decision - (rubis_au_sol * 10)
        
        return choix > decision

class RandomStrategy:
    def play(self, mon_coffre, mon_sac, rubis_au_sol, id_manche, les_joueurs, tas_tri, defausse):
        # Count active players
        active_players = sum(1 for j in les_joueurs if j.is_active)
        
        # Simple decision making
        if mon_sac >= 15:  # Leave if we have enough rubies
            return True
            
        if len(tas_tri) < 10:  # More likely to leave when deck is almost empty
            return random.random() < 0.4
            
        # Basic probability that increases with round number
        return random.random() < (0.2 + id_manche * 0.05) 