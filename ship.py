""" A module to contain/address the alien ship(s). """

import pygame

class Ship:
    """ The class to manage the alien shipss. """

    def __init__( self, ai_game ):
        """ Initialize the ship and its starting position. """
        self.screen      = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rectangle.
        self.image = pygame.image.load( 'images/ship.bmp' )
        self.rect  = self.image.get_rect()

        # Start each new (alien) ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    
    def blitme( self) :
        """ Draw the alien ship at its current location. """
        self.screen.blit( self.image, self.rect )
