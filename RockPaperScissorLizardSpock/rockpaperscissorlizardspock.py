#!/usr/bin/env python

import random

def main( ):
  hands = { 1 : "rock", 2 : "paper", 3 : "scissor", 4 : "lizard", 5: "spock" }
  rockWins = paperWins = scissorWins = lizardWins = spockWins = tie = ( 0 )

  totalGames = ( input( "\nEnter # of games to play: " ) ) 
  while( totalGames.isalpha( ) ):
    totalGames = ( input( "Enter # of games toplay: " ) )

  totalGames = ( int( totalGames ) )

  print( "\n", end = ( "" ) )

  for i in range( 0, totalGames ):
    p1randNum = ( random.randrange( 1, len( hands ) + 1 ) )
    p2randNum = ( random.randrange( 1, len( hands ) + 1 ) )

    print( "Player one:", hands[p1randNum]
      , "\tVS\t"
      , "Player two:"
      , hands[p2randNum]
      , sep = ( " " )
      , end = ( " " ) )

    if( hands[p1randNum] == ( "rock" ) and ( hands[p2randNum] == ( "rock" ) ) ):
      print( "\t=\t"
        , "TIE"
        , sep = ( " " )
        , end = ( "\n" ) )
      tie = tie + 1
    elif( hands[p1randNum] == ( "paper" ) and ( hands[p2randNum] == ( "paper" ) ) ):
      print( "\t=\t"
        , "TIE"
        , sep = ( " " )
        , end = ( "\n" ) )
      tie = tie + 1
    elif( hands[p1randNum] == ( "scissor" ) and ( hands[p2randNum] == ( "scissor" ) ) ):
      print( "\t=\t"
        , "TIE"
        , sep = ( " " )
        , end = ( "\n" ) )
      tie = tie + 1
    elif( hands[p1randNum] == ( "lizard" ) and ( hands[p2randNum] == ( "lizard" ) ) ):
      print( "\t=\t"
        , "TIE"
        , sep = ( " " )
        , end = ( "\n" ) )
      tie = tie + 1
    elif( hands[p1randNum] == ( "spock" ) and ( hands[p2randNum] == ( "spock" ) ) ):
      print( "\t=\t"
        , "TIE"
        , sep = ( " " )
        , end = ( "\n" ) )
      tie = tie + 1
    elif( hands[p1randNum] == ( "rock" ) and ( hands[p2randNum] == ( "paper" ) ) ):
      print( "\t=\t"
        , "PAPER"
        , sep = ( " " )
        , end = ( "\n" ) )
      paperWins = paperWins + 1
    elif( hands[p1randNum] == ( "rock" ) and ( hands[p2randNum] == ( "scissor" ) ) ):
      print( "\t=\t"
        , "ROCK"
        , sep = ( " " )
        , end = ( "\n" ) )
      rockWins = rockWins + 1
    elif( hands[p1randNum] == ( "rock" ) and ( hands[p2randNum] == ( "lizard" ) ) ):
      print( "\t=\t"
        , "ROCK"
        , sep = ( " " )
        , end = ( "\n" ) )
      rockWins = rockWins + 1
    elif( hands[p1randNum] == ( "rock" ) and ( hands[p2randNum] == ( "spock" ) ) ):
      print( "\t=\t"
        , "SPOCK"
        , sep = ( " " )
        , end = ( "\n" ) )
      spockWins = spockWins + 1
    elif( hands[p1randNum] == ( "paper" ) and ( hands[p2randNum] == ( "rock" ) ) ):
      print( "\t=\t"
        , "PAPER"
        , sep = ( " " )
        , end = ( "\n" ) )
      paperWins = paperWins + 1
    elif( hands[p1randNum] == ( "paper" ) and ( hands[p2randNum] == ( "scissor" ) ) ):
      print( "\t=\t"
        , "SCISSOR"
        , sep = ( " " )
        , end = ( "\n" ) )
      scissorWins = scissorWins + 1
    elif( hands[p1randNum] == ( "paper" ) and ( hands[p2randNum] == ( "spock" ) ) ):
      print( "\t=\t"
        , "PAPER"
        , sep = ( " " )
        , end = ( "\n" ) )
      paperWins = paperWins + 1
    elif( hands[p1randNum] == ( "paper" ) and ( hands[p2randNum] == ( "lizard" ) ) ):
      print( "\t=\t"
        , "LIZARD"
        , sep = ( " " )
        , end = ( "\n" ) )
      lizardWins = lizardWins + 1
    elif( hands[p1randNum] == ( "scissor" ) and ( hands[p2randNum] == ( "rock" ) ) ):
      print( "\t=\t"
        , "ROCK"
        , sep = ( " " )
        , end = ( "\n" ) )
      rockWins = rockWins + 1
    elif( hands[p1randNum] == ( "scissor" ) and ( hands[p2randNum] == ( "paper" ) ) ):
      print( "\t=\t"
        , "SCISSOR"
        , sep = ( " " )
        , end = ( "\n" ) )
      scissorWins = scissorWins + 1
    elif( hands[p1randNum] == ( "scissor" ) and ( hands[p2randNum] == ( "lizard" ) ) ):
      print( "\t=\t"
        , "SCISSOR"
        , sep = ( " " )
        , end = ( "\n" ) )
      scissorWins = scissorWins + 1
    elif( hands[p1randNum] == ( "scissor" ) and ( hands[p2randNum] == ( "spock" ) ) ):
      print( "\t=\t"
        , "SPOCK"
        , sep = ( " " )
        , end = ( "\n" ) )
      spockWins = spockWins + 1
    elif( hands[p1randNum] == ( "lizard" ) and ( hands[p2randNum] == ( "rock" ) ) ):
      print( "\t=\t"
        , "ROCK"
        , sep = ( " " )
        , end = ( "\n" ) )
      rockWins = rockWins + 1
    elif( hands[p1randNum] == ( "lizard" ) and ( hands[p2randNum] == ( "paper" ) ) ):
      print( "\t=\t"
        , "LIZARD"
        , sep = ( " " )
        , end = ( "\n" ) )
      lizardWins = lizardWins + 1
    elif( hands[p1randNum] == ( "lizard" ) and ( hands[p2randNum] == ( "scissor" ) ) ):
      print( "\t=\t"
        , "SCISSOR"
        , sep = ( " " )
        , end = ( "\n" ) )
      scissorWins = scissorWins + 1
    elif( hands[p1randNum] == ( "lizard" ) and ( hands[p2randNum] == ( "spock" ) ) ):
      print( "\t=\t"
        , "LIZARD"
        , sep = ( " " )
        , end = ( "\n" ) )
      scissorWins = scissorWins + 1
    elif( hands[p1randNum] == ( "spock" ) and ( hands[p2randNum] == ( "rock" ) ) ):
      print( "\t=\t"
        , "SPOCK"
        , sep = ( " " )
        , end = ( "\n" ) )
      spockWins = spockWins + 1
    elif( hands[p1randNum] == ( "spock" ) and ( hands[p2randNum] == ( "paper" ) ) ):
      print( "\t=\t"
        , "PAPER"
        , sep = ( " " )
        , end = ( "\n" ) )
      paperWins = paperWins + 1
    elif( hands[p1randNum] == ( "spock" ) and ( hands[p2randNum] == ( "scissor" ) ) ):
      print( "\t=\t"
        , "SPOCK"
        , sep = ( " " )
        , end = ( "\n" ) )
      spockWins = spockWins + 1
    elif( hands[p1randNum] == ( "spock" ) and ( hands[p2randNum] == ( "lizard" ) ) ):
      print( "\t=\t"
        , "LIZARD"
        , sep = ( " " )
        , end = ( "\n" ) )
      lizardWins = lizardWins + 1
    else:
      print( "UNKNOWN" )

  print( "\n\nTotal Games Played:\t", (rockWins + paperWins + scissorWins + lizardWins + spockWins + tie ) )
  print( "Total Rock Wins:\t", int( rockWins ) )
  print( "Total Paper Wins:\t", int( paperWins ) )
  print( "Total Scissor Wins:\t", int( scissorWins ) )
  print( "Total Lizard Wins:\t", int( lizardWins ) )
  print( "Total Spock Wins:\t", int( spockWins ) )
  print( "Total Ties:\t\t", int( tie ) )
  print( "\n", end = ( "" ) )
    
if( __name__ == ( "__main__" ) ):
  main( )
