""" A module to contain/address the game settings. """

class Settings:
    """ The class to manage the game settings. """

    def __init__(self):
        """ Initialize all of the game settings. """
        
        # Screen settings
        self.screen_width  = 1200
        self.screen_height = 800
        self.bg_color      = ( 230, 230, 230 ) # background color

        # Define the defending ship settings       
        self.ship_limit = 3       # The number of defending ships allowed

        # Define the bullet settings
        self.bullet_width    = 4
        self.bullet_height   = 15
        self.bullets_allowed = 4
        self.bullet_color    = ( 60, 60, 60 )

        # Define the settings for the UFOs
        self.fleet_drop_speed = 10

        # Define how quickly the game speeds up with each new level.
        self.speedup_scale = 1.1              # About 10%
        self.score_scale   = 2.0              # Double point score per game level.

        self.initialize_dynamic_settings()    # These can change during a game.


    def initialize_dynamic_settings( self ):
        """ Initialize the settings that can change throughout the game. """
        self.ship_speed   = 2       # Default is 2 pixels per keypress
        self.bullet_speed = 3.0        
        self.ufo_speed    = 1.0
    
        # UFO fleet direction of 1 represents 'right', -1 represents 'left'
        self.fleet_direction  = 1

        # Set the points gained by destroying a UFO.
        self.ufo_points = 10
        self.max_points = 2500


    def increase_speed( self ):
        """ Increase the speed settings of the game components. """
        self.ship_speed   *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ufo_speed    *= self.speedup_scale

        # Update the points acquired for destroying UFOs when a new fleet
        # is generated.
        self.ufo_points   = int( self.ufo_points * self.score_scale )
        
        # Limit the max score per UFO
        if self.ufo_points > self.max_points:
            self.ufo_points = self.max_points 

        #print( f"New UFO score value is {self.ufo_points}" )
