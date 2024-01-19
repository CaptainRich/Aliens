""" An 'alien invasion game. """

import sys
import pygame

##############################################################################
class AlienInvasion:
    """ Overall class to manage the game assets and behavior. """

    def __init__(self):
        """ Iniitialize the game, and create its resources. """
        pygame.init()

        self.clock = pygame.time.Clock()   # to control for frame rate

        self.screen = pygame.display.set_mode( (1200,800) )  # game window size
        pygame.display.set_caption( "Alien Invasion" )

        # Set the background color of the game window (surface).
        self.bg_color = ( 230, 230, 230 )

    def run_game(self):
        """ Start the main interaction (event) loop for the game. """

        while True:
            # Watch for keyboard and mouse control events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()           # quite the game

            # Redraw the screen (surface) during each loop pass, to apply
            # the background color.
            self.screen.fill( self.bg_color )

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick( 60 )  # run the loop 60 times/second

##############################################################################
# Main
            
if __name__ == '__main__':
    # Make a game instance, then start the game.
    ai = AlienInvasion()
    ai.run_game()

