#!/usr/bin/env python3

from sys import exit
from pylogthis import WriteThis

def main( ):
  wt = WriteThis( "config.txt", "error.txt", "log.txt" )
  wt.string_output( "log", "hello, world!" )

if( __name__ == ( "__main__" ) ):
    exit( main( ) )
