#!/usr/bin/env python3

def calcMillisecond( second ):
  return( second * 1000 )

def calcSec( minute ):
  return( minute * 60 )

def calcMin( hour ):
  return( hour * 60 )

def calcHour( day ):
  return( day * 24 )

def calcDay( year ):
  return( year * 365 )

def main( ):

  while( True ):
    year = ( int( input( "Enter year: " ) ) )
    if( year ):
      break

  day = ( calcDay( year ) )
  hour = ( calcHour( day ) )
  minute = ( calcMin( hour ) )
  second = ( calcSec( minute ) )
  millisecond = ( calcMillisecond( second ) )

  print( "Days: ", day )
  print( "Hours: ", hour )
  print( "Minutes: ", minute )
  print( "Seconds: ", second )
  print( "Milliseconds: ", millisecond )

if( __name__ == ( "__main__" ) ):
  main( )
