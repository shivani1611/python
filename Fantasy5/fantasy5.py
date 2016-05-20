#!/usr/bin/env python3

from random import randrange

def main( ):

  numOfWins = ( int( input( "How many times do you wish to win: " ) ) )
  sumAttempts = ( 0 )
  avgAttempts = ( 0 )
  count = ( 0 )
  winningArray = []
  userArray = []

  for i in range( 0, numOfWins, 1 ): 
    count += ( 1 )
    numOfAttempts = ( 0 )

    while True:
      isWin = ( True )
      userNumbers = ( "" )
      winningNumbers = ( "" )
      numOfAttempts += ( 1 )

      for i in range( 0, 5, 1 ):
        winningNumbers += ( str( randrange( 1 , 40, 1 ) ) )
      winningArray = ( winningNumbers.split( ' ' ) )

      for i in range( 0, 5, 1 ):
        userNumbers += ( str( randrange( 1, 40, 1 ) ) )
      userArray = ( userNumbers.split( ' ' ) )

      for x in winningArray:
        for y in userArray:
          if( y not in x ):
            isWin = ( False )

      if( isWin ):
        break

    print( "Win #:", ( count ), "\tAttempts:", numOfAttempts, "\tWinning #\'s:", userNumbers, sep = ( " " ) )
    sumAttempts += ( numOfAttempts )  

  avgAttempts = ( sumAttempts / ( count ) )

  print( "\nSum Attempts: ", sumAttempts )
  print( "Average Attempts: ", avgAttempts )

if( __name__ == ( "__main__" ) ):
  main( )
