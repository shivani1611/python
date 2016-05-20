#!/usr/bin/env python3

# Get filename from user and search for their chosen word and the frequency

def main( ):
  fileName = ( input( "Enter filename to open: " ) )
  fileLine = ( "" )

  try:
    fileObj = ( open( fileName, 'r' ) )
  except IOError as e:
    print( "Could not open file: ", e )
    exit( )

  for i in fileObj:
    fileLine += ( i )

  while True:
    searchWord = ( input( "Enter word to search: " ) )

    if( not searchWord ):
      break

    if( fileLine.count( searchWord ) <= ( 0 ) ):
      print( "No match found for \"", searchWord, "\"", sep = ( "" ) )
    else:
      print( fileLine.count( searchWord ),\
      " match found for \"", searchWord, "\"", sep = ( "" ) )

  fileObj.close( )

if( __name__ == ( "__main__" ) ):
  main( )
