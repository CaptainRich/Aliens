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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()           # quite the game

            # Redraw the screen (surface) during each loop pass, to apply
            # the background color.
            self.screen.fill( self.settings.bg_color )
            self.ship.blitme()            # display the alien ship

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick( 60 )  # run the loop 60 times/second

##############################################################################
# Main
            
if __name__ == '__main__':
    # Make a game instance, then start the game.
    ai = AlienInvasion()
    ai.run_game()

