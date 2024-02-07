""" A module to introduce and play sounds when a UFO is destroyed. """
import pygame
from time import sleep

class Ufodestroy:
    """ A class to manage UFO game sounds. """

    def __init__( self ):
        """ Initialize the 'ufo destroyed' sound. """
        self.sound = pygame.mixer.Sound( "ufo_destroy.wav" )



    def destroy_sound( self ):
        """ Play the crash sound when the defender's ship is destroyed. """
        pygame.mixer.Sound.play( self.sound )
        pygame.mixer.music.stop()