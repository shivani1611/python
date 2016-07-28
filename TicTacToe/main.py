#!/usr/bin/env python3

import os
import sys
import time

# global variables
a = []
b = []
c = []

p1 = ( "X" )
p2 = ( "O" )

isGridFull = ( False )

def displayError( message ):
  print( "\n\t\t\t", message )
  time.sleep( 2 )

def clearScreen( ):
  if( ( "win32" in str( sys.platform ).lower( ) ) or ( "window" in str( sys.platform ).lower( ) ) ):
    print( sys.platform )
    os.system( "cls" )
  else:
    os.system( "clear" )

def title( ):
  print( "\n\n\t\t\t\tTic Tac Toe by Armond Sarkisian" )
  print( "\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" )

def refreshScreen( ):
  clearScreen( )
  title( )

def setGrid( space, symbol ):
  global a
  global b
  global c

  space = ( space.lower( ).strip( ) )

  isSet = ( True )

  print( "SPACE: ", space )
  if( space == ( "a1" ) ):
    if( a[0] == ( " " ) ):
      a[0] = ( symbol )
    else:
      displayError( "ERROR 105: Space already occupied!" )
      isSet = ( False )
  elif( space == ( "a2" ) ):
    if( a[1] == ( " " ) ):
      a[1] = ( symbol )
    else:
      displayError( "ERROR 105: Space already occupied!" )
      isSet = ( False )
  elif( space == ( "a3" ) ):
    if( a[2] == ( " " ) ):
      a[2] = ( symbol )
    else:
      displayError( "ERROR 105: Space already occupied!" )
      isSet = ( False )
  elif( space == ( "b1" ) ):
    if( b[0] == ( " " ) ):
      b[0] = ( symbol )
    else:
      displayError( "ERROR 105: Space already occupied!" )
      isSet = ( False )
  elif( space == ( "b2" ) ):
    if( b[1] == ( " " ) ):
      b[1] = ( symbol )
    else:
      displayError( "ERROR 105: Space already occupied!" )
      isSet = ( False )
  elif( space == ( "b3" ) ):
    if( b[2] == ( " " ) ):
      b[2] = ( symbol )
    else:
      displayError( "ERROR 105: Space already occupied!" )
      isSet = ( False )
  elif( space == ( "c1" ) ):
    if( c[0] == ( " " ) ):
      c[0] = ( symbol )
    else:
      displayError( "ERROR 105: Space already occupied!" )
      isSet = ( False )
  elif( space == ( "c2" ) ):
    if( c[1] == ( " " ) ):
      c[1] = ( symbol )
    else:
      displayError( "ERROR 105: Space already occupied!" )
      isSet = ( False )
  elif( space == ( "c3" ) ):
    if( c[2] == ( " " ) ):
      c[2] = ( symbol )
    else:
      displayError( "ERROR 105: Space already occupied!" )
      isSet = ( False )
  else:
    displayError( "ERROR 102: Space does not exist!" ) 
    isSet = ( False )

  displayGrid( )
  return( isSet )

def checkGrid( ):
  global isGridFull

  if( a[0] != ( " " ) and a[1] != ( " " ) and a[2] != ( " " ) 
  and b[0] != ( " " ) and b[1] != ( " " ) and b[2] != ( " " ) 
  and c[0] != ( " " ) and c[1] != ( " " ) and c[2] != ( " " ) ):
    isGridFull = ( True )
  return( isGridFull )

def initializeGrid( ):
  global a
  global b
  global c

  a = []
  b = []
  c = []

  a.append( " " )
  a.append( " " )
  a.append( " " )

  b.append( " " )
  b.append( " " )
  b.append( " " )

  c.append( " " )
  c.append( " " )
  c.append( " " )
  return

def displayGrid( ):
  refreshScreen( )
  print( "\n\n" )
  print( "\t\t", "             1               2               3" )
  print( )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", " A           {}      |        {}        |      {}".format( a[0], a[1], a[2] ) )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "      -----------------------------------------------" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", " B           {}      |        {}        |      {}".format( b[0], b[1], b[2] ) )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "      -----------------------------------------------" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", " C           {}      |        {}        |      {}".format( c[0], c[1], c[2] ) )
  print( "\t\t", "                    |                 |" )
  print( "\t\t", "                    |                 |" )
  print( '\n' )
  return

