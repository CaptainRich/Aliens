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
        self.ship_speed = 2       # Default is 2 pixels per keypress

        # Define the bullet settings
        self.bullet_speed    = 3.0
        self.bullet_width    = 4
        self.bullet_height   = 15
        self.bullets_allowed = 4
        self.bullet_color    = ( 60, 60, 60 )

        # Define the settings for the UFOs
        self.ufo_speed        = 1.0
        self.fleet_drop_speed = 10

        # UFO fleet direction of 1 represents 'right', -1 represents 'left'
        self.fleet_direction  = 1
