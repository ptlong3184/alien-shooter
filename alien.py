import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    
    def __init__(self, ai_game):
        """Initialize the alien attributes"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien1.png').convert_alpha()
        self.rect = self.image.get_rect()
        
        # Start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien exact horizontal position
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Return True if an alien is at edge of the screen"""

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        """Update the position of the alien"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x