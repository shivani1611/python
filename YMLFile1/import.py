#!/usr/bin/env python2

import sys
import yaml

def main( ):

  file_name = raw_input( "Enter filename without extension: " )

  with open( file_name + ".yml" ) as f:
    my_list = yaml.load( f )

  for i in range( 0, len( my_list ), 1 ):
    print( my_list[i] )

if( __name__ == ( "__main__"  ) ):
  sys.exit( main( ) )
