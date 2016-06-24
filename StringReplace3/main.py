#!/usr/bin/env python3

import sys

def main( ):
  my_string = ( "i went to school today" )
  my_string = my_string.replace( "i", "we" )
  my_string = my_string.replace( "school", "work" )
  my_string = my_string.replace( "today", "yesterday" )

  print( my_string )


if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
