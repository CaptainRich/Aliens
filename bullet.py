""" A module to contain/address the bullet behavior. """

import pygame
from pygame.sprite import Sprite


class Bullet( Sprite ):
    """ The class to manage the firing of bullets from the ship. """

    def __init__( self, ai_game ):
        """ Create a bullet at the ship's current position. """

        super().__init__()      # Initialize the 'Sprite' class 
        self.screen   = ai_game.screen
        self.settings = ai_game.settings
        self.color    = self.settings.bullet_color


        # Create a bullet 'rect' at (0,0) and then set the correct position
        # based on the ship's location.
        self.rect = pygame.Rect( 0, 0, self.settings.bullet_width,
                                self.settings.bullet_height )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float( self.rect.y )

        
    def update( self ):
        """ Move the bullet up the screen. """

        # Update the exact position of the bullet.  (This is a decreasing
        # 'y' coordinate.)
        self.y      -= self.settings.bullet_speed
        self.rect.y =  self.y


    def draw_bullet( self ):
        """ Draw the bullet onto the screen. """
        pygame.draw.rect( self.screen, self.color, self.rect )

    