def checkWinner( symbol ):
  isWinner = ( False )

  if( a[0] == ( symbol ) and a[1] == ( symbol ) and a[2] == ( symbol ) ):
    isWinner = ( True )
  elif( b[0] == ( symbol ) and b[1] == ( symbol ) and b[2] == ( symbol ) ):
    isWinner = ( True )
  elif( c[0] == ( symbol ) and c[1] == ( symbol ) and c[2] == ( symbol ) ):
    isWinner = ( True )
  elif( a[0] == ( symbol ) and b[0] == ( symbol ) and c[0] == ( symbol ) ):
    isWinner = ( True )
  elif( a[1] == ( symbol ) and b[1] == ( symbol ) and c[1] == ( symbol ) ):
    isWinner = ( True )
  elif( a[2] == ( symbol ) and b[2] == ( symbol ) and c[2] == ( symbol ) ):
    isWinner = ( True )
  elif( a[0] == ( symbol ) and b[1] == ( symbol ) and c[2] == ( symbol ) ):
    isWinner = ( True )
  elif( a[2] == ( symbol ) and b[1] == ( symbol ) and c[0] == ( symbol ) ):
    isWinner = ( True )
  else:
    isWinner = ( False )

  if( isWinner == ( True ) ):
    displayGrid( )
    print( '\n' + "{}".format( "Player 1: {}".format( symbol ) if symbol == ( 'X' ) else "Player 2" ) + " wins!" )
    time.sleep( 3 )
  return( isWinner )

