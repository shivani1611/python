#!/usr/bin/env python3

from random import randrange

def main( ):

  numOfWins = ( int( input( "How many times do you wish to win: " ) ) )
  sumAttempts = ( 0 )
  avgAttempts = ( 0 )
  count = ( 0 )

  for i in range( 0, numOfWins, 1 ): 
    count += ( 1 )
    numOfAttempts = ( 0 )

    while True:
      userNumbers = ( "" )
      winningNumbers = ( "" )
      numOfAttempts += ( 1 )

      for i in range( 0, 3, 1 ):
        winningNumbers += ( str( randrange( 0, 10, 1 ) ) )

      for i in range( 0, 3, 1 ):
        userNumbers += ( str( randrange( 0, 10, 1 ) ) )

      if( userNumbers == ( winningNumbers ) ):
        break 

    print( "Attempts:", numOfAttempts, "\tWinning #\'s:", userNumbers, sep = ( " " ) )
    sumAttempts += ( numOfAttempts )  

  avgAttempts = ( sumAttempts / ( count ) )

  print( "\nSum Attempts: ", sumAttempts )
  print( "Average Attempts: ", avgAttempts )

if( __name__ == ( "__main__" ) ):
  main( )
