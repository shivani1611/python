#!/usr/bin/env python3

# get all x letter words from file.txt and export to x.txt

def main( ):
  fileLine = ( "" )
  allWords = []

  fileName = ( input( "Enter filename to read from: " ) )
  while( not fileName ):
    fileName = ( input( "Enter filename to read from: " ) )

  try:
    fileObj = ( open( fileName, 'r' ) )
  except IOError as e:
    print( "File I/O error: ", e )
    quit( )

  # gather all words from the file
  for i in fileObj:
    fileLine += ( i )

  allWords = ( fileLine.split( ' ' ) )

  for i in allWords:
    if( len( i ) >= 8 ):
      fileObj = ( open( "8.txt", 'a' ) )
      fileObj.write( i + '\n' )
      fileObj.close( )
    elif( len( i ) >= 7 ):
      fileObj = ( open( "7.txt", 'a' ) )
      fileObj.write( i + '\n' )
      fileObj.close( )
    elif( len( i ) >= 6 ):
      fileObj = ( open( "6.txt", 'a' ) )
      fileObj.write( i + '\n' )
      fileObj.close( )
    elif( len( i ) >= 5 ):
      fileObj = ( open( "5.txt", 'a' ) )
      fileObj.write( i + '\n' )
      fileObj.close( )
    elif( len( i ) >= 4 ):
      fileObj = ( open( "4.txt", 'a' ) )
      fileObj.write( i + '\n' )
      fileObj.close( )
    elif( len( i ) >= 3 ):
      fileObj = ( open( "3.txt", 'a' ) )
      fileObj.write( i + '\n' )
      fileObj.close( )
    elif( len( i ) >= 1 ):
      fileObj = ( open( "1-2.txt", 'a' ) )
      fileObj.write( i + '\n' )
      fileObj.close( )
    
if( __name__ == ( "__main__" ) ):
  main( )
