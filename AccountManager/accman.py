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
isSave = ( False )
isSearch = ( False )

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
  print( "\n\n\nNetwork Account Manager\n~~~~~~~~~~~~~~~~~~~~~~~" )
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
  global isSave
  global pwLength 
  global numOfOptions 
  global outputFile 

  pythonVersion     = ( "python3" )
  appName           = ( "accman.py" )
  lengthSwitch      = ( "#" )
  alphaSwitch       = ( "--alpha" )
  lowerCaseSwitch   = ( "--lcase" )
  upperCaseSwitch   = ( "--ucase" )
  numberSwitch      = ( "--num" )
  punctuationSwitch = ( "--punc" )
  encryptSwitch     = ( "--enc" )
  decryptSwitch     = ( "--dec=" )
  outputFileSwitch  = ( "--outfile=" )
  saveSwitch        = ( "--save" )

  try: 
    if( len( argv ) > ( 1 ) ): 
      for i in range( 0, len( argv ), 1 ): 
        if( argv[i] == ( alphaSwitch ) ): 
          if( isAlpha ): 
            print( "\nWarning: You should only specify {} once!".format( alphaSwitch ) )
          isAlpha = ( True ) 
        elif( argv[i] == ( numberSwitch ) ): 
          if( isNumeric ): 
            print( "\nWarning: You should only specify {} once!".format( numberSwitch ) ) 
          isNumeric = ( True ) 
        elif( argv[i] == ( upperCaseSwitch ) ): 
          if( isUpperCase ): 
            print( "\nWarning: You should can only specify {} once!".format( upperCaseSwitch ) ) 
          isUpperCase = ( True ) 
        elif( argv[i] == ( lowerCaseSwitch ) ): 
          if( isLowerCase ): 
            print( "\nWarning: You should only specify {} once!".format( lowerCaseSwitch ) ) 
          isLowerCase = ( True ) 
        elif( argv[i] == ( punctuationSwitch ) ): 
          if( isPunctuation ):
            print( "\nWarning: You should only specify {} once!".format( punctuationSwitch ) )
          isPunctuation = ( True )
        elif( argv[i].isnumeric( ) ):
          if( isGetLength ):
            raise ValueError( "You can only specify length once!" )
          pwLength = ( int( argv[i] ) )
          isGetLength = ( True )
        elif( argv[i] == ( encryptSwitch ) ):
          if( isEncrypt ):
            print( "\nWarning: You should only specify {} once!".format( encryptSwitch ) )
          isEncrypt = ( True )
        elif( outputFileSwitch in argv[i] ):
          if( isOutputFile ):
            raise ValueError( "You can only specify {} once!".format( outputFileSwitch ) )
          isOutputFile = ( True )
          outputFile = ( str( argv[i][10:] ) )
        elif( argv[i] == ( saveSwitch ) ):
          if( isSave ):
            raise ValueError( "You can only specify {} once!".format( saveSwitch ) )
          isSave = ( True )
          if( not isOutputFile ):
            while( True ):
              outputFile = ( input( "Enter filename to save: " ) )
              outputFile = ( outputFile.strip( ) )
              if( outputFile ):
                break
          else:
            print( "\nWarning: You should specify either {} or {}!".format( saveSwitch, outputFileSwitch ) )
        elif( decryptSwitch in argv[i] ):
          if( isDecrypt ):
            print( "\nWarning: You should only specify {} once!".format( decryptSwitch ) )
          isDecrypt = ( True )
          tmpString = ( str( argv[i][6:] ) )
          print( "\nEncoded String:\t\t", tmpString )
          decryptStr = ( "".join( map( chr, base64.b64decode( bytes( tmpString, "utf-8" ) ) ) ) )
          print( "Decoded String:\t\t", decryptStr, '\n' )
          quit( )

      # switch rules
      if( pwLength == ( 0 ) ):
        raise ValueError( "Password length should be specified!" )
      elif( pwLength < ( 3 ) ):
        raise ValueError( "Password length should be at least 3 characters!" )
      elif( pwLength > ( 50 ) ):
        raise ValueError( "Password length should not exceed 50 characters!" ) 
      elif( ( isAlpha and not isUpperCase ) and ( isAlpha and not isLowerCase ) ):
        raise ValueError( "Please also specify either {} or {}!".format( upperCaseSwitch, lowerCaseSwitch ) )
      elif( isOutputFile ):
        if( len( outputFile ) > ( 20 ) ):
          raise ValueError( "Output file name should not exceed 20 characters!" )
      elif( ( isUpperCase and not isAlpha ) or ( isLowerCase and not isAlpha ) ):
        raise ValueError( "Please also specify the {} switch!".format( alphaSwitch ) )
      elif( not isAlpha and not isNumeric and not isPunctuation ):
        raise ValueError( "Please specify encoding options!" )
    else:
      raise ValueError( "No arguments provided!" )
  except ValueError as e:
    print( "\n=> Exception:", e )
    print( "\n{} \t\t= specify the length of the password".format( lengthSwitch ) )
    print( "{} \t= enable alpha characters".format( alphaSwitch ) )
    print( " {} \t= allow lowercase characters".format( lowerCaseSwitch ) )
    print( " {} \t= allow uppercase characters".format( upperCaseSwitch ) )
    print( "{} \t\t= enable numbers".format( numberSwitch ) )
    print( "{} \t\t= enable punctuations".format( punctuationSwitch ) )
    print( "{} \t\t= encode password using base64 encryption".format( encryptSwitch ) )
    print( "{}string \t= decode string using base64 decryption".format( decryptSwitch ) )
    print( "{}file \t= store the password in a json file".format( outputFileSwitch ) )
    print( "{} \t\t= prompt to store the password in a json file".format( saveSwitch ) )
    print( "\nUsage: {} {} {} [{} [{} | {}]] [{} | {}string] [{} | {}] [{}file | {}]]".format( pythonVersion, appName, lengthSwitch, alphaSwitch, lowerCaseSwitch, upperCaseSwitch, encryptSwitch, decryptSwitch, numberSwitch, punctuationSwitch, outputFileSwitch, saveSwitch ) )
    print( "\nExample: {} {} 25 {} {} {}".format( pythonVersion, appName, alphaSwitch, lowerCaseSwitch, numberSwitch ) )
    print( "Example: {} {} 10 {} {} {}".format( pythonVersion, appName, alphaSwitch, upperCaseSwitch, punctuationSwitch ) )
    print( "Example: {} {} 30 {} {} {}".format( pythonVersion, appName, numberSwitch, encryptSwitch, saveSwitch ) )
    print( "Example: {} {} {}ZnJ2".format( pythonVersion, appName, decryptSwitch ) )
    print( "Example: {} {} 5 {} {}file.dat".format( pythonVersion, appName, numberSwitch, outputFileSwitch ) ) 
    print( )
    quit( )

  # determine the number of arguments supplied
  if( isAlpha and isLowerCase ):
    numOfOptions = ( numOfOptions + 2 )

  if( isAlpha and isUpperCase ):
    numOfOptions = ( numOfOptions + 2 )

  if( isNumeric ):
    numOfOptions = ( numOfOptions + 1 )

  if( isPunctuation ):
    numOfOptions = ( numOfOptions + 1 )

  if( isEncrypt ):
    numOfOptions = ( numOfOptions + 1 )

  if( isDecrypt ):
    numOfOptions = ( numOfOptions + 1 )

  if( isOutputFile ):
    numOfOptions = ( numOfOptions + 1 )

  if( isSearch ):
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
    print( "\nGenerated Password:\t =>  ", mainPassword )
    encodedPassword = ( base64.b64encode( bytes( mainPassword, "utf-8" ) ) )
    encodedPassword = ( encodedPassword.decode( "utf-8" ) )
    print( "Encrypted Password:\t =>  ", encodedPassword, '\n' )
  else:
    print( "\nGenerated Password:\t =>  ", mainPassword, '\n' )

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
  if( isOutputFile or isSave ):
    un = ( "" )
    email = ( "" )
    url = ( "" )
    notes = ( "" )

    while( True ):
      un = ( input( "Enter username or s to skip: " ) )
      if( un.strip( ).lower( ) == ( 's' ) ):
        un = ( "" )
        break
      elif( len( un ) > ( 75 ) or len( un ) < ( 3 ) ):
        print( "Username should not be less than 3 characters and also not exceed 75 characters!" )
        continue
      elif( un ):
        break
    while( True ):
      email = ( input( "Enter email address or s to skip: " ) )
      if( email.strip( ).lower( ) == ( 's' ) ):
        email = ( "" )
        break
      elif( len( email ) > ( 75 ) or len( email ) < ( 5 ) ):
        print( "Email address should not be less than 5 characters and also not exceed 75 characters!" )
        continue
      elif( email ):
        break
    while( True ):
      url = ( input( "Enter URL/IP or s to skip: " ) )
      if( url.strip( ).lower( ) == ( 's' ) ):
        url = ( "" )
        break
      elif( len( url ) > ( 125 ) or len( url ) < ( 5 ) ):
        print( "URL should not be less than 5 characters and also not exceed 125 characters!" )
        continue
      elif( url ):
        break
    while( True ):
      notes = ( input( "Enter description or s to skip: " ) )
      if( notes.strip( ).lower( ) == ( 's' ) ):
        notes = ( "" )
        break
      elif( len( notes ) > ( 250 ) or len( notes ) < ( 4 ) ):
        print( "Description should not be less than 4 characters and also not exceed 250 characters!" )
        continue
      elif( notes ):
        break

    tmpJson = { "DESCRIPTION" : notes.strip( ), "ENCODED PW" : encodedPassword, "RAW PW" : mainPassword, "URL/IP" : url.strip( ), "EMAIL" : email.strip( ), "USER" : un.strip( ),  }
    tmp_new = ( json.dumps( tmpJson ) )
    converted_new = ( tmp_new.replace( "\'", "\"" ) )
    jsonOutput_new = ( json.loads( tmp_new ) )

    isReadFile = ( False )

    jsonOutput = []
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