def playTurn( who, symbol ):
  who = ( who.lower( ).strip( ) )

  if( who == ( "human" ) ):
    while( True ):
      displayGrid( )

      if( symbol.upper( ) == ( 'X' ) ):
        choice = ( input( "Player 1: Enter selection: " ) )
      else:
        choice = ( input( "Player 2: Enter selection: " ) )
      choice = ( choice.lower( ).strip( ) )

      if( ( "a1" in ( choice ) ) or ( "a2" in ( choice ) ) or ( "a3" in ( choice ) )
      or ( "b1" in ( choice ) ) or ( "b2" in ( choice ) ) or ( "b3" in ( choice ) )
      or ( "c1" in ( choice ) ) or ( "c2" in ( choice ) ) or ( "c3" in ( choice ) ) ):
        if( setGrid( choice, symbol ) == ( True ) ):
          break
      else:
        displayError( "ERROR 104: Invalid Space!" )
  elif( who == ( "computer" ) ):
    if( symbol.strip( ) == ( p1 ) ):
      comp = ( p2 )
    else:
      comp = ( p1 )

    while( True ):
      # try to get middle square first
      if( b[1] == ( " " ) ):
        if( setGrid( "b2", symbol ) == ( True ) ):
          break
      # offensive
      elif( ( a[0] == ( symbol ) ) and a[1] == ( symbol ) and a[2] == ( " " ) ):
        if( setGrid( "a3", symbol ) == ( True ) ):
          break
      elif( ( a[1] == ( symbol ) ) and a[2] == ( symbol ) and a[0] == ( " " ) ):
        if( setGrid( "a1", symbol ) == ( True ) ):
          break
      elif( ( a[0] == ( symbol ) ) and a[2] == ( symbol ) and a[1] == ( " " ) ):
        if( setGrid( "a2", symbol ) == ( True ) ):
          break
      elif( ( b[0] == ( symbol ) ) and b[1] == ( symbol ) and b[2] == ( " " ) ):
        if( setGrid( "b3", symbol ) == ( True ) ):
          break
      elif( ( b[1] == ( symbol ) ) and b[2] == ( symbol ) and b[0] == ( " " ) ):
        if( setGrid( "b1", symbol ) == ( True ) ):
          break
      elif( ( b[0] == ( symbol ) ) and b[2] == ( symbol ) and b[1] == ( " " ) ):
        if( setGrid( "b2", symbol ) == ( True ) ):
          break
      elif( ( c[0] == ( symbol ) ) and c[1] == ( symbol ) and c[2] == ( " " ) ):
        if( setGrid( "c3", symbol ) == ( True ) ):
          break
      elif( ( c[1] == ( symbol ) ) and c[2] == ( symbol ) and c[0] == ( " " ) ):
        if( setGrid( "c1", symbol ) == ( True ) ):
          break
      elif( ( c[0] == ( symbol ) ) and c[2] == ( symbol ) and c[1] == ( " " ) ):
        if( setGrid( "c2", symbol ) == ( True ) ):
          break
      elif( ( b[0] == ( symbol ) ) and c[0] == ( symbol ) and a[0] == ( " " ) ):
        if( setGrid( "a1", symbol ) == ( True ) ):
          break
      elif( ( a[0] == ( symbol ) ) and c[0] == ( symbol ) and b[0] == ( " " ) ):
        if( setGrid( "b1", symbol ) == ( True ) ):
          break
      elif( ( a[0] == ( symbol ) ) and b[0] == ( symbol ) and c[0] == ( " " ) ):
        if( setGrid( "c1", symbol ) == ( True ) ):
          break
      elif( ( b[1] == ( symbol ) ) and c[1] == ( symbol ) and a[1] == ( " " ) ):
        if( setGrid( "a2", symbol ) == ( True ) ):
          break
      elif( ( a[1] == ( symbol ) ) and c[1] == ( symbol ) and b[1] == ( " " ) ):
        if( setGrid( "b2", symbol ) == ( True ) ):
          break
      elif( ( a[1] == ( symbol ) ) and b[1] == ( symbol ) and c[1] == ( " " ) ):
        if( setGrid( "c2", symbol ) == ( True ) ):
          break
      elif( ( b[2] == ( symbol ) ) and c[2] == ( symbol ) and a[2] == ( " " ) ):
        if( setGrid( "a3", symbol ) == ( True ) ):
          break
      elif( ( a[2] == ( symbol ) ) and c[2] == ( symbol ) and b[2] == ( " " ) ):
        if( setGrid( "b3", symbol ) == ( True ) ):
          break
      elif( ( a[2] == ( symbol ) ) and b[2] == ( symbol ) and c[2] == ( " " ) ):
        if( setGrid( "c3", symbol ) == ( True ) ):
          break
      elif( ( c[2] == ( symbol ) ) and b[1] == ( symbol ) and a[2] == ( " " ) ):
        if( setGrid( "a1", symbol ) == ( True ) ):
          break
      elif( ( a[0] == ( symbol ) ) and c[2] == ( symbol ) and b[1] == ( " " ) ):
        if( setGrid( "b2", symbol ) == ( True ) ):
          break
      elif( ( a[0] == ( symbol ) ) and b[1] == ( symbol ) and c[2] == ( " " ) ):
        if( setGrid( "c3", symbol ) == ( True ) ):
          break
      elif( ( c[0] == ( symbol ) ) and b[1] == ( symbol ) and a[2] == ( " " ) ):
        if( setGrid( "a3", symbol ) == ( True ) ):
          break
      elif( ( c[0] == ( symbol ) ) and a[2] == ( symbol ) and b[1] == ( " " ) ):
        if( setGrid( "b2", symbol ) == ( True ) ):
          break
      elif( ( a[2] == ( symbol ) ) and b[1] == ( symbol ) and c[0] == ( " " ) ):
        if( setGrid( "c1", symbol ) == ( True ) ):
          break
      # defensive
      elif( ( a[0] == ( comp ) ) and a[1] == ( comp ) and a[2] == ( " " ) ):
        if( setGrid( "a3", symbol ) == ( True ) ):
          break
      elif( ( a[1] == ( comp ) ) and a[2] == ( comp ) and a[0] == ( " " ) ):
        if( setGrid( "a1", symbol ) == ( True ) ):
          break
      elif( ( a[0] == ( comp ) ) and a[2] == ( comp ) and a[2] == ( " " ) ):
        if( setGrid( "a2", symbol ) == ( True ) ):
          break
      elif( ( b[0] == ( comp ) ) and b[1] == ( comp ) and b[2] == ( " " ) ):
        if( setGrid( "b3", symbol ) == ( True ) ):
          break
      elif( ( b[1] == ( comp ) ) and b[2] == ( comp ) and b[0] == ( " " ) ):
        if( setGrid( "b1", symbol ) == ( True ) ):
          break
      elif( ( b[0] == ( comp ) ) and b[2] == ( comp ) and b[1] == ( " " ) ):
        if( setGrid( "b2", symbol ) == ( True ) ):
          break
      elif( ( c[0] == ( comp ) ) and c[1] == ( comp ) and c[2] == ( " " ) ):
        if( setGrid( "c3", symbol ) == ( True ) ):
          break
      elif( ( c[1] == ( comp ) ) and c[2] == ( comp ) and c[0] == ( " " ) ):
        if( setGrid( "c1", symbol ) == ( True ) ):
          break
      elif( ( c[0] == ( comp ) ) and c[2] == ( comp ) and c[1] == ( " " ) ):
        if( setGrid( "c2", symbol ) == ( True ) ):
          break
      elif( ( b[0] == ( comp ) ) and c[0] == ( comp ) and a[0] == ( " " ) ):
        if( setGrid( "a1", symbol ) == ( True ) ):
          break
      elif( ( a[0] == ( comp ) ) and c[0] == ( comp ) and b[0] == ( " " ) ):
        if( setGrid( "b1", symbol ) == ( True ) ):
          break
      elif( ( a[0] == ( comp ) ) and b[0] == ( comp ) and c[0] == ( " " ) ):
        if( setGrid( "c1", symbol ) == ( True ) ):
          break
      elif( ( b[1] == ( comp ) ) and c[1] == ( comp ) and a[1] == ( " " ) ):
        if( setGrid( "a2", symbol ) == ( True ) ):
          break
      elif( ( a[1] == ( comp ) ) and c[1] == ( comp ) and b[1] == ( " " ) ):
        if( setGrid( "b2", symbol ) == ( True ) ):
          break
      elif( ( a[1] == ( comp ) ) and b[1] == ( comp ) and c[1] == ( " " ) ):
        if( setGrid( "c2", symbol ) == ( True ) ):
          break
      elif( ( b[2] == ( comp ) ) and c[2] == ( comp ) and a[2] == ( " " ) ):
        if( setGrid( "a3", symbol ) == ( True ) ):
          break
      elif( ( a[2] == ( comp ) ) and c[2] == ( comp ) and b[2] == ( " " ) ):
        if( setGrid( "b3", symbol ) == ( True ) ):
          break
      elif( ( a[2] == ( comp ) ) and b[2] == ( comp ) and c[2] == ( " " ) ):
        if( setGrid( "c3", symbol ) == ( True ) ):
          break
      elif( ( c[2] == ( comp ) ) and b[1] == ( comp ) and a[0] == ( " " ) ):
        if( setGrid( "a1", symbol ) == ( True ) ):
          break
      elif( ( a[0] == ( comp ) ) and c[2] == ( comp ) and b[1] == ( " " ) ):
        if( setGrid( "b2", symbol ) == ( True ) ):
          break
      elif( ( a[0] == ( comp ) ) and b[1] == ( comp ) and c[2] == ( " " ) ):
        if( setGrid( "c3", symbol ) == ( True ) ):
          break
      elif( ( c[0] == ( comp ) ) and b[1] == ( comp ) and a[2] == ( " " ) ):
        if( setGrid( "a3", symbol ) == ( True ) ):
          break
      elif( ( c[0] == ( comp ) ) and a[2] == ( comp ) and b[1] == ( " " ) ):
        if( setGrid( "b2", symbol ) == ( True ) ):
          break
      elif( ( a[2] == ( comp ) ) and b[1] == ( comp ) and c[0] == ( " " ) ):
        if( setGrid( "c1", symbol ) == ( True ) ):
          break
      # start game placement (corners)
      elif( a[0] == ( symbol ) and a[1] == ( " " ) and a[2] == ( " " ) ):
        if( setGrid( "a3", symbol ) == ( True ) ):
          break
      # start game placement (edges ) 
      elif( a[1] == ( " " ) ):
        if( setGrid( "a1", symbol ) == ( True ) ):
          break
      # independent corners
      elif( a[0] == ( " " ) ):
        if( setGrid( "a1", symbol ) == ( True ) ):
          break
      elif( a[2] == ( " " ) ):
        if( setGrid( "a3", symbol ) == ( True ) ):
          break
      elif( c[0] == ( " " ) ):
        if( setGrid( "c1", symbol ) == ( True ) ):
          break
      elif( c[2] == ( " " ) ):
        if( setGrid( "c3", symbol ) == ( True ) ):
          break
      # independent edges
      elif( a[1] == ( " " ) ):
        if( setGrid( "a2", symbol ) == ( True ) ):
          break
      elif( c[1] == ( " " ) ):
        if( setGrid( "c2", symbol ) == ( True ) ):
          break
      elif( b[0] == ( " " ) ):
        if( setGrid( "b1", symbol ) == ( True ) ):
          break
      elif( b[2] == ( " " ) ):
        if( setGrid( "b3", symbol ) == ( True ) ):
          break
      # error space
      else:
        displayError( "ERROR 104: Invalid Space!" )
  else:
    displayError( "ERROR 103: Invalid Player!" )

  if( checkWinner( symbol ) == ( True ) ):
    return( True )
  return( False )

