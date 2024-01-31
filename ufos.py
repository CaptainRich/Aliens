""" A module to manage alien ships - UFOs. """

import pygame
from pygame.sprite import Sprite

class UFOs( Sprite ):
    """ A class to represent a single UFO in the alien fleet. """

    def __init__( self, ai_game ):
        """ Initialize the UFO and set its starting position. """
        super().__init__()
        self.screen = ai_game.screen

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
