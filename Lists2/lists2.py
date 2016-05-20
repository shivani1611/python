#!/usr/bin/env python3

# get files from the user specified file, check their length and if length > x, store the
# words in a new sorted list which then you will have the user search for words in the new
# list

def main( ):
  fileName = ( input( "Enter filename to open: " ) )
  fileLine = ( "" )
  wordLength = ( int( input( "Min word size to gather: " ) ) )
  allWords = []
  bigWords = []

  fileObj = ( open( fileName, 'r' ) )

  for i in fileObj:
    fileLine += ( i )

  allWords = ( fileLine.split( ' ' )  )

  for i in allWords:
    if( len( i ) > ( wordLength ) ):
      bigWords.append( i )

  for i in bigWords:
    print( i )

  while True:
    wordSearch = ( input( "Enter word to search for: " ) )

    if( not wordSearch ):
      break
    elif( wordSearch in bigWords ):
      print( "\"", wordSearch, "\" found!", sep = ( "" ), end = ( "\n" ) )

if( __name__ == ( "__main__" ) ):
  main( )
