import json

class GameStats:
    """Track statistics for Alien Invasion"""
    
    def __init__(self, ai_game):
        """Initialize the statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start Alien Invasion in an inactive state
        self.game_active = False
        
        self.game_over = False
        self.game_pause = False
        # Highscore should never be reset and be stored
        filename = 'highscore.json'
        with open(filename) as file_object:
            self.high_score = json.load(file_object)
        
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit     
        
        # Start at 0 points each reset
        self.score = 0
        
        # Start at level 1 each reset
        self.level = 1
        
        # Power shots
        self.power_shots = self.settings.power_shots_number
        
        