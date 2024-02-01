""" An 'alien invasion game. """

# Required imports
import sys
import pygame          # MAKE SURE TO INVOKE THE VIRTUAL ENVIRONMENT!!!

from settings import Settings    # The class that manages game settings.
from ship import Ship            # The class that manages defending ships.
from bullet import Bullet        # The class that manages bullets.
from ufos import UFOs            # The class that manages UFOs.


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

        self.ship    = Ship( self )           # Make an instance of a defending ship
        self.bullets = pygame.sprite.Group()  # A group to hold multiple bullets
        self.ufos    = pygame.sprite.Group()  # A group to hold multiple UFOs

        self._create_fleet()                  # Create the UFO fleet


    def run_game(self):
        """ Start the main interaction (event) loop for the game. """

        while True:
            # Watch for keyboard and mouse control events.  Update the ship
            # and bullet positions on the screen.
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_ufos()

            # Redraw the screen (surface) during each loop pass, to apply
            # the background color.
            self._update_screen()

            self.clock.tick( 60 )  # run the loop 60 times/second



###############################################################################
# Helper (class) functions.
            
    def _update_bullets( self ):
        """ A helper method to respond to manage bullets. Note the leading
            underscore in the method name! """ 

        self.bullets.update()

        # Check bullet's position and if off the top of the screen, delete
        # the bullet from the group (to avoid waisting resources).
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove( bullet )
            
        #print( len( self.bullets ) )    

        # Check for bullets that hit UFOs.  If there is a hit, get rid of the
        # bullet and the UFO that was hit.
        collisions = pygame.sprite.groupcollide( self.bullets, self.ufos, True, True )   


    def _update_ufos( self ):
        """ Check if any UFO in the fleet is at a screen edge and update the 
            positions of all of the UFOs in the alien fleet accordingly. """
        self._check_fleet_edges()
        self.ufos.update()


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


                
    def _update_screen( self ):
        """ A helper method to update the screen/display.  Note the leading
            underscore in the method name! """
        
        self.screen.fill( self.settings.bg_color )

        for bullet in self.bullets.sprites():   # Draw each bullet
            bullet.draw_bullet()

        self.ship.blitme()            # display the defending ship
        self.ufos.draw( self.screen ) # display the ufo

        # Make the most recently drawn screen visible.
        pygame.display.flip()


    def _check_keydown_events( self, event ):
        """ A helper method to respond to key presses.  Note the leading
            underscore in the method name! """
        
        if event.key == pygame.K_RIGHT:
            # Move the defending ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the defending ship to the left
            self.ship.moving_left = True

        elif event.key == pygame.K_q:       # Quit if user presses 'q'
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        


    def _check_keyup_events( self, event ):
        """ A helper method to respond to key releases.  Note the leading
            underscore in the method name! """
        
        if event.key == pygame.K_RIGHT:
            # Stop the movement to the right.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Stop the movement to the left.
            self.ship.moving_left = False

    def _fire_bullet( self ):
        """ A helper method to respond to space-bar presses.  Note the leading
            underscore in the method name! Create a new bullet and add it to
            the 'bullets' group. """
        
        if len( self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet( self )
            self.bullets.add( new_bullet )


    def _create_fleet( self ):
        """ Create the fleet of UFOs. This is also a helper method. """
        # Make a UFO, then add more until there is no more room in the 
        # current row of the screen.
        ufo = UFOs( self )

        # The spacing between UFOs is the width and height of the UFO image.
        ufo_width, ufo_height = ufo.rect.size       

        # Set where the next UFO ship goes on the screen
        current_x, current_y = ufo_width, ufo_height

        while current_y < (self.settings.screen_height - (3*ufo_height) ):
            while current_x < (self.settings.screen_width - (2*ufo_width) ):
                self._create_ufo( current_x, current_y )
                current_x += 2 * ufo_width

            # Finished with a row of UFOs, reset the x value and increment 
            # the y value for the next row (if possible).
            current_x = ufo_width
            current_y += 2 * ufo_height


    def _create_ufo( self, x_position, y_position ):
        """ Create a single UFO. This is also a helper method. """  
        new_ufo        = UFOs( self )
        new_ufo.x      = x_position
        new_ufo.rect.x = x_position
        new_ufo.rect.y = y_position
        self.ufos.add( new_ufo )


    def _check_fleet_edges( self ):
        """ Check if any UFO has hit the screen edge, and change direction. """
        for ufo in self.ufos.sprites():
            if ufo.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction( self ):
        """ Change the fleet direction and drop the fleet down one row. """
        for ufo in self.ufos.sprites():
            ufo.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1
        
##############################################################################
# Main
            
if __name__ == '__main__':
    # Make a game instance, then start the game.
    ai = AlienInvasion()
    ai.run_game()

