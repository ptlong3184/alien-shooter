import pygame
from pygame import mixer

class SoundFX:
    """A class contains all sound effects of the game"""
    
    def __init__(self, ai_game):
        """Initialize the attributes of sound effects"""
        mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        
        self.alien_explosion_fx = pygame.mixer.Sound('sounds/alien_explosion.wav')
        self.alien_explosion_fx.set_volume(0.25)
        
        self.ship_explosion_fx = pygame.mixer.Sound('sounds/ship_explosion.wav')
        self.ship_explosion_fx.set_volume(1.25)
        
        self.power_shot_fx = pygame.mixer.Sound('sounds/power_shot.wav')
        self.power_shot_fx.set_volume(0.25)
        
        self.game_over_fx = pygame.mixer.Sound('sounds/game_over.wav')
        self.game_over_fx.set_volume(0.5)
 