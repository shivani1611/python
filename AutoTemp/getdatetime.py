from datetime import date
from datetime import datetime
from calendar import isleap
from calendar import month
from calendar import monthrange
from dateutil.relativedelta import relativedelta

import calendar
import time

class GetDateTime( object ):
    _start_time   = ( 0.0 )
    _elapsed_time = ( 0.0 )
    _end_time     = ( 0.0 )

    @ClassProperty
    @classmethod
    def start_time( cls ):
        return( cls._start_time ) 

    @ClassProperty
    @classmethod
    def elapsed_time( cls ):
        return( cls._elapsed_time ) 

    @ClassProperty
    @classmethod
    def end_time( cls ):
        return( cls._end_time ) 

    @start_time.setter
    @classmethod
    def start_time( cls, value ):
        cls._start_time = ( value )

    @elapsed_time.setter
    @classmethod
    def elapsed_time( cls, value ):
        cls._elapsed_time = ( value )

    @end_time.setter
    @classmethod
    def end_time( cls, value ):
        cls._end_time = ( value )

    @classmethod
    def reset_timer( cls ):
        cls.start_time   = ( 0.0 )
        cls.elapsed_time = ( 0.0 )
        cls.end_time     = ( 0.0 )

    @staticmethod
    def is_leap_year( value ):
        return( isleap( int( value ) ) )

    @staticmethod
    def print_current_month_calendar( _year, _month ):
        print( month( _year, _month ) ) 

    @staticmethod
    def print_current_date_time( ):
        _time = ( datetime.today( ) )
        return( _time.strftime( '%c' ) )

    @staticmethod
    def current_first_last_day_in_month( ):
         return( str( monthrange( int( GetDateTime.current_year_value( ) ), int( GetDateTime.current_month_value( ) ) ) ) )

    @staticmethod
    def current_day_of_month( ):
        _month = ( datetime.today( ) )
        return( _month.strftime( '%d' ) )

    @staticmethod
    def current_timestamp( with_milli_seconds = ( True ) ):
        if( with_milli_seconds == ( True ) ):
            val = ( str( datetime.now( ) ) )
        else:
            val = ( str( datetime.now( ) )[0:19:1] )
        return( val )

    @staticmethod
    def current_year_value( incre = ( 0 ) ):
        return( str( int( date.today( ).year ) + int( incre ) ) )

    @staticmethod
    def current_year_abbrev_value( ):
        _year = ( datetime.today( ) )
        return( _year.strftime( '%y' ) )

    @staticmethod
    def current_month_name( incre = ( 0 ) ):
        _month = ( datetime.today( ) + relativedelta( month = ( incre ) ) )
        return( _month.strftime( '%B' ) )

    @staticmethod
    def current_month_abbrev_name( incre = ( 0 ) ):
        _month = ( datetime.today( ) + relativedelta( month = ( incre ) ) )
        return( _month.strftime( '%b' ) )

    @staticmethod
    def current_month_value( incre = ( 0 ) ):
        _month = ( datetime.today( ) + relativedelta( month = ( incre ) ) )
        return( _month.strftime( '%m' ) )

    @staticmethod
    def current_day_name( incre = ( 0 ) ):
        if( incre < 0 ):
            retur( '?' )
        _day = ( datetime.today( ) + relativedelta( day = ( incre ) ) )
        return( _day.strftime( '%A' ) )

    @staticmethod
    def current_day_abbrev_name( incre = ( 0 ) ):
        _day = ( datetime.today( ) + relativedelta( day = incre ) )
        return( _day.strftime( '%a' ) )

    @staticmethod
    def current_day_value( ):
        _day = ( datetime.today( ) )
        return( _day.strftime( '%w' ) )

    @staticmethod
    def current_24_hour_value( ):
        _day = ( datetime.today( ) )
        return( _day.strftime( '%H' ) )

    @staticmethod
    def current_12_hour_value( ):
        _day = ( datetime.today( ) )
        return( _day.strftime( '%I' ) )

    @staticmethod
    def current_minute_value( ):
        _minute = ( datetime.today( ) )
        return( _minute.strftime( '%M' ) )

    @staticmethod
    def current_second_value( ):
        _second = ( datetime.today( ) )
        return( _second.strftime( '%S' ) )

    @staticmethod
    def current_micro_second_value( ):
        _micro_second = ( datetime.today( ) )
        return( _micro_second.strftime( '%f' ) )