def humanVSComputer( ):
  if( playTurn( "computer", p1 ) == ( False ) ):
    if( playTurn( "human", p2 ) == ( False ) ):
      if( playTurn( "computer", p1 ) == ( False ) ):
        if( playTurn( "human", p2 ) == ( False ) ):
          if( playTurn( "computer", p1 ) == ( False ) ):
            if( playTurn( "human", p2 ) == ( False ) ):
              if( playTurn( "computer", p1 ) == ( False ) ):
                if( playTurn( "human", p2 ) == ( False ) ):
                  if( playTurn( "computer", p1 ) == ( False ) ):
                    displayGrid( )
                    print( '\n' + "Tie Game!" )
                    time.sleep( 3 )
  displayGrid( )
  return

def humanVSHuman( ):
  if( playTurn( "human", p1 ) == ( False ) ):
    if( playTurn( "human", p2 ) == ( False ) ):
      if( playTurn( "human", p1 ) == ( False ) ):
        if( playTurn( "human", p2 ) == ( False ) ):
          if( playTurn( "human", p1 ) == ( False ) ):
            if( playTurn( "human", p2 ) == ( False ) ):
              if( playTurn( "human", p1 ) == ( False ) ):
                if( playTurn( "human", p2 ) == ( False ) ):
                  if( playTurn( "human", p1 ) == ( False ) ):
                    displayGrid( )
                    print( '\n' + "Tie Game!" )
                    time.sleep( 3 )                   

  displayGrid( )
  return

