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
  print( "_-=-_-=-_-=-_=-_-=-_-=-_-=" )
  print( "- Parrot Speak Interface -" )
  print( "=-_-=-_-=-_-=_-=-_-=-_-=-_" )
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
  # --hello
  # --thank you
  # --whattayoudoing
  # --goodmorning
  # --goodnight
  # --iloveyou
  # --imhungry
  # --yoursopretty
  # --uhoh
  # --byebye
  # --whistle-sw
  # --relaxing
  # --help

  print( )
  print( "--hello, he            = Teach the parrot to say \"Hello\"" )
  print( "--thankyou, ty         = Teach the parrot to say \"Thank you\"" )
  print( "--whattayoudoing, wyd  = Teach the parrot to say \"Whatta you doing\"" )
  print( "--goodmorning, gm      = Teach the parrot to say \"Good morning\"" )
  print( "--goodnight, gn        = Teach the parrot to say \"Good night\"" )
  print( "--iloveyou, ilu        = Teach the parrot to say \"I love you\"" )
  print( "--imhungry, ih         = Teach the parrot to say \"I'm hungry\"" )
  print( "--yoursopretty, ysp    = Teach the parrot to say \"You're so pretty!\"" )
  print( "--uhoh, uo             = Teach the parrot to say \"Uh-oh\"" )
  print( "--byebye, bb           = Teach the parrot to say \"Bye bye\"" )
  print( "--whistle-sw, whsw     = Teach the parrot to whistle \"Star Wars\" theme" )
  print( "--relaxing, rx         = Relaxing forest/jungle music for your parot" )
  print( "--help, hlp            = Display the help menu" )
  print( )
  print( "Usage: python3 speak.py {--hello | --thankyou | --whattayoudoing | --goodmorning | --goodnight | --iloveyou | --imhungry | --yoursopretty | --uhoh | --byebye | --whistle-sw | --help}" )
  print( )
  print( "Example: python3 speak.py --hello" )
  print( "Example: python3 speak.py --goodnight" )
  print( "Example: python3 speak.py bb" )
  print( "Example: python3 speak.py --iloveyou" )
  print( "Example: python3 speak.py ih" )
  print( )

  return

def connect( ): 
  drv = ( webdriver.Firefox( ) )

  time.sleep( 15 )

  return( drv )

def playVideo( drv, what ):
  what = ( what.strip( ).lower( ) )

  if( what == ( "hello" ) ):
    drv.get( "https://www.youtube.com/watch?v=I4xMzf4YSRs"  )
  elif( what == ( "thankyou" ) ):
    drv.get( "https://www.youtube.com/watch?v=x-0M_COlEws" )
  elif( what == ( "whattayoudoing" ) ):
    drv.get( "https://www.youtube.com/watch?v=3-LvSWUqVbM" )
  elif( what == ( "goodmorning" ) ):
    drv.get( "https://www.youtube.com/watch?v=-pVljJwhArc" )
  elif( what == ( "goodnight" ) ):
    drv.get( "https://www.youtube.com/watch?v=DlOKi6oIyRM" )
  elif( what == ( "iloveyou" ) ):
    drv.get( "https://www.youtube.com/watch?v=9qC6PDPCZUE" )
  elif( what == ( "imhungry" ) ):
    drv.get( "https://www.youtube.com/watch?v=A67u3rLRx7c" )
  elif( what == ( "yoursopretty" ) ):
    drv.get( "https://www.youtube.com/watch?v=j9fsXTQy7YE" )
  elif( what == ( "uhoh" ) ):
    drv.get( "https://www.youtube.com/watch?v=LltoWo0GVVE" )
  elif( what == ( "byebye" ) ):
    drv.get( "https://www.youtube.com/watch?v=8k6qAorZbig" )
  elif( what == ( "whistle-sw" ) ):
    drv.get( "https://www.youtube.com/watch?v=Bsd7KxVcW-U" )
  elif( what == ( "relaxing" ) ):
    drv.get( "https://www.youtube.com/watch?v=VeIhRdR2jsU" )
  return

