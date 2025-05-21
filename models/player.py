class Player:
    def __init__(self):
        # Initialize player's chest (one slot for each round)
        self.mon_coffre = [0] * 5
        # Current rubies in hand
        self.mon_sac = 0
        # Whether player is still in the current round
        self.is_active = True

    def reset_for_round(self):
        """Reset player for a new round"""
        self.is_active = True
        self.mon_sac = 0

    def leave_round(self, round_id):
        """Player decides to leave the round"""
        # Store current rubies in chest
        self.mon_coffre[round_id] = self.mon_sac
        # Mark as inactive and clear hand
        self.is_active = False
        self.mon_sac = 0

    def get_total_score(self):
        """Get total score from all rounds"""
        return sum(self.mon_coffre) 