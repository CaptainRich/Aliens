import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """ A class to report game scoring. Numeric values and ship images
        are displayed and updated on the screen."""

    def __init__( self, ai_game ):
        """ Initialize the game score keeping parameters. """
        self.ai_game     = ai_game
        self.screen      = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings    = ai_game.settings
        self.stats       = ai_game.stats

        # Define the font settings to display the scoring data.
        self.text_color = ( 30, 30, 30 )
        self.font       = pygame.font.SysFont( None, 24 )

        # Prepare the initial 'score', 'level' and 'ship' images.
        self.prepare_score_images()

    
    def prepare_score_images( self ):
        """ Prep the scores, levels, and ship counters. """
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_score( self ):
        """ Turn the score into a (rounded) image. """
        rounded_score = round( self.stats.score, -1 )
        score_str = f"Score: {rounded_score:,}"
        self.score_image = self.font.render( score_str, True, self.text_color, 
                                             self.settings.bg_color )
        
        # Display the score at the top right of the screen.
        self.score_rect       = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top   = 20


    def prep_high_score( self ):
        """ Turn the high score into a (rounded) image. """
        high_score            = round( self.stats.high_score, -1 )
        high_score_str        = f"High Score: {high_score:,}"
        self.high_score_image = self.font.render( high_score_str, True, 
                                                 self.text_color, 
                                                 self.settings.bg_color )
        
        # Center the high score at the center of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_level( self ):
        """ Turn the level number into an image. """
        level_str = f"Level: {self.stats.level}" 
        self.level_image = self.font.render( level_str, True, self.text_color, 
                                             self.settings.bg_color )
        
        # Display the level number below the current score.
        self.level_rect       = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top   = self.score_rect.bottom + 10


    def prep_ships( self ):
        """ Show how many defender's ships are left."""
        self.ships = Group()
        for ship_number in range( self.stats.ships_left ):
            ship = Ship( self.ai_game )
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add( ship )



    def check_high_score( self ):
        """ Check if there is a new high score. """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def show_score( self ):
        """ Display the scoring data. """

        # Display the current game score.
        self.screen.blit( self.score_image, self.score_rect )

        # Display the high score.
        self.screen.blit( self.high_score_image, self.high_score_rect )

        # Display the game level
        self.screen.blit( self.level_image, self.level_rect )

        # Display the remaining "defender's" ships.
        self.ships.draw( self.screen )

