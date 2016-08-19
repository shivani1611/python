#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import base64
import os
import platform
import sys
import time

def clearScreen( ):
  if( ( "window" ) in str( platform.system( ) ).lower( ) ):
    os.system( "cls" )
  else:
    os.system( "clear" )

  return

def title( ):
  print( )
  print( "_-=-_=-_-=-_-=-_-=-_-=-_-=" )
  print( "- Nest Control Interface -" )
  print( "=-_-=_-=-_-=-_-=-_-=-_-=-_" )
  print( )

  return

def resetScreen( ):
  clearScreen( )
  title( )

  return

def encode( msg ):
  return( base64.b64encode( bytes( msg, "utf-8" ) ) )

def decode( msg ):
  return( "".join( map( chr, base64.b64decode( bytes( msg, "utf-8" ) ) ) ) )

def help( ):
  # --cool
  # --heat
  # --coolheat
  # --off
  # --help

  print( )
  print( "--cool, co      = Cool the home" )
  print( "--heat, he      = Heat the home" )
  print( "--coolheat, ch  = Cool/Heat the home" )
  print( "--off, of       = Turn unit off" )
  print( "--help, hlp     = Help menu" )
  print( )
  print( "Usage: python3 nest.py {--cool | --heat | --coolheat | --off | --help}" )
  print( )
  print( "Example: python3 nest.py --cool" )
  print( "Example: python3 nest.py --heat" )
  print( "Example: python3 nest.py --coolheat" )
  print( "Example: python3 nest.py --off" )
  print( "Example: python3 nest.py --help" )
  print( )

  return

def cool( drv ):
  element = drv.find_element_by_id( "security_button_1" )
  element.click( )  

  time.sleep( 1 )

  return

def heat( drv ):
  element = drv.find_element_by_id( "security_button_2" )
  element.click( )  

  time.sleep( 1 )

  return

def login( drv ):
  URL           = ( "https://home.nest.com" )
  USER_ELM      = ( "email" )
  PASS_ELM      = ( "pass" )
  SIGNIN_ELM    = ( "signin" )

  drv.get( URL )

  time.sleep( 5 )
  #drv.find_element_by_id( USER_ELM ).clear( )
  #drv.find_element_by_id( USER_ELM ).send_keys( "armond.sarkisian@gmail.com" )

  #drv.find_element_by_id( PASS_ELM ).clear( )
  #drv.find_element_by_id( PASS_ELM ).send_keys( "Mysql123890!" )

  drv.find_element_by_name( SIGNIN_ELM ).click( )

  time.sleep( 1 )

  return

def logout( drv ):
  SIGNOUT_ELM = ( "" )

  time.sleep( 1 )

  drv.find_element_by_id( SIGNOUT_ELM ).click( )

  time.sleep( 1 )

  return

def connect( ): 
  drv = ( webdriver.Firefox( ) )

  time.sleep( 1 )

  return( drv )

def main( ):
  isCool_sw      = ( False )
  isHeat_sw      = ( False )
  isCoolHeat_sw  = ( False )
  isOff_sw       = ( False )
  isHelp_sw      = ( False )

  NO_ARG                = ( 1 )
  MAX_ARG               = ( 2 )

  resetScreen( )

  # if no arguments are provided
  if( ( len( sys.argv ) == ( NO_ARG ) ) or ( len( sys.argv ) > ( MAX_ARG ) ) ):
    help( )
  else:
    arg = str( sys.argv[1] ).lower( )

    if( ( ( "cool" ) in arg ) or ( arg == ( "co" ) ) ):
      isCool_sw = ( True )
    elif( ( ( "heat" ) in arg ) or ( arg == ( "he" ) ) ):
      isHeat_sw = ( True )
    elif( ( ( "coolheat" ) in arg ) or ( arg == ( "ch" ) ) ):
      isCoolHeat_sw = ( True )
    elif( ( ( "off" ) in arg ) or ( arg == ( "of" ) ) ):
      isOff_sw = ( True )
    elif( ( ( "help" ) in arg ) or ( arg == ( "hlp" ) ) ):
      isHelp_sw = ( True )
    else:
      isHelp_sw = ( True )
 
    if( isHelp_sw ):
      help( )
    else:
      if( ( isCool_sw ) or ( isHeat_sw ) or ( isCoolHeat_sw ) or ( isOff_sw ) ):
        drv = ( connect( ) )
        login( drv )

      time.sleep( 15 )

      if( ( isCool_sw ) or ( isHeat_sw ) or ( isCoolHeat_sw ) or ( isOff_sw ) ):
        drv = ( connect( ) )
        logout( drv )
        drv.close( )
  
  print( "\r\nGoodbye!" )
  print( )

  return

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
