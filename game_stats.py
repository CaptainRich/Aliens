

class GameStats:
    """ Track game statistics. """

    def __init__( self, ai_game ):
        """ Initialize the statistics to be tracked. """
        self.settings = ai_game.settings
        self.reset_stats()

        # The 'high score' should never be reset, but should be initialized.
        self.high_score = 0


    def reset_stats( self ):
        """ Initialize the statistics that can change during the game. """
        self.ships_left = self.settings.ship_limit

        # Reset the game score and playing level.
        self.score = 0
        self.level = 1
        