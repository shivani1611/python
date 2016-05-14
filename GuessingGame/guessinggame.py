from sys import stdout
import random

def main( ) :
  secretNumber = ( random.randrange( 0, 10000 ) )

  while True :
    userNumber = ( int( input( "Enter number to guess: " ) ) )

    if( userNumber < ( secretNumber ) ) :
      print( "Too low!" )
    elif( userNumber > ( secretNumber ) ) :
      print( "Too high!" )
    else :
      print( "Congratulations. You win!" )
      break;

if( __name__ == ( "__main__" ) ) :
  main( )
