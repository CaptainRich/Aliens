
import pygame.font

class Button:
    """ A class to build buttons for the game. """

    def __init__( self, ai_game, msg ):
        """ Initialize the (game start) button attributes. """
        self.screen      = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the (Play) button.
        self.width, self.height = 200, 50
        self.button_color       = ( 0, 135, 0 )
        self.text_color         = ( 255, 255, 255 )
        self.font               = pygame.font.SysFont( None, 48 )

        # Build the button's rect object and center it on the screen.
        self.rect        = pygame.Rect( 0, 0, self.width, self.height )
        self.rect.center = self.screen_rect.center

        # "prep" the button's message (needed only once).
        self._prep_msg( msg )


    def draw_button( self ):
        """ Draw a blank button, then draw the message. """
        self.screen.fill( self.button_color, self.rect )
        self.screen.blit( self.msg_image, self.msg_image_rect )
        

############################################################################
## Helper class methods
        
    def _prep_msg( self, msg ):
        """ A helper method to turn the message into a rendered image and
            center the text on the button. """
        self.msg_image = self.font.render( msg, True, self.text_color,
                                           self.button_color )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
