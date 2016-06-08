from sys import argv
from random import randint
from random import sample
from random import seed
import base64

def main( ):

  isAlpha = ( False )
  isNumeric = ( False )
  isUpperCase = ( False )
  isLowerCase = ( False )
  isPunctuation = ( False )
  isEncrypt = ( False )
  isDecrypt = ( False )
  isGetLength = ( False )

  pwLength = ( 0 )
  numOfOptions = ( 0 )

  print( "\nNetwork Password Generator" )
  print( "~~~~~~~~~~~~~~~~~~~~~~~~~~\n" )

  try:
    if( len( argv ) > ( 1 ) ):
      for i in range( 0, len( argv ), 1 ):
        if( argv[i] == ( "--alpha" ) ):
          isAlpha = ( True )
        elif( argv[i] == ( "--num" ) ):
          isNumeric = ( True )
        elif( argv[i] == ( "--ucase" ) ):
          isUpperCase = ( True )
        elif( argv[i] == ( "--lcase" ) ):
          isLowerCase = ( True )
        elif( argv[i] == ( "--punc" ) ):
          isPunctuation = ( True )
        elif( argv[i].isnumeric( ) ):
          if( isGetLength ):
            raise ValueError( "You can only specify length once!" )
          pwLength = ( int( argv[i] ) )
          isGetLength = ( True )
        elif( argv[i] == ( "--enc" ) ):
          isEncrypt = ( True )
        elif( "--dec=" in argv[i] ):
          isDecrypt = ( True )
          tmpString = ( str( argv[i][6:] ) )
          print( "Encoded String:\t\t", tmpString )
          decryptStr = ( "".join( map( chr, base64.b64decode( bytes( tmpString, "utf-8" ) ) ) ) )
          print( "Decoded String:\t\t", decryptStr, '\n' )
          quit( )

      if( pwLength == ( 0 ) ):
        raise ValueError( "Password length should be specified!" )
      elif( pwLength < ( 3 ) ):
        raise ValueError( "Password length should be at least 3 characters!" )
      elif( pwLength > ( 50 ) ):
        raise ValueError( "Password length should not exceed 50 characters!" ) 
      elif( ( isAlpha and not isUpperCase ) and ( isAlpha and not isLowerCase ) ):
        raise ValueError( "Must specify either uppercase or lowercase letters!" )
      elif( ( isUpperCase and not isAlpha ) or ( isLowerCase and not isAlpha ) ):
        raise ValueError( "Must specify the alpha switch!" )
      elif( not isAlpha and not isNumeric and not isPunctuation ):
        raise ValueError( "Please specify options such as alpha, number, puctuation" )
    else:
      raise ValueError( "No arguments provided!" )
  except ValueError as e:
    print( "Exception:", e )
    print( "\n# \t\t= specify the length of the password" )
    print( "--alpha \t= enable alpha characters" )
    print( " --lcase \t= allow lowercase characters" )
    print( " --ucase \t= allow uppercase characters" )
    print( "--num \t\t= enable numbers" )
    print( "--punc \t\t= enable punctuations" )
    print( "--enc \t\t= encode password using base64 encryption" )
    print( "--dec=string\t= decode string using base64 decryption" )
    print( "\nUsage: python3 pwgen.py [{--alpha}[--lcase][--ucase]] [--enc] [--dec=string] [--num] [--punc]" )
    print( "\nExample: python3 pwgen.py 25 --alpha --lcase --num" )
    print( "Example: python3 pwgen.py 10 --alpha --ucase --punc" )
    print( "Example: python3 pwgen.py 30 --num --enc" )
    print( "Example: python3 pwgen.py --dec=ZnJ2\n" ) 
    quit( )

  # determine the number of arguments supplied
  if( isAlpha and isLowerCase ):
    numOfOptions = ( numOfOptions + 1 )

  if( isAlpha and isUpperCase ):
    numOfOptions = ( numOfOptions + 1 )

  if( isNumeric ):
    numOfOptions = ( numOfOptions + 1 )

  if( isPunctuation ):
    numOfOptions = ( numOfOptions + 1 )

  alphaUpperList = ( 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' )

  alphaLowerList = ( 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' )

  numberList = ( '1', '2', '3', '4', '5', '6', '7', '8', '9' )

  puncList = ( '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '`', '~', ',', '<', '.', '>', '/', '?', ';', '\'', '\"', '\\', ':', '[', '{', ']', '}', '|' )

  seed( )

  mainPassword = ( "" )
  tempPassword = ( "" )

  if( isNumeric ):
    for i in range( 0, pwLength, 1 ):
      randVal = ( randint( 0, len( numberList ) - 1 ) )
      tempPassword += ( numberList[randVal] )
  if( isAlpha and isLowerCase ):
    for i in range( 0, pwLength, 1 ):
      randVal = ( randint( 0, len( alphaLowerList ) - 1 ) )
      tempPassword += ( alphaLowerList[randVal] )
  if( isAlpha and isUpperCase ):
    for i in range( 0, pwLength, 1 ):
      randVal = ( randint( 0, len( alphaUpperList ) - 1 ) )
      tempPassword += ( alphaUpperList[randVal] )
  if( isPunctuation ):
    for i in range( 0, pwLength, 1 ):
      randVal = ( randint( 0, len( puncList ) - 1 ) )
      tempPassword += ( puncList[randVal] )

  temp = ( sample( tempPassword , pwLength ) )

  # join the list password into a string password
  for i in temp:
    mainPassword += ( str( i ) )

  if( isEncrypt ):
    print( "Generated Password:\t", mainPassword )
    mainPassword = ( base64.b64encode( bytes( mainPassword, "utf-8" ) ) )
    print( "Encoded Password:\t", mainPassword, '\n' )
  else:
    print( "Generated Password:\t", mainPassword, '\n' )

if( __name__ == ( "__main__" ) ):
  main( )
