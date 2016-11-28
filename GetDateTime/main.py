#!/usr/bin/env python3

from getdatetime import GetDateTime

def main( ):
  print( "Is 2016 a leap year: " + ( str( GetDateTime.is_leap_year(2016 ) ) ) )
  print( GetDateTime.current_first_last_day_in_month( ) )
  print( GetDateTime.current_year_value( ) )
  print( GetDateTime.current_year_value( 2 ) )
  print( GetDateTime.current_year_abbrev_value( ) )
  print( GetDateTime.current_month_value( ) )
  print( GetDateTime.current_month_value( 2 ) )
  print( GetDateTime.current_month_name( ) )
  print( GetDateTime.current_month_name( 2 ) )
  print( GetDateTime.current_month_abbrev_name( ) )
  print( GetDateTime.current_month_abbrev_name( 2 ) )
  print( GetDateTime.current_day_name(  ) )
  print( GetDateTime.current_day_name( 2 ) )
  print( GetDateTime.current_day_abbrev_name( ) )
  print( GetDateTime.current_day_abbrev_name( 2 ) )
  print( GetDateTime.current_24_hour_value(  ) )
  print( GetDateTime.current_24_hour_value( ) )
  print( GetDateTime.current_12_hour_value(  ) )
  print( GetDateTime.current_12_hour_value( ) ) 
  print( GetDateTime.current_day_value( ) )
  print( GetDateTime.current_minute_value( ) )
  print( GetDateTime.current_second_value( ) )
  print( GetDateTime.current_micro_second_value( ) )
  print( GetDateTime.print_current_date_time( ) )

  

if( __name__ == ( "__main__" ) ):
  main( )
