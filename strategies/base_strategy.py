from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    @abstractmethod
    def play(self, mon_coffre, mon_sac, rubis_au_sol, id_manche, les_joueurs, tas_tri, defausse):
        """
        Make a decision whether to stay or leave the round
        
        Args:
            mon_coffre: List of integers representing rubies stored in each round
            mon_sac: Current number of rubies in hand
            rubis_au_sol: Rubies remaining to be shared
            id_manche: Current round number (0-4)
            les_joueurs: List of all players
            tas_tri: Remaining cards in deck
            defausse: Cards already played
            
        Returns:
            bool: True to leave the round, False to stay
        """
        pass 