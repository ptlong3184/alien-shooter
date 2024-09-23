import pygame.font
from pygame.sprite import Group
from life import Life

class Scoreboard:
    """A class to report scoring information"""
    
    def __init__(self, ai_game):
        """Initialize the scoreboard attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        self.ai_game = ai_game
        
        # Font settings for scoring information
        self.text_color = (245,245,245)
        self.game_over_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.small_font = pygame.font.SysFont(None, 30)
        self.bg_color = (22, 26, 38)
        # Prepare all images
        self.prep_images()
        
    def prep_score(self):
        """Turn the score into rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.bg_color)
        
        # Display the score on the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        """Turn high score into rendered image"""
        self.high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.bg_color)
        
        # Display the highscore in the center top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        """Turn the level into rendered image"""
        level = self.stats.level
        level_str = str(level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.bg_color)

        # Display the level rect below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_power_shots(self):
        """Turn the power shots left into rendered image"""
        power_shot = self.stats.power_shots
        power_shot_str = str(power_shot)
        self.power_shot_image = self.small_font.render("Pow: " + power_shot_str, True, self.text_color , self.bg_color)
        
        # Display the power shot left rect on the bottom right of the screen
        self.power_shot_rect = self.power_shot_image.get_rect()
        self.power_shot_rect.x = 20 
        self.power_shot_rect.y = 65
    
    def prep_lives(self):
        """Show how many lives are left"""
        self.lives = Group()
        for life_number in range(self.stats.ships_left):
            life = Life(self.ai_game)
            life.rect.x = 10 + life_number * life.rect.width
            life.rect.y = 10 
            self.lives.add(life)
    
    def check_high_score(self):
        """Detect any new highscore"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def game_over(self):
        """Display game over when the player is out of ship"""
        self.game_over_image = self.font.render("Game over!", True, self.game_over_color, self.bg_color)
        
        # Diplay the game over
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.x = self.high_score_rect.x - 10
        self.game_over_rect.y = self.high_score_rect.y + 200
        
    def prep_images(self):
        """Prepare the images for the scoreboard elements"""
        # Prepare the initial scoring image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_power_shots()
        self.prep_lives()
        self.game_over()
    
    def show_score(self):
        """Draw the score the the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.power_shot_image, self.power_shot_rect)
        self.lives.draw(self.screen)
        