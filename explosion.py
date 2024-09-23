import pygame
from pygame.sprite import Sprite
from alien import Alien


class Explosion(Sprite):
    """A class that manage the explosion"""
    
    def __init__(self, ai_game, object, x, y):
        """Initialize the explosion"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.alien = Alien(ai_game)
        self.images = []
       
        for num in range(1,10):
            img = pygame.image.load(f"images/{object}_explosion{num}.png")
            # Add img to the list
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.counter = 0
        
    def update(self):
        """Move the bullet up the screen"""
        
        # Update explosion animation
        self.counter += 1
        
        if self.counter >= self.settings.explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        if self.counter >= self.settings.explosion_speed and self.index >= len(self.images) - 1:
            self.kill()
            
    def draw_explosion(self):
        """Draw the explosion to the screen"""
        self.screen.blit(self.image, self.rect)  