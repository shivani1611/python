#!/usr/bin/env python3

def bubbleSort( li ):
  for x in range( len( li ) ):
    for y in range( len( li ) -1 ):
      if( li[y] > ( li[y + 1] ) ):
        strBuffer = ( li[y] )
        li[y] = ( li[y + 1] )
        li[y + 1] = ( strBuffer )

def main( ):

  try:
    fileObj = ( open( "file.txt", 'r' ) )
  except IOError as e:
    print( "File open error: ", e )
    quit( )

  fileContents = fileObj.read( )
  fileObj.close( )

  words = ( fileContents.split( '\n' ) )
  bubbleSort( words )

  try:
    fileObj = ( open( "sorted.txt", 'w' ) )
  except IOError as e:
    print( "File create error: ", e )
    quit( )

  for i in words:
    fileObj.write( i + '\n' )

  fileObj.close( )

if( __name__ == ( "__main__" ) ):
  main( )
