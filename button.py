import pygame.font

class Button:
    """Model the button of the game"""
    
    def __init__(self, ai_game, msg, x, y):
        """Initialize the attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and the properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the button rect subject and center it
        self.rect = pygame.Rect(x, y, self.width, self.height)
        
        # The button message needs to be preped once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg in to image and center it on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Display the button on the screen"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)