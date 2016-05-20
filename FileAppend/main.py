#!/usr/bin/env python3

def main( ):

  while( True ):
    fileName = ( input( "Enter filename to write/append or enter to quit: " ) )
    if( not fileName ):
      break
 
    while( True ):
      fileContent = ( input( "Enter some words: " ) )
      if( fileContent ):
        break

    wordList = ( fileContent.split( ' ' ) )

    try:
      fileObj = ( open( fileName, "a+" ) )
    except IOError as e:
      print( "Error with File IO: ", e )
      quit( )

    with fileObj:
      for i in wordList:
        try:
          fileObj.write( i + '\n' )
        except IOError as e:
          print( "Unable to write to file: ", e )

    fileObj.close( )

if( __name__ == ( "__main__" ) ):
  main( )
