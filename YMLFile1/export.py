#!/usr/bin/env python2

import sys
import yaml

def main( ):

  my_list = []

  file_name = raw_input( "Enter filename without extension: " )

  for i in range( 0, 10, 1 ):
    word = raw_input( "Enter a word: " ) 
    my_list.append( word )

  with open( file_name + ".yml", 'w' ) as f:
    f.write( yaml.dump( my_list ) )

if( __name__ == ( "__main__"  ) ):
  sys.exit( main( ) )
