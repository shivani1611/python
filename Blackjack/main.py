#!/usr/bin/env python3

from sys  import exit
from Game import Game

def main( ):
  the_game = ( Game( ) )
  the_game.start( )
  return( 0 ) 

if( __name__ == ( "__main__" ) ):
  exit( main( ) )