def computerVSComputer( ):
  if( playTurn( "computer", p1 ) == ( False ) ):
    if( playTurn( "computer", p2 ) == ( False ) ):
      if( playTurn( "computer", p1 ) == ( False ) ):
        if( playTurn( "computer", p2 ) == ( False ) ):
          if( playTurn( "computer", p1 ) == ( False ) ):
            if( playTurn( "computer", p2 ) == ( False ) ):
              if( playTurn( "computer", p1 ) == ( False ) ):
                if( playTurn( "computer", p2 ) == ( False ) ):
                  if( playTurn( "computer", p1 ) == ( False ) ):
                    displayGrid( )
                    print( '\n' + "Tie Game!" )
                    time.sleep( 3 )
  displayGrid( )
  return

def menu( ):
  choice = ( "" )

  while( not choice ):
    initializeGrid( )
    refreshScreen( )

    print( "\n\n\n\t\t\t\t1) Play Human VS Computer" )
    print( "\n\t\t\t\t2) Play Human VS Human" )
    print( "\n\t\t\t\t3) Play Computer VS Computer" )
    print( "\n\t\t\t\tX) Exit" )

    choice = ( input( "\n\n\n\t\t\t\tEnter choice: " ) )
    if( choice.upper( ) == ( 'X' ) or choice.upper( ) == ( "EXIT" ) ):
      clearScreen( )
      break
    elif( choice == ( '1' ) ):
      humanVSComputer( )
    elif( choice == ( '2' ) ):
      humanVSHuman( )
    elif( choice == ( '3' ) ):
      computerVSComputer( )
    else:
      displayError( "ERROR 100: No such menu selection!" )
    time.sleep( 2 )
    choice = ( "" )
  print( '\n' )
  return

def main( ):
  menu( )

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
