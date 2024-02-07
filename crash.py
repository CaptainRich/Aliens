""" A module to introduce and play sounds when a defender ship is destroyed. """
import pygame
from time import sleep

class Crash:
    """ A class to manage game sounds. """

    def __init__( self ):
        """ Initialize the 'defender destroyed' crash sound. """
        self.sound = pygame.mixer.Sound( "crash.wav" )



    def crash_sound( self ):
        """ Play the crash sound when the defender's ship is destroyed. """
        pygame.mixer.Sound.play( self.sound )
        sleep( 0.5 )
        pygame.mixer.music.stop()