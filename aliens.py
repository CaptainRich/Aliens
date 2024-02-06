""" An 'alien invasion game. """

# Required imports
import sys
from time import sleep       # To pause the game if the defender is hit.
import pygame                # MAKE SURE TO INVOKE THE VIRTUAL ENVIRONMENT!!!

from settings import Settings     # The class that manages game settings.
from ship import Ship             # The class that manages defending ships.
from bullet import Bullet         # The class that manages bullets.
from ufos import UFOs             # The class that manages UFOs.
from game_stats import GameStats  # The class to monitor game statistics
from button import Button         # The class to draw the 'play' button
from scoreboard import Scoreboard # The class to draw the 'score' to the screen


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

        # Create an instance of the GameStats to store game statistics
        self.stats = GameStats( self )

        # Create an instance of the object to display the game statistics.
        self.scorebrd = Scoreboard( self )

        self.ship    = Ship( self )           # Make an instance of a defending ship
        self.bullets = pygame.sprite.Group()  # A group to hold multiple bullets
        self.ufos    = pygame.sprite.Group()  # A group to hold multiple UFOs

        self._create_fleet()                  # Create the UFO fleet

        # Set the game to an 'in-active' state upon startup.
        self.game_active = False

        # Create the 'play' button (which doesn't display it).
        self.play_button = Button( self, "Play" )


    def run_game(self):
        """ Start the main interaction (event) loop for the game. """

        while True:
            # Watch for keyboard and mouse control events.  Update the ship
            # and bullet positions on the screen.
            self._check_events()

            # These actions occur only if the game is active (defender has
            # ships left to play with).
            if self.game_active:
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

        # Check for bullet/UFO hits, as well as the need to generate a
        # completely new UFO fleet.
        self._check_bullet_ufo_collisions() 


    def _update_ufos( self ):
        """ Check if any UFO in the fleet is at a screen edge and update the 
            positions of all of the UFOs in the alien fleet accordingly. """
        self._check_fleet_edges()
        self.ufos.update()

        # Check if a UFO hits the defending ship.
        if pygame.sprite.spritecollideany( self.ship, self.ufos ):
            ship_id = 4 - self.stats.ships_left
            print( f"Defending ship {ship_id} destroyed!" )
            self._ship_hit()

        # Check if any UFO has reached the bottom of the screen.
        self._check_ufos_bottom()



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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button( mouse_pos )



    def _check_play_button( self, mouse_pos ):
        """ A helper method to start a new game if the mouse click occurs
            withing the 'play' button boundary. """
        button_clicked = self.play_button.rect.collidepoint( mouse_pos )

        # Only reset if the click occurred when the game was inactive.
        if button_clicked and not self.game_active:
            # Reset the game statistics and settings
            self.stats.reset_stats()
            self.scorebrd.prep_score()
            self.scorebrd.prep_level()
            self.scorebrd.prep_ships()
            self.settings.initialize_dynamic_settings()
            self.game_active = True        # Make the game active.

            # Get rid of any remaining bullets or UFOs
            self.bullets.empty()
            self.ufos.empty()

            # Create a new fleet of UFOs and center the defender's ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor while game is active
            pygame.mouse.set_visible( False )

                
    def _update_screen( self ):
        """ A helper method to update the screen/display.  Note the leading
            underscore in the method name! """
        
        self.screen.fill( self.settings.bg_color )

        for bullet in self.bullets.sprites():   # Draw each bullet
            bullet.draw_bullet()

        self.ship.blitme()            # display the defending ship
        self.ufos.draw( self.screen ) # display the ufo

        # Display the scoreboard (info).
        self.scorebrd.show_score()

        # Display the 'play' button.
        if not self.game_active:
            self.play_button.draw_button()

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


    def _check_bullet_ufo_collisions( self ):
        """" Check for bullets that hit UFOs.  If there is a hit, get rid of the
             bullet and the UFO that was hit. """

        collisions = pygame.sprite.groupcollide( self.bullets, self.ufos, True, True )  

        # Update the score if a UFO is destroyed (hit by a bullet).
        if collisions:
            # Loop over this dictionary to score all UFO hits
            for ufos in collisions.values():
                self.stats.score += self.settings.ufo_points * len( ufos )    

                self.scorebrd.prep_score()
                self.scorebrd.check_high_score()

        # If the UFO group is empty (all destroyed), clear any existing bullets 
        # and create a new fleet of UFOs.
        if not self.ufos:
            self.bullets.empty()
            self._create_fleet()

            # Increase the game speeds and the level number.
            self.settings.increase_speed()
            self.stats.level += 1
            self.scorebrd.prep_level()



    def _ship_hit( self ):
        """ Defending ship has been hit by a UFO. """

        if( self.stats.ships_left > 0 ):

            # Decrement the number of defending ships left to play with.
            self.stats.ships_left -= 1
            self.scorebrd.prep_ships()       # Remove a ship image

            # Remove any existing bullets/UFOs from the screen.
            self.bullets.empty()
            self.ufos.empty()

            # Create a new fleet of UFos, a new defender's ship, and center it.
            self._create_fleet()
            self.ship.center_ship()

            # Pause the game so the player can get ready.
            sleep( 2.0 )

        else:
            self.game_active = False
            pygame.mouse.set_visible( True )  # Unhide the mouse cursor.
    


    def _check_ufos_bottom( self ):
        """ Check if any UFOs reach the bottom of the screen.  This is a 
            'loss', the same as a UFO hitting the defenders ship. """
        
        for ufo in self.ufos.sprites():
            if ufo.rect.bottom >= self.settings.screen_height:
                # This UFO is at the bottom, act as if the defender was hit.
                self._ship_hit()
                break
##############################################################################
# Main
            
if __name__ == '__main__':
    # Make a game instance, then start the game.
    ai = AlienInvasion()
    ai.run_game()

