#!/usr/bin/env python3

import random
import copy
import sys

def main( ):

  verboseMode = ( False )
  howManyTimesToWin = ( 0 )

  if( len( sys.argv ) == ( 1 ) ):
    print( "No arguments specified!" )
    print( "-v = verbose mode" )
    print( "# = how many times to win" )
    print( "Example: python3 main.py -v 10" )
    quit( )
  elif( len( sys.argv ) > ( 1 ) ):
    for i in range( 0, len( sys.argv ), 1 ):
      if( sys.argv[i] == ( "-v" ) ):
        verboseMode = ( True )
      elif( sys.argv[i].isnumeric( ) ):
        howManyTimesToWin = ( int( sys.argv[i] ) )

  if( howManyTimesToWin == ( 0 ) ):
    print( "Number argument not specified!" )
    quit( )

  random.seed( )

  sumAttempts = ( 0 )
  averageWins = ( 0 )
  numOfWins = ( 0 )

  print( )
 
  for a in range( 0, howManyTimesToWin, 1 ):
    attemptsCounter = ( 0 )

    while( True ):
      attemptsCounter = ( attemptsCounter + 1 )
      winningNumbers = []
      userNumbers = []

      for i in range( 0, 5, 1 ):
        winningNumbers.append( random.randint( 1, 40 ) )

      for i in range( 0, 5, 1 ):
        userNumbers.append( random.randint( 1, 40 ) )

      # keep a backup of the user numbers
      backupUserNumbers = ( copy.copy( userNumbers ) )

      for x in range( 0, len( winningNumbers ), 1 ):
        for y in range( 0, len( backupUserNumbers ), 1 ):
          if( backupUserNumbers[y] == ( winningNumbers[x] ) ):
            backupUserNumbers[y] = ( 'X' )
            break

      if( verboseMode ):
        print( "Attempt #: %d" % attemptsCounter , " Winning:", winningNumbers, " User:",  userNumbers )

      if( backupUserNumbers == ( [ 'X', 'X', 'X', 'X', 'X' ] ) ):
        print( "Attempt #: %d" % attemptsCounter, "\tWinning Number:", userNumbers )
        numOfWins = ( numOfWins + 1 )
        break

    sumAttempts += ( attemptsCounter )

  averageWins = ( numOfWins / ( sumAttempts ) )

  print( "\nTotal Attempts:\t\t", sumAttempts )
  print( "Total Wins:\t\t", numOfWins )
  print( "Average Wins:\t\t %f" % averageWins )
  print( "Winning Numbers:\t {}/{}\n".format( winningNumbers, userNumbers ) )
 
if( __name__ == ( "__main__" ) ):
  main( )
