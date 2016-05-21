#!/usr/bin/env python3

import os
import platform
import random
import time

def clearScreen( ):
  if( platform.system( ) == "Windows" ):
    os.system( "cls" )
  else:
    os.system( "clear" )

def main( ):

  isPlayAgain = ( True )

  while( isPlayAgain ):

    lives = ( 10 )
    chosenWord = ( "" )
    letterList = []
    charList = []
    i = ( 0 )
    isWin = ( True )

    words = { "superstitious" 
               : "someone who believes things that are not likely", 
              "wonderful" 
               : "when something is amazing and...", 
              "spontaneous" 
               : "when you do something without planning", 
              "acceleration" 
               : "when you speed up..",
              "miraculous" 
               : "when god intervenes", 
              "acclaimed" 
               : "achieving highest accolades", 
              "intervened" 
               : "interfering with a negative behavior",
              "withstand" 
               : "to test your resiliency", 
              "heavenly" 
               : "where you go after your life", 
              "investigated" 
               : "to look deeper into",  
              "sinful" 
               : "when you do something really bad", 
              "nightingale" 
               : "a beautiful bird", 
              "joyful" 
               : "when you are overly happy", 
              "happiness" 
               : "when you are content in life", 
              "boasting" 
               : "when you highly speak about yourself",
          }

    randNum = ( random.randrange( 0, len( words ), 1 ) )

    for word in words.items( ):
      if( i == ( randNum ) ):
        chosenWord = ( word[0] )
        chosenWord = ( chosenWord.lower( ) )
        hint = ( word[1] )
        hint = ( hint.title( ) )
      i = ( i + 1 )

    for i in chosenWord:
      charList.append( i )

    while( True ):
      lives -= ( 1 )

      if( lives <= ( 0 ) ):
        print( "You lost! Secret word was: \"", chosenWord.capitalize( ), "\"", sep = ( '' ), end = ( '\n' ) )
        break

      isWin = ( True )
      clearScreen( )

      print( "\n*** - Hangman 1.0 by Armond Sarkisian - ***" )
      print( "-------------------------------------------\n", sep = ( '' ), end = ( '\n' ) )

      print( "Tries Left: (", lives, ')', sep = ( '' ), end = ( '\n' ) )
      print( "Secret Word: ", sep = ( '' ), end = ( '' ) )
      for i in range( 0, len( charList ), 1 ):
        print( chosenWord[i] if( charList[i] == ( '*' ) ) else ( '*' ), sep = ( "" ), end = ( "" ) )

      print( "\nHint: ", ( hint ) )

      letters = ( input( "\nEnter letter(s) to guess: " ) )

      if( not letters ):
        break
      elif( not letters.isalpha( ) ):
        continue

      letters = ( letters.lower( ) )

      for i in letters:
        letterList.append( i )
   
      for x in range( 0, len( charList ), 1 ):
        for y in range( 0, len( letterList ), 1 ): 
          if( letterList[y] == ( charList[x] ) ):
            #print( "Match found for: ", charList[x] )
            charList[x] = ( '*' )

      for x in charList:
        if( x != ( '*' ) ):
          isWin = ( False )
        
      if( isWin ):
        if( lives >= ( 9 ) ):
          print( "\nVery impressive! You won on your very first attempt. Great job! " ) 
        elif( lives >= ( 8 ) ):
          print( "\nWow, you won on your second attempt. Great job! " )
        elif( lives >= ( 7 ) ):
          print( "\nImpressive. You are very good at this. Good job! " )
        elif( lives >= ( 6 ) ):
          print( "\nWell done! You got it with only a few tries. " )
        elif( lives >= ( 4 ) ):
          print( "\nYou won! " )
        elif( lives >= ( 1 ) ):
          print( "\nYou won but try to guess the correct word with fewer tries " )

        print( "\nSecret word is: \"", chosenWord.capitalize( ), "\"\n", sep = ( '' ), end = ( '' ) )
        break

      time.sleep( 1 )

    while( True ):
      isPlayAgain = ( input( "\nPlay again? (Y/N): " ) )
      isPlayAgain = ( isPlayAgain.lower( ) )

      if( isPlayAgain == ( 'y' )
       or isPlayAgain == ( "yes" )
       or isPlayAgain == ( "yessiree" )
       or isPlayAgain == ( "of course" )
       or isPlayAgain == ( "ofcourse" )
       or isPlayAgain == ( "sure" )
       or isPlayAgain == ( "yep" )
       or isPlayAgain == ( "ok" ) ):
        isPlayAgain = ( True )
        break
      elif( isPlayAgain == ( 'n' )
       or isPlayAgain == ( "no" )
       or isPlayAgain == ( "naw" )
       or isPlayAgain == ( "nope" )
       or isPlayAgain == ( "na" )
       or isPlayAgain == ( "never" )
       or isPlayAgain == ( "nono" )
       or isPlayAgain == ( "nah" )
       or isPlayAgain == ( "naw" ) ): 
        isPlayAgain = ( False )
        break
      else:
        continue

      if( not isPlayAgain ):
        quit( )
      elif( not letters.isalpha( ) ):
        break

if( __name__ == ( "__main__" ) ):
  main( )
