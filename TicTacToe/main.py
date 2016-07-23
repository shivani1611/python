#!/usr/bin/env python3

import os
import sys
import time

def clearScreen( ):
  if( sys.platform == ( "Windows" ) ):
    os.system( "cls" )
  else:
    os.system( "clear" )

def title( ):
  print( "\n\n\t\t\t\tTic Tac Toe by Armond Sarkisian" )
  print( "\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" )

def refreshScreen( ):
  clearScreen( )
  title( )

def displayGrid( ):
  refreshScreen( )
  print( "\n\n" )
  print( "\t\t", "             1               2               3" )
  print( )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", " A                  |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "      -----------------------------------------------" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", " B                  |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "      -----------------------------------------------" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", " C                  |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( '\n' )

def playOpponentHuman( ):
  pass

def playOpponentComputer( ):
  displayGrid( )
  time.sleep( 5 )
  pass

def menu( ):

  choice = ( "" )

  while( not choice ):
    refreshScreen( )

    print( "\n\n\n\t\t\t\t1) Play Computer" )
    print( "\t\t\t\t2) Play Human" )
    print( "\t\t\t\tX) Exit" )

    choice = ( input( "\n\t\t\t\tEnter choice: " ) )
    if( choice.lower( ) == ( 'x' ) ):
      clearScreen( )
      break
    elif( choice == ( '1' ) ):
      playOpponentComputer( )
    elif( choice == ( '2' ) ):
      playOpponentHuman( )
    else:
      print( "\n\t\t\tERROR 100: No such menu selection. Please try again!" )
    time.sleep( 2 )
    choice = ( "" )
  print( '\n' )

def main( ):
  menu( )

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
