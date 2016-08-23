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
  print( "_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=" )
  print( "- ADT Pulse Control Interface -" )
  print( "=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_" )
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
  # --armaway
  # --armstay
  # --disarm
  # --isarmed
  # --help

  print( )
  print( "--armaway, aa = Arm the home while you are away" )
  print( "--armstay, as = Arm the home while you are inside" )
  print( "--disarm, da  = Disarm the home" )
  print( "--isarmed, ia = Is the home currently armed?" )
  print( "--help, hlp   = Help menu" )
  print( )
  print( "Usage: python3 pulse.py {--isarmed | --armaway | --armstay | --disarm | --help}" )
  print( )
  print( "Example: python3 pulse.py --armaway" )
  print( "Example: python3 pulse.py --armstay" )
  print( "Example: python3 pulse.py --disarm" )
  print( "Example: python3 pulse.py --isarmed" )
  print( "Example: python3 pulse.py --help" )
  print( )

  return

def isArmed( drv ):
  time.sleep( 1 )
  isArm = ( True )

  element = drv.find_element_by_id( "security_button_1" )
  element_value = element.get_attribute( 'value' )
  if( str( element_value ).lower( ) == ( "arm away" ) ):
    isArm = ( False )

  return( isArm )

def disarm( drv ):
  element = drv.find_element_by_id( "security_button_1" )
  element.click( )

  time.sleep( 1 )

  print( "  ==> System is now in DISARMED mode!" )

  return

def armAway( drv ):
  element = drv.find_element_by_id( "security_button_1" )
  element.click( )  

  time.sleep( 1 )

  try:
    WebDriverWait( drv, 3 ).until( expected_conditions.alert_is_present( ),
                                   'Timed out waiting for PA creation ' + 
                                   'confirmation popup to appear.' )

    alert = drv.switch_to_alert( )
    alert.accept( )
    print( "  ==> Sensors were: [ BYPASSED ]" )
  except TimeoutException:
    print( "  ==> All sensors are: [ GREEN ]" )

  print( "  ==> System is now in mode: [ ARMED AWAY ]" )

  return

def armStay( drv ):
  element = drv.find_element_by_id( "security_button_2" )
  element.click( )  

  time.sleep( 15 )

  try:
    WebDriverWait( drv, 3 ).until( expected_conditions.alert_is_present( ),
                                   'Timed out waiting for PA creation ' + 
                                   'confirmation popup to appear.' )

    alert = drv.switch_to_alert( )
    alert.accept( )
    print( "  ==> Sensors were: [ BYPASSED ]" )
  except TimeoutException:
    print( "  ==> All sensors are: [ GREEN ]" )

  print( "  ==> System is now in mode: [ ARMED STAY ]" )

  return

def login( drv ):
  URL           = ( "https://portal.adtpulse.com" )
  USER_ELM      = ( "username" )
  PASS_ELM      = ( "password" )
  SIGNIN_ELM    = ( "signin" )

  time.sleep( 5 )

  drv.get( URL )

  time.sleep( 30 )

  drv.find_element_by_id( USER_ELM ).clear( )
  drv.find_element_by_id( USER_ELM ).send_keys( decode(  ) )

  drv.find_element_by_id( PASS_ELM ).clear( )
  drv.find_element_by_id( PASS_ELM ).send_keys( decode( ) )

  drv.find_element_by_name( SIGNIN_ELM ).click( )

  time.sleep( 1 )

  return

def logout( drv ):
  SIGNOUT_ELM = ( "p_signout2" )

  time.sleep( 1 )

  drv.find_element_by_id( SIGNOUT_ELM ).click( )

  time.sleep( 1 )

  return

def connect( ): 
  drv = ( webdriver.Firefox( ) )

  time.sleep( 15 )

  return( drv )

def main( ):
  isArmStay_sw          = ( False )
  isArmAway_sw          = ( False )
  isDisarm_sw           = ( False )
  isCurrentlyArmed_sw   = ( False )
  isHelp_sw             = ( False )

  NO_ARG                = ( 1 )
  MAX_ARG               = ( 2 )

  resetScreen( )

  # if no arguments are provided
  if( ( len( sys.argv ) == ( NO_ARG ) ) or ( len( sys.argv ) > ( MAX_ARG ) ) ):
    help( )
  else:
    arg = str( sys.argv[1] ).lower( )

    if( ( ( "armaway" ) in arg ) or ( arg == ( "aa" ) ) ):
      isArmAway_sw = ( True )
    elif( ( ( "armstay" ) in arg ) or ( arg == ( "as" ) ) ):
      isArmStay_sw = ( True )
    elif( ( ( "disarm" ) in arg ) or ( arg == ( "da" ) ) ):
      isDisarm_sw = ( True )
    elif( ( ( "isarm" ) in arg ) or ( arg == ( "ia" ) ) ):
      isCurrentlyArmed_sw = ( True )
    elif( ( ( "help" ) in arg ) or ( arg == ( "hlp" ) ) ):
      isHelp_sw = ( True )
    else:
      isHelp_sw = ( True )
 
    if( isHelp_sw ):
      help( )
    else:
      if( ( isArmAway_sw ) or ( isArmStay_sw ) or ( isDisarm_sw ) or ( isCurrentlyArmed_sw ) ):
        drv = ( connect( ) )
        login( drv )

      time.sleep( 45 )

      if( isCurrentlyArmed_sw ):
        print( "  ==> The system is currently armed: [ {0} ]".format( str( isArmed( drv ) ).upper( ) ) )
        time.sleep( 1 )
      else:
        if( not isArmed( drv ) ):
          if( isArmAway_sw ):
            armAway( drv )
          elif( isArmStay_sw ):
            armStay( drv )
    
        if( isArmed( drv ) ):
          if( isDisarm_sw ):
            disarm( drv )
    
        time.sleep( 45 )

      if( ( isArmAway_sw ) or ( isArmStay_sw ) or ( isDisarm_sw ) or ( isCurrentlyArmed_sw ) ):
        logout( drv )
        drv.close( )
        time.sleep( 1 )
        drv.quit( )
  
  print( "\r\nGoodbye!" )
  print( )

  return

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
