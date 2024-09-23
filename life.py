import pygame
from pygame.sprite import Sprite
      
class Life(Sprite):
    """A class that store the lives of the game"""
    
    def __init__(self, ai_game):
        """Initialize the lives attributes"""
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        super().__init__()
        
        # Get the lives image and load it rect
        self.image = pygame.image.load('images/lives.png').convert_alpha()
        self.rect = self.image.get_rect()