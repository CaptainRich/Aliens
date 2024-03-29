""" A module to contain/address the defending ship(s). """

import pygame
from pygame.sprite import Sprite

class Ship ( Sprite ):
    """ The class to manage the defending ships. """

    def __init__( self, ai_game ):
        """ Initialize the ship and its starting position. """
        super().__init__()

        self.screen      = ai_game.screen
        self.settings    = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rectangle.
        self.image = pygame.image.load( 'images/ship.bmp' )
        self.rect  = self.image.get_rect()

        # Start each new (defending) ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the ship's exact horizontal screen position.
        self.x = float( self.rect.x )

        # Set the movement flag, starting with 'not moving'.
        self.moving_right = False
        self.moving_left  = False


    def update( self ):
        """ Update the ship's position based on the movement flag. """
        # Update the ship's 'x' value, the the 'x' value of the rect.
        # Note the second clause in each of these 'if statements' limits
        # the movement of the ship to the screen (surface) borders.
        if( self.moving_right  and self.rect.right < self.screen_rect.right ):
            self.x += self.settings.ship_speed

        if( self.moving_left and self.rect.left > 0 ):
            self.x -= self.settings.ship_speed

        # Now update the "rect" object based on the ships 'x'.
        self.rect.x = self.x


    def center_ship( self ):
        """ Center the defender's ship on the screen. """ 
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float( self.rect.x )
        
          
    def blitme( self ):
        """ Draw the defending ship at its current location. """
        self.screen.blit( self.image, self.rect )
