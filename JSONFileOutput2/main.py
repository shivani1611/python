#!/usr/bin/env python3

import json
import sys
from pprint import pprint as pp

def main( ):
  with open( "armond.txt", 'r' ) as fin:
    my_list = json.load( fin )

  pp( my_list )

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
