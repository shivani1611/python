#!/usr/bin/env python3

########################################################################################################
#
# Author  : Armond Sarkisian
# Date    : July 2nd, 2016
# Title   : Network Account Manager
# Purpose : To maintain a record of all network device logins
#
########################################################################################################

########################################################################################################
from random import randint
from random import sample
from random import seed
from pprint import pprint
from sys import argv
import base64
import json
import os.path
import sys
import traceback
########################################################################################################

########################################################################################################
# Global Switches/Options
isAlpha = ( False )
isNumeric = ( False )
isUpperCase = ( False )
isLowerCase = ( False )
isPunctuation = ( False )
isEncrypt = ( False )
isDecrypt = ( False )
isGetLength = ( False )
isOutputFile = ( False )

pwLength = ( 0 )
numOfOptions = ( 0 )
outputFile = ( "" )

# Global Constants
ALPHAUPPERLIST = ( 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' )
ALPHALOWERLIST = ( 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' )
NUMBERLIST = ( '1', '2', '3', '4', '5', '6', '7', '8', '9' )
PUNCLIST = ( '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '`', '~', ',', '<', '.', '>', '/', '?', ';', '\'', '\"', '\\', ':', '[', '{', ']', '}', '|' )
########################################################################################################

########################################################################################################
# Public: Display the title
#
# Examples
#
#   displayTitle( )
#   # => None
#
# Returns Nothing
def displayTitle( ):
  print( "\nNetwork Account Manager\n~~~~~~~~~~~~~~~~~~~~~~~" )
########################################################################################################

########################################################################################################
# Public: Validate all the arguments specified by the user
#
# Examples
#
#   validateArguments( )
#   # => None
#
# Returns Nothing
def validateArguments( ):
  global isAlpha
  global isNumeric
  global isUpperCase
  global isLowerCase
  global isPunctuation
  global isEncrypt
  global isDecrypt
  global isGetLength
  global isOutputFile

  global pwLength
  global numOfOptions
  global outputFile

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
        elif( "--outputfile=" in argv[i] ):
          isOutputFile = ( True )
          outputFile = ( str( argv[i][13:] ) )
        elif( "--dec=" in argv[i] ):
          isDecrypt = ( True )
          tmpString = ( str( argv[i][6:] ) )
          print( "Encoded String:\t\t", tmpString )
          decryptStr = ( "".join( map( chr, base64.b64decode( bytes( tmpString, "utf-8" ) ) ) ) )
          print( "Decoded String:\t\t", decryptStr, '\n' )

      # switch rules
      if( pwLength == ( 0 ) ):
        raise ValueError( "Password length should be specified!" )
      elif( pwLength < ( 3 ) ):
        raise ValueError( "Password length should be at least 3 characters!" )
      elif( pwLength > ( 50 ) ):
        raise ValueError( "Password length should not exceed 50 characters!" ) 
      elif( ( isAlpha and not isUpperCase ) and ( isAlpha and not isLowerCase ) ):
        raise ValueError( "Password will be blank. Please specify either --ucase or --lcase!" )
      elif( isOutputFile ):
        if( len( outputFile ) > ( 20 ) ):
          raise ValueError( "Output file name should not exceed 20 characters!" )
      elif( ( isUpperCase and not isAlpha ) or ( isLowerCase and not isAlpha ) ):
        raise ValueError( "Password will be blank. Please specify the --alpha switch!" )
      elif( not isAlpha and not isNumeric and not isPunctuation ):
        raise ValueError( "Password will be blank. Please specify options such as --alpha, --num, --punc" )
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
    print( "--outputfile=file\t= store the password in a json file" )
    print( "\nUsage: python3 accman.py [--alpha [--lcase | --ucase]] [--enc | --dec=string] [--num | --punc] [--outputfile=filename]]" )
    print( "\nExample: python3 accman.py 25 --alpha --lcase --num" )
    print( "Example: python3 accman.py 10 --alpha --ucase --punc" )
    print( "Example: python3 accman.py 30 --num --enc" )
    print( "Example: python3 accman.py --dec=ZnJ2" )
    print( "Example: python3 accman.py 5 --num --outputfile=filename\n" ) 
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
########################################################################################################

########################################################################################################
# Public: Generate the password based on the options provided by the user 
#
# Examples
#
#   generatePassword( )
#   # => "12345", "@^@^#2"
#
# Returns the main password as well as the encoded password
def generatePassword( ):
  global ALPHAUPPERLIST
  global ALPHALOWERLIST
  global NUMBERLIST
  global PUNCLIST

  # randomize
  seed( )

  mainPassword = ( "" )
  tempPassword = ( "" )
  encodedPassword = ( "" )

  if( isNumeric ):
    for i in range( 0, pwLength, 1 ):
      randVal = ( randint( 0, len( NUMBERLIST ) - 1 ) )
      tempPassword += ( NUMBERLIST[randVal] )
  if( isAlpha and isLowerCase ):
    for i in range( 0, pwLength, 1 ):
      randVal = ( randint( 0, len( ALPHALOWERLIST ) - 1 ) )
      tempPassword += ( ALPHALOWERLIST[randVal] )
  if( isAlpha and isUpperCase ):
    for i in range( 0, pwLength, 1 ):
      randVal = ( randint( 0, len( ALPHAUPPERLIST ) - 1 ) )
      tempPassword += ( ALPHAUPPERLIST[randVal] )
  if( isPunctuation ):
    for i in range( 0, pwLength, 1 ):
      randVal = ( randint( 0, len( PUNCLIST ) - 1 ) )
      tempPassword += ( PUNCLIST[randVal] )

  temp = ( sample( tempPassword , pwLength ) )

  # join the list password into a string password
  for i in temp:
    mainPassword += ( str( i ) )
 
  if( isEncrypt ):
    print( "Generated Password:\t", mainPassword )
    encodedPassword = ( base64.b64encode( bytes( mainPassword, "utf-8" ) ) )
    encodedPassword = ( encodedPassword.decode( "utf-8" ) )
    print( "Encrypted Password:\t", encodedPassword, '\n' )
  else:
    print( "Generated Password:\t", mainPassword, '\n' )

  return( mainPassword, encodedPassword )
########################################################################################################

########################################################################################################
# Public: Output content to specified file using json structure
#
# mainPassword  - The main generated password from generatePassword( )
# encodedPassword - The encoded password from generatePassword( )
#
# Examples
#
#   processOutputFile( '12345', '#@#sss' )
#   # => None
#
# Returns Nothing
def processOutputFile( mainPassword, encodedPassword ):
  if( isOutputFile ):
    un = ( "" )
    email = ( "" )
    url = ( "" )
    notes = ( "" )

    while( True ):
      un = ( input( "Enter username or s to skip: " ) )
      if( un.strip( ).lower( ) == ( 's' ) ):
        un = ( "" )
        break
      elif( len( un ) > ( 75 ) ):
        print( "Username should not exceed 75 characters!" )
        continue
      elif( un ):
        break
    while( True ):
      email = ( input( "Enter email address or s to skip: " ) )
      if( email.strip( ).lower( ) == ( 's' ) ):
        email = ( "" )
        break
      elif( len( email ) > ( 75 ) ):
        print( "Email address should not exceed 75 characters!" )
        continue
      elif( email ):
        break
    while( True ):
      url = ( input( "Enter URL/IP or s to skip: " ) )
      if( url.strip( ).lower( ) == ( 's' ) ):
        url = ( "" )
        break
      elif( len( url ) > ( 125 ) ):
        print( "URL should not exceed 125 characters!" )
        continue
      elif( url ):
        break
    while( True ):
      notes = ( input( "Enter description or s to skip: " ) )
      if( notes.strip( ).lower( ) == ( 's' ) ):
        notes = ( "" )
        break
      elif( len( notes ) > ( 250 ) ):
        print( "Description should not exceed 250 characters!" )
        continue
      elif( notes ):
        break

  # only perform these actions if the user selected to output the password to a file
  if( isOutputFile ):
    tmpJson = { "DESCRIPTION" : notes.strip( ), "ENCODED PW" : encodedPassword, "RAW PW" : mainPassword, "URL/IP" : url.strip( ), "EMAIL" : email.strip( ), "USER" : un.strip( ),  }
    tmp_new = ( json.dumps( tmpJson ) )
    converted_new = ( tmp_new.replace( "\'", "\"" ) )
    jsonOutput_new = ( json.loads( tmp_new ) )

    isReadFile = ( False )

    jsonOutput = []
    if( isOutputFile ):
      if( os.path.isfile( outputFile ) ):
        try:
          with open( outputFile, 'r' ) as readFile:
            isReadFile = ( True )
            jsonOutput_old = json.load( readFile )
            for i in jsonOutput_old:
              jsonOutput.append( i )
        except:
          print(  traceback.format_exc( ) )
          isReadFile = ( False )

    jsonOutput.append( jsonOutput_new )
    with open( outputFile, 'w' ) as fout:
      #pprint( jsonOutput, stream=fout ) # causing issue with single/double quotes with json
      json.dump( jsonOutput, fout )
########################################################################################################
  
########################################################################################################
# Public: Main entry point
#
# Examples
#
#   main( )
#   # => None
#
# Returns Nothing
def main( ):
  # display the title of the program
  displayTitle( )

  # verify what switches the user provided
  validateArguments( )

  # generate the password based on the user provided arguments
  mainPassword, encodedPassword = generatePassword( )

  # generate the output json file
  processOutputFile( mainPassword, encodedPassword )
########################################################################################################

########################################################################################################
if( __name__ == ( "__main__" ) ):
  main( )
########################################################################################################