def main( ):
  isHello_sw          = ( False )
  isThankYou_sw       = ( False )
  isWhattaYouDoing_sw = ( False )
  isGoodMorning_sw    = ( False )
  isGoodNight_sw      = ( False )
  isILoveYou_sw       = ( False )
  isImHungry_sw       = ( False )
  isYourSoPretty_sw   = ( False )
  isUhOh_sw           = ( False )
  isByeBye_sw         = ( False )
  isWhistleSW_sw      = ( False )
  isRelaxing_sw       = ( False )
  isHelp_sw           = ( False )

  NO_ARG                = ( 1 )
  MAX_ARG               = ( 2 )

  resetScreen( )

  # if no arguments are provided
  if( ( len( sys.argv ) == ( NO_ARG ) ) or ( len( sys.argv ) > ( MAX_ARG ) ) ):
    help( )
  else:
    arg = str( sys.argv[1] ).lower( )

    if( ( ( "hello" ) in arg ) or ( arg == ( "he" ) ) ):
      isHello_sw = ( True )
    elif( ( ( "thankyou" ) in arg ) or ( arg == ( "ty" ) ) ):
      isThankYou_sw = ( True )
    elif( ( ( "whattayoudoing" ) in arg ) or ( arg == ( "wyd" ) ) ):
      isWhattaYouDoing = ( True )
    elif( ( ( "goodmorning" ) in arg ) or ( arg == ( "gm" ) ) ):
      isGoodMorning_sw = ( True )
    elif( ( ( "goodnight" ) in arg ) or ( arg == ( "gn" ) ) ):
      isGoodNight_sw = ( True )
    elif( ( ( "iloveyou" ) in arg ) or ( arg == ( "ilu" ) ) ):
      isILoveYou_sw = ( True )
    elif( ( ( "imhungry" ) in arg ) or ( arg == ( "ih" ) ) ):
      isImHungry_sw = ( True )
    elif( ( ( "yoursopretty" ) in arg ) or ( arg == ( "ysp" ) ) ):
      isYourSoPretty_sw = ( True )
    elif( ( ( "uhoh" ) in arg ) or ( arg == ( "uo" ) ) ):
      isUhOh_sw = ( True )
    elif( ( ( "byebye" ) in arg ) or ( arg == ( "bb" ) ) ):
      isByeBye_sw = ( True )
    elif( ( ( "whistle-sw" ) in arg ) or ( arg == ( "whsw" ) ) ):
      isWhistleSW_sw = ( True )
    elif( ( ( "relaxing" ) in arg ) or ( arg == ( "rx" ) ) ):
      isRelaxing_sw = ( True )
    else:
      isHelp_sw = ( True )
 
    if( isHelp_sw ):
      help( )
    else:
      drv = ( connect( ) )

      time.sleep( 30 )

      if( isHello_sw ):
        playVideo( drv, "hello" )
      elif( isThankYou_sw ):
        playVideo( drv, "thankyou" )
      elif( isWhattaYouDoing_sw ):
        playVideo( drv, "whattayoudoing" )
      elif( isGoodMorning_sw ):
        playVideo( drv, "goodmorning" )
      elif( isGoodNight_sw ):
        playVideo( drv, "goodnight" )
      elif( isILoveYou_sw ):
        playVideo( drv, "iloveyou" )
      elif( isImHungry_sw ):
        playVideo( drv, "imhungry" )
      elif( isYourSoPretty_sw ):
        playVideo( drv, "yoursopretty" )
      elif( isUhOh_sw ):
        playVideo( drv, "uhoh" )
      elif( isByeBye_sw ):
        playVideo( drv, "byebye" )
      elif( isWhistleSW_sw ):
        playVideo( drv, "whistle-sw" )
      elif( isRelaxing_sw ):
        playVideo( drv, "relaxing" )

      time.sleep( 3600 )

      drv.close( )
      drv.quit( )
  
  print( "\r\nGoodbye!" )
  print( )

  return

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
