import pygame
      
class Ship():
    """A class that store the ship of the game"""
    
    def __init__(self, ai_game):
        """Initialize the ship attributes"""
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # Get the ship image and load it rect
        self.image = pygame.image.load('images/spacecraft1.png').convert_alpha()
        self.rect = self.image.get_rect()
        
        # Start each ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        
        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
    
    def update(self):
        """Update the ship position by the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x
        self.rect.x = self.x
    
    def center_ship(self):
        """Center the ship at the bottom of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)