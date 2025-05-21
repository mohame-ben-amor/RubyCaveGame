class Player:
    def __init__(self):
        # Initialise le coffre du joueur (un emplacement pour chaque manche)
        self.mon_coffre = [0] * 5
        # Rubis actuels en main
        self.mon_sac = 0
        # Indique si le joueur est toujours actif dans la manche
        self.is_active = True

    def reset_for_round(self):
        """Réinitialise le joueur pour une nouvelle manche"""
        self.is_active = True
        self.mon_sac = 0

    def leave_round(self, round_id):
        """Le joueur décide de quitter la manche"""
        # Stocke les rubis actuels dans le coffre
        self.mon_coffre[round_id] = self.mon_sac
        # Marque comme inactif et vide la main
        self.is_active = False
        self.mon_sac = 0

    def get_total_score(self):
        """Calcule le score total de toutes les manches"""
        return sum(self.mon_coffre) 