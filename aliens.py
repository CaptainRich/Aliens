""" An 'alien invasion game. """

# Required imports
import sys
import pygame          # MAKE SURE TO INVOKE THE VIRTUAL ENVIRONMENT!!!

from settings import Settings    # The class that manages game settings.
from ship import Ship            # The class that manages alien ships.


##############################################################################
class AlienInvasion:
    """ Overall class to manage the game assets and behavior. """

    def __init__(self):
        """ Iniitialize the game, and create its resources. """
        pygame.init()

        self.clock    = pygame.time.Clock()   # to control for frame rate
        self.settings = Settings()            # instantiate a "Settings" object

        self.screen = pygame.display.set_mode( 
            (self.settings.screen_width, self.settings.screen_height) )
        pygame.display.set_caption( "Alien Invasion" )

        self.ship = Ship( self )      # Make an instance of an alien ship


    def run_game(self):
        """ Start the main interaction (event) loop for the game. """

        while True:
            # Watch for keyboard and mouse control events.
            self._check_events()
            self.ship.update()

            # Redraw the screen (surface) during each loop pass, to apply
            # the background color.
            self._update_screen()

            self.clock.tick( 60 )  # run the loop 60 times/second


    def _check_events( self ):
        """ A helper method to respond to 'events'. Note the leading
            underscore in the method name! """
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()           # quit the game

            # Check for certain 'movement' key presses.
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events( event )

            elif event.type == pygame.KEYUP:
                self._check_keyup_events( event )


###############################################################################
# Helper (class) functions.
                
    def _update_screen( self ):
        """ A helper method to update the screen/display.  Note the leading
            underscore in the method name! """
        
        self.screen.fill( self.settings.bg_color )
        self.ship.blitme()            # display the alien ship

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _check_keydown_events( self, event ):
        """ A helper method to respond to key presses.  Note the leading
            underscore in the method name! """
        
        if event.key == pygame.K_RIGHT:
            # Move the alien ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the alien ship to the left
            self.ship.moving_left = True

        elif event.key == pygame.K_q:       # Quit if user presses 'q'
            sys.exit()
        


    def _check_keyup_events( self, event ):
        """ A helper method to respond to key releases.  Note the leading
            underscore in the method name! """
        
        if event.key == pygame.K_RIGHT:
            # Stop the movement to the right.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Stop the movement to the left.
            self.ship.moving_left = False

##############################################################################
# Main
            
if __name__ == '__main__':
    # Make a game instance, then start the game.
    ai = AlienInvasion()
    ai.run_game()

