import pygame

class Settings: 
    """A class that store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's settings"""
        
        # Screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg = pygame.image.load("images/bg.png")
        
        # Ship settings
        self.ship_limit = 3
        
        # Bullet settings:
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255,250,250)
        self.bullets_allowed = 3
        
        # Alien setting
        self.fleet_drop_speed = 10
        
        # How the points increases after each level
        self.easy_score_scale = 1.4
        self.medium_score_scale = 1.6
        self.hard_score_scale = 1.8
        self.extreme_score_scale = 2
        
        # How quickly the game speed up
        self.speed_up_scale_easy = 1.1
        self.speed_up_scale_medium = 1.2
        self.speed_up_scale_hard = 1.3
        self.speed_up_scale_extreme = 1.4
        
        self.initialize_dynamic_settings()
        
        # Difficulty 
        self.difficulty = 'easy'
        
    def initialize_dynamic_settings(self):
        """Initialize settings can be changed throughout the game"""
        self.ship_speed = 4
        self.bullet_speed = 2
        self.alien_speed = 1
        self.power_shot_speed = 3
        self.explosion_speed = 15
        # Fleet direction of 1 represent right, of -1 represent left
        self.fleet_direction = 1
        
        # Power shots
        self.power_shots_number = 100
        
        # Alien points
        self.alien_points = 50
        
    def increase_speed(self):
        """Increase speed of the game"""
        if self.difficulty == 'easy':
            self.alien_speed *= self.speed_up_scale_easy
            self.bullet_speed *= self.speed_up_scale_easy
            self.power_shot_speed *= self.speed_up_scale_easy
            self.explosion_speed /= self.speed_up_scale_easy
            self.alien_points = int(self.alien_points * self.easy_score_scale)
        
        elif self.difficulty == 'medium':
            self.alien_speed *= self.speed_up_scale_medium
            self.bullet_speed *= self.speed_up_scale_medium
            self.power_shot_speed *= self.speed_up_scale_medium
            self.explosion_speed /= self.speed_up_scale_medium
            self.alien_points = int(self.alien_points * self.medium_score_scale)
        
        elif self.difficulty == 'hard':
            self.alien_speed *= self.speed_up_scale_hard
            self.bullet_speed *= self.speed_up_scale_hard
            self.power_shot_speed *= self.speed_up_scale_hard
            self.explosion_speed /= self.speed_up_scale_hard
            self.alien_points = int(self.alien_points * self.hard_score_scale)
        
        elif self.difficulty == 'extreme':
            self.alien_speed *= self.speed_up_scale_extreme
            self.bullet_speed *= self.speed_up_scale_extreme
            self.power_shot_speed *= self.speed_up_scale_extreme
            self.explosion_speed /= self.speed_up_scale_extreme
            self.alien_points = int(self.alien_points * self.extreme_score_scale)