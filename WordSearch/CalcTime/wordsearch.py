def main( ):

  reservedWords = [ "armond", "syuzi" ]

  fileName = ( str( input( "Enter filename to read to: " ) ) )  
  fileObj = ( open( fileName, 'r' ) )
  fileLine = ( "" )
  lineCount = ( 0 )

  for i in fileObj:
    lineCount = lineCount + 1
    fileLine = ( i )
    for j in reservedWords:
      if( j in i ):
        print( "Keyword: \"", j, "\" found in line #: ", lineCount, sep = ( "" ), end = ( "\n" ) )
    #print( fileLine, end = ( "" ) )

  fileObj.close( )

if( __name__ == ( "__main__" ) ):
  main( )
