#!/usr/bin/env python3

from sys import exit
from pylogthis import WriteThis

def main( ):
  wt = WriteThis( "config.txt", "error.txt", "log.txt" )

if( __name__ == ( "__main__" ) ):
    exit( main( ) )
