import pygame.font

class Difficulty:
    """Categorize the difficulty buttons of the game"""
    
    def __init__(self, ai_game, msg_1, msg_2, msg_3, msg_4):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties for the buttons
        self.width, self.height = 150, 50
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Button color
        self.re_color_button()
        
        # Build the rect for the difficulty buttons and position it
        self.easy_rect = pygame.Rect(0, 600, self.width, self.height)
        self.easy_rect.left = self.screen_rect.left + 185
        
        self.medium_rect = pygame.Rect(0, 600, self.width, self.height)
        self.medium_rect.left = self.easy_rect.right + 185
        
        self.hard_rect = pygame.Rect(0, 600, self.width, self.height)
        self.hard_rect.left = self.medium_rect.right + 185
        
        self.extreme_rect = pygame.Rect(0, 600, self.width, self.height)
        self.extreme_rect.left = self.hard_rect.right + 185
        
        # The button needs to be preped 
        self._prep_msg(msg_1, msg_2, msg_3, msg_4)
        
    def re_color_button(self):
        """Re-color the button"""
        
        self.easy_button_color = (0,0,0)
        self.medium_button_color = (0,0,0)
        self.hard_button_color = (0,0,0)
        self.extreme_button_color = (0,0,0)
    
    def _prep_msg(self, msg_1, msg_2, msg_3, msg_4):
        """Turn msg in to image and center it on the button"""
        
        # Easy button
        self.easy_msg_image = self.font.render(msg_1, True, self.text_color, self.easy_button_color)
        self.easy_msg_image_rect = self.easy_msg_image.get_rect()
        self.easy_msg_image_rect.center = self.easy_rect.center
        
        # Medium button
        self.medium_msg_image = self.font.render(msg_2, True, self.text_color, self.medium_button_color)
        self.medium_msg_image_rect = self.medium_msg_image.get_rect()
        self.medium_msg_image_rect.center = self.medium_rect.center
        
        # Hard button 
        self.hard_msg_image = self.font.render(msg_3, True, self.text_color, self.hard_button_color)
        self.hard_msg_image_rect = self.hard_msg_image.get_rect()
        self.hard_msg_image_rect.center = self.hard_rect.center
        
        # Extreme button
        self.extreme_msg_image = self.font.render(msg_4, True, self.text_color, self.extreme_button_color)
        self.extreme_msg_image_rect = self.extreme_msg_image.get_rect()
        self.extreme_msg_image_rect.center = self.extreme_rect.center
    
    def draw_button(self):
        """Display the button on the screen"""
        
        # Easy button
        self.screen.fill(self.easy_button_color, self.easy_rect)
        self.screen.blit(self.easy_msg_image, self.easy_msg_image_rect)
        
        # Medium button
        self.screen.fill(self.medium_button_color, self.medium_rect)
        self.screen.blit(self.medium_msg_image, self.medium_msg_image_rect)
        
        # Hard button 
        self.screen.fill(self.hard_button_color, self.hard_rect)
        self.screen.blit(self.hard_msg_image, self.hard_msg_image_rect)
        
        # Extreme button
        self.screen.fill(self.extreme_button_color, self.extreme_rect)
        self.screen.blit(self.extreme_msg_image, self.extreme_msg_image_rect)