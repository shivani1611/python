#!/usr/bin/env python3

from sys       import exit
from logthis.pylogthis import WriteThis

def main( ):
  wt = WriteThis( "", "error.txt", "log.txt" )

  wt.is_conf_enabled = ( True )
  wt.is_err_enabled  = ( False )
  wt.is_log_enabled  = ( True )

  wt.string_output( "log", "this is a log message" )
  wt.string_output( "err", "this is an error message", main.__name__ )
  wt.string_output( "conf", "this is a configuration message" )

if( __name__ == ( "__main__" ) ):
    exit( main( ) )
