#!/usr/bin/env python3

from random import randrange

def main( ):

  # get users input
  userString = ( input( "Enter a sentence to scramble: " ) )

  # build an array by converting the string to a list
  tmpArray = ( userString.split( ' ' ) )

  # the list which we will form with the scrambled words
  finalArray = []

  # traverse through all the words
  for i in range( 0, len( tmpArray ), 1 ):

    # convert word to char list to make necessary modifications
    charList = ( list( tmpArray[i] ) )

    # traverse through all the characters
    for y in range( 0, len( charList ), 1 ):

      while True:
        # get a random number from 0, to length of string
        randNum = ( randrange( 0, len( charList ), 1 ) )

        if( charList[randNum] != ( '|' )  ):
          break;

      # copy the random letter to the finalArray
      finalArray.append( charList[randNum] )

      # turn off the character just used
      charList[randNum] = '|'

    # add 1 space inbetween every word
    finalArray.append( ' ' )

  # convert finalArray back to finalString with no additional spaces
  finalString = ( ''.join( finalArray ) )

  # display the scrambled text
  print( finalString )

if( __name__ == ( "__main__" ) ):
  main( )
