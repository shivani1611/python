from datetime import date
from datetime import datetime
from calendar import monthrange
from calendar import isleap
from dateutil.relativedelta import relativedelta

import calendar
import time

class GetDateTime( object ):
    @staticmethod
    def is_leap_year( value ):
        return( isleap( int( value ) ) )

    @staticmethod
    def current_days_in_month( incre = ( 0 ) ):
        month_start_end = ( monthrange( GetDateTime.current_year_value( ), GetDateTime.current_month_value( ) + incre ) )
        return( int( month_start_end[1] ) - int( month_start_end[0] ) )

    @staticmethod
    def current_first_day_in_month( incre = ( 0 ) ):
        return( str( monthrange( GetDateTime.current_year_value( ), GetDateTime.current_month_value( ) + incre )[0] ) )

    @staticmethod
    def current_last_day_in_month( incre = ( 0 ) ):
         return( str( monthrange( GetDateTime.current_year_value( ), GetDateTime.current_month_value( ) + incre )[1] ) )

    @staticmethod
    def current_timestamp( with_milli_seconds = ( True ) ):
        if( with_milli_seconds == ( True ) ):
            val = ( str( datetime.now( ) ) )
        else:
            val = ( str( datetime.now( ) )[0:19:1] )
        return( val )

    @staticmethod
    def current_year_value( incre = ( 0 ) ):
        return( str( date.today( ).year + incre ) )

    @staticmethod
    def current_month_name( incre = ( 0 ) ):
        _month = ( datetime.today( ) + relativedelta( month = ( incre ) ) )
        return( _month._strftime( '%B' ) )

    @staticmethod
    def current_month_value( ):
        return

    @staticmethod
    def current_week_name( ):
        return

    @staticmethod
    def current_week_value( ):
        return

    @staticmethod
    def current_day_name( ):
        return

    @staticmethod
    def current_day_value( ):
        return

    @staticmethod
    def current_hour_value( ):
        return

    @staticmethod
    def current_minute_value( ):
        return

    @staticmethod
    def current_second_value( ):
        return

    @staticmethod
    def current_millisecond_value( ):
        return
