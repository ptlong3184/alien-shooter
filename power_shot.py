import pygame
from pygame.sprite import Sprite

class PowerShot(Sprite):
    """A class that manage the powershots fired from the ship"""
    
    def __init__(self, ai_game):
        """Initialize the powershot object for the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Create a bullet rect at (0,0) and then set correct position
        self.image = pygame.image.load('images/power_shot1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = ai_game.ship.rect.midtop
        
        # Store the decimal value of the ship positon
        self.y = self.rect.y
        
    def update(self):
        """Move the powershot up the screen"""
        
        # Addjust the bulelt position by its speed
        self.y -= self.settings.power_shot_speed
        
        # Change the bullet rect position 
        self.rect.y = self.y
    
    def draw_power_shot(self):
        """Draw the bullet to the screen"""
        self.screen.blit(self.image, self.rect)