""" A module to manage alien ships - UFOs. """

import pygame
from pygame.sprite import Sprite

class UFOs( Sprite ):
    """ A class to represent a single UFO in the alien fleet. """

    def __init__( self, ai_game ):
        """ Initialize the UFO and set its starting position. """
        super().__init__()
        self.screen   = ai_game.screen
        self.settings = ai_game.settings

        # Load the UFO image and set its 'rect' attribute
        self.image = pygame.image.load( 'images/alien.bmp' )
        self.rect  = self.image.get_rect()

        # Start each new UFO near the top left of the screen.  The actual
        # position is offset an amount equal to the height/width of the
        # UFO's 'rect'.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the UFO's exact horizontal position.
        self.x = float( self.rect.x )


    def update( self ):
        """ Move the UFO fleet to the right or left. 'fleet_direction' can 
            be either +1 or -1. """
        self.x      += self.settings.ufo_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges( self ):
        """ Check if a UFO is at the edge of the screen, and if so return True. """
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
