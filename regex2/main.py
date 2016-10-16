#!/usr/bin/env python3

from sys import exit
import re

def main( ):
  with open( "test.txt", 'r' ) as fin:
    fileStr = ( fin.readlines( ) )

  fileStr = ( str( fileStr ) )

  emailPattern = ( r"([a-zA-Z_.]{1,25})@([a-zA-Z]{1,25}).([a-zA-Z]{1,5})" )
  result = ( re.search( emailPattern, fileStr ) )

  print( "match!" ) if( result ) else print( "no match!" )

  return( 0 )

if( __name__ ==  ( "__main__" ) ):
  exit( main( ) )
