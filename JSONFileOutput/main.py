#!/usr/bin/env python3

from sys import exit
from pprint import pprint
import json

def main( ):
  fullName = ( input( "Enter full name: " ) )
  fullName2 = ( input( "Enter full name: " ) )

  age = ( input( "Enter age: " ) )
  age2 = ( input( "Enter age: " ) )

  dict = { fullName : age, fullName2 : age2 }

  jsonData = ( json.dumps( dict ) )

  pprint( jsonData )  

  with open( 'armond', 'w' ) as fout:
    json.dump( jsonData, fout )

if( __name__ == ( "__main__" ) ):
  exit( main( ) )
