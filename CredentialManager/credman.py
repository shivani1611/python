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
from pprint import pprint
from random import randint
from random import sample
from random import seed
from sys import argv
import base64
import json
import os.path
import sys
import traceback
########################################################################################################

########################################################################################################
# Global Switches/Options
isAlpha       = ( False )
isNumeric     = ( False )
isUpperCase   = ( False )
isLowerCase   = ( False )
isPunctuation = ( False )
isEncrypt     = ( False )
isDecrypt     = ( False )
isGetLength   = ( False )
isOutputFile  = ( False )
isSave        = ( False )
isHelp        = ( False )

pwLength      = ( 0 )
numOfOptions  = ( 0 )
outputFile    = ( "" )

# Global Constants
ALPHAUPPERLIST = ( 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' )
ALPHALOWERLIST = ( 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' )
NUMBERLIST     = ( '1', '2', '3', '4', '5', '6', '7', '8', '9' )
PUNCLIST       = ( ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '`', '~', ',', '<', '.', '>', '/', '?', ';', '\'', '\"', '\\', ':', '[', '{', ']', '}', '|' )
DECKCARDLIST   = ( "\u2660", "\u2661", "\u2662", "\u2663", "\u2664", "\u2665", "\u2666", "\u2667" )
MATHLIST       = ( "\u0183", "\u0151", "/", "+", "-" )
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
  print( "\n\n\nNetwork Credential Manager By Armond Sarkisian\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" )
########################################################################################################

########################################################################################################
#def mainMenu( ):

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
  global isHelp

  global pwLength 
  global numOfOptions 
  global outputFile 

  pythonVersion     = ( "python3" )
  fileName          = ( "credman.py" )
  lengthSwitch      = ( "#" )
  helpSwitch        = ( "--help" )
  alphaSwitch       = ( "--alpha" )
  lowerCaseSwitch   = ( "--lcase" )
  upperCaseSwitch   = ( "--ucase" )
  numberSwitch      = ( "--num" )
  punctuationSwitch = ( "--punc" )
  encryptSwitch     = ( "--enc" )
  encryptSwitch2    = ( "--enc=" )
  decryptSwitch     = ( "--dec=" )
  outputFileSwitch  = ( "--outfile=" )
  saveSwitch        = ( "--save" )

  try: 
    if( len( argv ) > ( 1 ) ): 
      for i in range( 0, len( argv ), 1 ): 
        if( fileName in argv[i] ):
          pass
        elif( argv[i] == ( helpSwitch ) ):
          isHelp = ( True )
          raise ValueError( "None" )
        elif( argv[i] == ( alphaSwitch ) ): 
          if( isAlpha ): 
            print( "\nWarning: You should specify {} only once!".format( alphaSwitch ) )
          isAlpha = ( True ) 
        elif( argv[i] == ( numberSwitch ) ): 
          if( isNumeric ): 
            print( "\nWarning: You should specify {} only once!".format( numberSwitch ) ) 
          isNumeric = ( True ) 
        elif( argv[i] == ( upperCaseSwitch ) ): 
          if( isUpperCase ): 
            print( "\nWarning: You should specify {} only once!".format( upperCaseSwitch ) ) 
          isUpperCase = ( True ) 
        elif( argv[i] == ( lowerCaseSwitch ) ): 
          if( isLowerCase ): 
            print( "\nWarning: You should specify {} only once!".format( lowerCaseSwitch ) ) 
          isLowerCase = ( True ) 
        elif( argv[i] == ( punctuationSwitch ) ): 
          if( isPunctuation ):
            print( "\nWarning: You should specify {} only once!".format( punctuationSwitch ) )
          isPunctuation = ( True )
        elif( argv[i].isnumeric( ) ):
          if( isGetLength ):
            raise ValueError( "You can specify length only once!" )
          pwLength = ( int( argv[i] ) )
          isGetLength = ( True )
        elif( outputFileSwitch in argv[i] ):
          if( isOutputFile ):
            raise ValueError( "You can specify {} only once!".format( outputFileSwitch ) )
          outputFile = ( str( argv[i][10:] ) )
          isOutputFile = ( True )
        elif( argv[i] == ( saveSwitch ) ):
          if( isSave ):
            raise ValueError( "You can specify {} only once!".format( saveSwitch ) )
          isSave = ( True )
          if( not isOutputFile ):
            while( True ):
              outputFile = ( input( "Enter filename to save: " ) )
              outputFile = ( outputFile.strip( ) )
              if( outputFile ):
                break
          else:
            print( "\nWarning: You should specify either {} or {}!".format( saveSwitch, outputFileSwitch ) )
        elif( argv[i] == ( encryptSwitch ) ):
          if( isEncrypt ):
            print( "\nWarning: You should specify {} only once!".format( encryptSwitch ) )
          isEncrypt = ( True )
        elif( encryptSwitch2 in argv[i] ):
          if( isEncrypt ):
            print( "\nWarning: You should specify the encrypt switch only once!" )
          isEncrypt = ( True )
          tmpString = ( str( argv[i][6:] ) )
          print( "\nDecoded String:\t\t", tmpString )
          encryptStr = ( base64.b64encode( bytes( tmpString, "utf-8" ) ) )
          encryptStr = ( encryptStr.decode( "utf-8" ) )
          print( "Encoded String:\t\t", encryptStr, '\n' )
          quit( )
        elif( decryptSwitch in argv[i] ):
          if( isDecrypt ):
            print( "\nWarning: You should specify {} only once!".format( decryptSwitch ) )
          isDecrypt = ( True )
          tmpString = ( str( argv[i][6:] ) )
          print( "\nEncoded String:\t\t", tmpString )
          decryptStr = ( "".join( map( chr, base64.b64decode( bytes( tmpString, "utf-8" ) ) ) ) )
          print( "Decoded String:\t\t", decryptStr, '\n' )
          quit( )
        else:
          raise ValueError( "Invalid switch used!" )

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
    print( "{} \t\t= display the help menu".format( helpSwitch ) )
    print( "{} \t= allow alpha characters".format( alphaSwitch ) )
    print( "  {} \t= enable lowercase characters".format( lowerCaseSwitch ) )
    print( "  {} \t= enable uppercase characters".format( upperCaseSwitch ) )
    print( "{} \t\t= allow number characters".format( numberSwitch ) )
    print( "{} \t\t= allow punctuation characters".format( punctuationSwitch ) )
    print( "{} \t\t= encode password using base64 encryption".format( encryptSwitch ) )
    print( "{}string \t= encode string using base64 encryption".format( encryptSwitch2 ) )
    print( "{}string \t= decode string using base64 decryption".format( decryptSwitch ) )
    print( "{}file \t= store the password in a json file".format( outputFileSwitch ) )
    print( "{} \t\t= prompt to store the password in a json file".format( saveSwitch ) )
    print( "\nUsage: {} {} {} [{} [{} | {}]] [{} | {}string] [{} | {}] [{}file | {}]]".format( pythonVersion, fileName, lengthSwitch, alphaSwitch, lowerCaseSwitch, upperCaseSwitch, encryptSwitch, decryptSwitch, numberSwitch, punctuationSwitch, outputFileSwitch, saveSwitch ) )
    print( "\nExample: {} {} 25 {} {} {}".format( pythonVersion, fileName, alphaSwitch, lowerCaseSwitch, numberSwitch ) )
    print( "Example: {} {} 10 {} {} {}".format( pythonVersion, fileName, alphaSwitch, upperCaseSwitch, punctuationSwitch ) )
    print( "Example: {} {} 30 {} {} {}".format( pythonVersion, fileName, numberSwitch, encryptSwitch, saveSwitch ) )
    print( "Example: {} {} {}ZnJ2".format( pythonVersion, fileName, decryptSwitch ) )
    print( "Example: {} {} 5 {} {}file.dat".format( pythonVersion, fileName, numberSwitch, outputFileSwitch ) ) 
    print( )
    quit( )

  # determine the number of arguments supplied
  if( isHelp ):
    numOfOptions = ( numOfOptions + 1 )

  if( isGetLength ):
    numOfOptions = ( numOfOptions + 1 )

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
  elif( isDecrypt ):
    numOfOptions = ( numOfOptions + 1 )

  if( isOutputFile ):
    numOfOptions = ( numOfOptions + 1 )
  elif( isSave ):
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
  global DECKCARDLIST
  global MATHLIST

  print( "CODE: ", "\u0095" )
  print( "CODE: ", "\u0098" )
  print( "CODE: ", "\u0099" )
  print( "CODE: ", "\u0100" )
  print( "CODE: ", "\u0101" )
  print( "CODE: ", "\u0102" )
  print( "CODE: ", "\u0103" )
  print( "CODE: ", "\u0104" )
  print( "CODE: ", "\u0105" )
  print( "CODE: ", "\u0106" )
  print( "CODE: ", "\u0107" )
  print( "CODE: ", "\u0108" )
  print( "CODE: ", "\u0109" )
  print( "CODE: ", "\u0110" )
  print( "CODE: ", "\u0111" )
  print( "CODE: ", "\u0112" )
  print( "CODE: ", "\u0113" )
  print( "CODE: ", "\u0114" )
  print( "CODE: ", "\u0115" )
  print( "CODE: ", "\u0116" )
  print( "CODE: ", "\u0117" )
  print( "CODE: ", "\u0118" )
  print( "CODE: ", "\u0119" )
  print( "CODE: ", "\u0120" )
  print( "CODE: ", "\u0121" )
  print( "CODE: ", "\u0122" )
  print( "CODE: ", "\u0123" )
  print( "CODE: ", "\u0124" )
  print( "CODE: ", "\u0125" )
  print( "CODE: ", "\u0126" )
  print( "CODE: ", "\u0127" )
  print( "CODE: ", "\u0128" )
  print( "CODE: ", "\u0129" )
  print( "CODE: ", "\u0130" )
  print( "CODE: ", "\u0131" )
  print( "CODE: ", "\u0132" )
  print( "CODE: ", "\u0133" )
  print( "CODE: ", "\u0134" )
  print( "CODE: ", "\u0135" )
  print( "CODE: ", "\u0136" )
  print( "CODE: ", "\u0137" )
  print( "CODE: ", "\u0138" )
  print( "CODE: ", "\u0139" )
  print( "CODE: ", "\u0140" )
  print( "CODE: ", "\u0141" )
  print( "CODE: ", "\u0142" )
  print( "CODE: ", "\u0143" )
  print( "CODE: ", "\u0144" )
  print( "CODE: ", "\u0145" )
  print( "CODE: ", "\u0146" )
  print( "CODE: ", "\u0147" )
  print( "CODE: ", "\u0148" )
  print( "CODE: ", "\u0149" )
  print( "CODE: ", "\u0150" )
  print( "CODE: ", "\u0151" )
  print( "CODE: ", "\u0152" )
  print( "CODE: ", "\u0153" )
  print( "CODE: ", "\u0154" )
  print( "CODE: ", "\u0155" )
  print( "CODE: ", "\u0156" )
  print( "CODE: ", "\u0157" )
  print( "CODE: ", "\u0158" )
  print( "CODE: ", "\u0159" )
  print( "CODE: ", "\u0160" )
  print( "CODE: ", "\u0161" )
  print( "CODE: ", "\u0162" )
  print( "CODE: ", "\u0163" )
  print( "CODE: ", "\u0164" )
  print( "CODE: ", "\u0165" )
  print( "CODE: ", "\u0166" )
  print( "CODE: ", "\u0167" )
  print( "CODE: ", "\u0168" )
  print( "CODE: ", "\u0169" )
  print( "CODE: ", "\u0170" )
  print( "CODE: ", "\u0171" )
  print( "CODE: ", "\u0172" )
  print( "CODE: ", "\u0173" )
  print( "CODE: ", "\u0174" )
  print( "CODE: ", "\u0175" )
  print( "CODE: ", "\u0176" )
  print( "CODE: ", "\u0177" )
  print( "CODE: ", "\u0178" )
  print( "CODE: ", "\u0179" )
  print( "CODE: ", "\u0180" )
  print( "CODE: ", "\u0181" )
  print( "CODE: ", "\u0182" )
  print( "CODE: ", "\u0183" )
  print( "CODE: ", "\u0184" )
  print( "CODE: ", "\u0185" )
  print( "CODE: ", "\u0186" )
  print( "CODE: ", "\u0187" )
  print( "CODE: ", "\u0188" )
  print( "CODE: ", "\u0189" )
  print( "CODE: ", "\u0190" )
  print( "CODE: ", "\u0191" )
  print( "CODE: ", "\u0192" )
  print( "CODE: ", "\u0193" )
  print( "CODE: ", "\u0194" )
  print( "CODE: ", "\u0195" )
  print( "CODE: ", "\u0196" )
  print( "CODE: ", "\u0197" )
  print( "CODE: ", "\u0198" )
  print( "CODE: ", "\u0199" )
  print( "CODE: ", "\u0200" )
  print( "CODE: ", "\u0201" )
  print( "CODE: ", "\u0202" )
  print( "CODE: ", "\u0203" )
  print( "CODE: ", "\u0204" )
  print( "CODE: ", "\u0205" )
  print( "CODE: ", "\u0206" )
  print( "CODE: ", "\u0207" )
  print( "CODE: ", "\u0208" )
  print( "CODE: ", "\u0209" )
  print( "CODE: ", "\u0210" )
  print( "CODE: ", "\u0211" )
  print( "CODE: ", "\u0212" )
  print( "CODE: ", "\u0213" )
  print( "CODE: ", "\u0214" )
  print( "CODE: ", "\u0215" )
  print( "CODE: ", "\u0216" )
  print( "CODE: ", "\u0217" )
  print( "CODE: ", "\u0218" )
  print( "CODE: ", "\u0219" )
  print( "CODE: ", "\u0220" )
  print( "CODE: ", "\u0221" )
  print( "CODE: ", "\u0222" )
  print( "CODE: ", "\u0223" )
  print( "CODE: ", "\u0224" )
  print( "CODE: ", "\u0225" )
  print( "CODE: ", "\u0226" )
  print( "CODE: ", "\u0227" )
  print( "CODE: ", "\u0228" )
  print( "CODE: ", "\u0229" )
  print( "CODE: ", "\u0230" )
  print( "CODE: ", "\u0231" )
  print( "CODE: ", "\u0232" )
  print( "CODE: ", "\u0233" )
  print( "CODE: ", "\u0234" )
  print( "CODE: ", "\u0235" )
  print( "CODE: ", "\u0236" )
  print( "CODE: ", "\u0237" )
  print( "CODE: ", "\u0238" )
  print( "CODE: ", "\u0239" )
  print( "CODE: ", "\u0240" )
  print( "CODE: ", "\u0241" )
  print( "CODE: ", "\u0242" )
  print( "CODE: ", "\u0243" )
  print( "CODE: ", "\u0244" )
  print( "CODE: ", "\u0245" )
  print( "CODE: ", "\u0246" )
  print( "CODE: ", "\u0247" )
  print( "CODE: ", "\u0248" )
  print( "CODE: ", "\u0249" )
  print( "CODE: ", "\u0250" )
  print( "CODE: ", "\u0251" )
  print( "CODE: ", "\u0252" )
  print( "CODE: ", "\u0253" )
  print( "CODE: ", "\u0254" )
  print( "CODE: ", "\u0255" )
  print( "CODE: ", "\u0256" )
  print( "CODE: ", "\u0257" )
  print( "CODE: ", "\u0258" )
  print( "CODE: ", "\u0259" )
  print( "CODE: ", "\u0260" )
  print( "CODE: ", "\u0261" )
  print( "CODE: ", "\u0262" )
  print( "CODE: ", "\u0263" )
  print( "CODE: ", "\u0264" )
  print( "CODE: ", "\u0265" )
  print( "CODE: ", "\u0266" )
  print( "CODE: ", "\u0267" )
  print( "CODE: ", "\u0268" )
  print( "CODE: ", "\u0269" )
  print( "CODE: ", "\u0270" )
  print( "CODE: ", "\u0271" )
  print( "CODE: ", "\u0272" )
  print( "CODE: ", "\u0273" )
  print( "CODE: ", "\u0274" )
  print( "CODE: ", "\u0275" )
  print( "CODE: ", "\u0276" )
  print( "CODE: ", "\u0277" )
  print( "CODE: ", "\u0278" )
  print( "CODE: ", "\u0279" )
  print( "CODE: ", "\u0280" )
  print( "CODE: ", "\u0281" )
  print( "CODE: ", "\u0282" )
  print( "CODE: ", "\u0283" )
  print( "CODE: ", "\u0284" )
  print( "CODE: ", "\u0285" )
  print( "CODE: ", "\u0286" )
  print( "CODE: ", "\u0287" )
  print( "CODE: ", "\u0288" )
  print( "CODE: ", "\u0289" )
  print( "CODE: ", "\u0290" )
  print( "CODE: ", "\u0291" )
  print( "CODE: ", "\u0292" )
  print( "CODE: ", "\u0293" )
  print( "CODE: ", "\u0294" )
  print( "CODE: ", "\u0295" )
  print( "CODE: ", "\u0296" )
  print( "CODE: ", "\u0297" )
  print( "CODE: ", "\u0298" )
  print( "CODE: ", "\u0299" )
  print( "CODE: ", "\u0300" )
  print( "CODE: ", "\u0301" )
  print( "CODE: ", "\u0302" )
  print( "CODE: ", "\u0303" )
  print( "CODE: ", "\u0304" )
  print( "CODE: ", "\u0305" )
  print( "CODE: ", "\u0306" )
  print( "CODE: ", "\u0307" )
  print( "CODE: ", "\u0308" )
  print( "CODE: ", "\u0309" )
  print( "CODE: ", "\u0310" )
  print( "CODE: ", "\u0311" )
  print( "CODE: ", "\u0312" )
  print( "CODE: ", "\u0313" )
  print( "CODE: ", "\u0314" )
  print( "CODE: ", "\u0315" )
  print( "CODE: ", "\u0316" )
  print( "CODE: ", "\u0317" )
  print( "CODE: ", "\u0318" )
  print( "CODE: ", "\u0319" )
  print( "CODE: ", "\u0320" )
  print( "CODE: ", "\u0321" )
  print( "CODE: ", "\u0322" )
  print( "CODE: ", "\u0323" )
  print( "CODE: ", "\u0324" )
  print( "CODE: ", "\u0325" )
  print( "CODE: ", "\u0326" )
  print( "CODE: ", "\u0327" )
  print( "CODE: ", "\u0328" )
  print( "CODE: ", "\u0329" )
  print( "CODE: ", "\u0330" )
  print( "CODE: ", "\u0331" )
  print( "CODE: ", "\u0332" )
  print( "CODE: ", "\u0333" )
  print( "CODE: ", "\u0334" )
  print( "CODE: ", "\u0335" )
  print( "CODE: ", "\u0336" )
  print( "CODE: ", "\u0337" )
  print( "CODE: ", "\u0338" )
  print( "CODE: ", "\u0339" )
  print( "CODE: ", "\u0340" )
  print( "CODE: ", "\u0341" )
  print( "CODE: ", "\u0342" )
  print( "CODE: ", "\u0343" )
  print( "CODE: ", "\u0344" )
  print( "CODE: ", "\u0345" )
  print( "CODE: ", "\u0346" )
  print( "CODE: ", "\u0347" )
  print( "CODE: ", "\u0348" )
  print( "CODE: ", "\u0349" )
  print( "CODE: ", "\u0350" )
  print( "CODE: ", "\u0351" )
  print( "CODE: ", "\u0352" )
  print( "CODE: ", "\u0353" )
  print( "CODE: ", "\u0354" )
  print( "CODE: ", "\u0355" )
  print( "CODE: ", "\u0356" )
  print( "CODE: ", "\u0357" )
  print( "CODE: ", "\u0358" )
  print( "CODE: ", "\u0359" )
  print( "CODE: ", "\u0360" )
  print( "CODE: ", "\u0361" )
  print( "CODE: ", "\u0362" )
  print( "CODE: ", "\u0363" )
  print( "CODE: ", "\u0364" )
  print( "CODE: ", "\u0365" )
  print( "CODE: ", "\u0366" )
  print( "CODE: ", "\u0367" )
  print( "CODE: ", "\u0368" )
  print( "CODE: ", "\u0369" )
  print( "CODE: ", "\u0370" )
  print( "CODE: ", "\u0371" )
  print( "CODE: ", "\u0372" )
  print( "CODE: ", "\u0373" )
  print( "CODE: ", "\u0374" )
  print( "CODE: ", "\u0375" )
  print( "CODE: ", "\u0376" )
  print( "CODE: ", "\u0377" )
  print( "CODE: ", "\u0378" )
  print( "CODE: ", "\u0379" )
  print( "CODE: ", "\u0380" )
  print( "CODE: ", "\u0381" )
  print( "CODE: ", "\u0382" )
  print( "CODE: ", "\u0383" )
  print( "CODE: ", "\u0384" )
  print( "CODE: ", "\u0385" )
  print( "CODE: ", "\u0386" )
  print( "CODE: ", "\u0387" )
  print( "CODE: ", "\u0388" )
  print( "CODE: ", "\u0389" )
  print( "CODE: ", "\u0390" )
  print( "CODE: ", "\u0391" )
  print( "CODE: ", "\u0392" )
  print( "CODE: ", "\u0393" )
  print( "CODE: ", "\u0394" )
  print( "CODE: ", "\u0395" )
  print( "CODE: ", "\u0396" )
  print( "CODE: ", "\u0397" )
  print( "CODE: ", "\u0398" )
  print( "CODE: ", "\u0399" )
  print( "CODE: ", "\u0400" )
  print( "CODE: ", "\u0401" )
  print( "CODE: ", "\u0402" )
  print( "CODE: ", "\u0403" )
  print( "CODE: ", "\u0404" )
  print( "CODE: ", "\u0405" )
  print( "CODE: ", "\u0406" )
  print( "CODE: ", "\u0407" )
  print( "CODE: ", "\u0408" )
  print( "CODE: ", "\u0409" )
  print( "CODE: ", "\u0410" )
  print( "CODE: ", "\u0411" )
  print( "CODE: ", "\u0412" )
  print( "CODE: ", "\u0413" )
  print( "CODE: ", "\u0414" )
  print( "CODE: ", "\u0415" )
  print( "CODE: ", "\u0416" )
  print( "CODE: ", "\u0417" )
  print( "CODE: ", "\u0418" )
  print( "CODE: ", "\u0419" )
  print( "CODE: ", "\u0420" )
  print( "CODE: ", "\u0421" )
  print( "CODE: ", "\u0422" )
  print( "CODE: ", "\u0423" )
  print( "CODE: ", "\u0424" )
  print( "CODE: ", "\u0425" )
  print( "CODE: ", "\u0426" )
  print( "CODE: ", "\u0427" )
  print( "CODE: ", "\u0428" )
  print( "CODE: ", "\u0429" )
  print( "CODE: ", "\u0430" )
  print( "CODE: ", "\u0431" )
  print( "CODE: ", "\u0432" )
  print( "CODE: ", "\u0433" )
  print( "CODE: ", "\u0434" )
  print( "CODE: ", "\u0435" )
  print( "CODE: ", "\u0436" )
  print( "CODE: ", "\u0437" )
  print( "CODE: ", "\u0438" )
  print( "CODE: ", "\u0439" )
  print( "CODE: ", "\u0440" )
  print( "CODE: ", "\u0441" )
  print( "CODE: ", "\u0442" )
  print( "CODE: ", "\u0443" )
  print( "CODE: ", "\u0444" )
  print( "CODE: ", "\u0445" )
  print( "CODE: ", "\u0446" )
  print( "CODE: ", "\u0447" )
  print( "CODE: ", "\u0448" )
  print( "CODE: ", "\u0449" )
  print( "CODE: ", "\u0450" )
  print( "CODE: ", "\u0451" )
  print( "CODE: ", "\u0452" )
  print( "CODE: ", "\u0453" )
  print( "CODE: ", "\u0454" )
  print( "CODE: ", "\u0455" )
  print( "CODE: ", "\u0319" )
  print( "CODE: ", "\u0319" )
  print( "CODE: ", "\u0319" )
  print( "CODE: ", "\u0319" )
  quit( )

  # randomize
  seed( )

  mainPassword    = ( "" )
  tempPassword    = ( "" )
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
    un    = ( "" )
    email = ( "" )
    url   = ( "" )
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

    jsonOutput = []
    if( os.path.isfile( outputFile ) ):
      try:
       with open( outputFile, 'r' ) as readFile:
          jsonOutput_old = json.load( readFile )
          for i in jsonOutput_old:
            jsonOutput.append( i )
      except:
        print(  traceback.format_exc( ) )

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
