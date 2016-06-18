#!/usr/bin/env python3

from sys import exit
from pprint import pprint
import json

def main( ):

  with open( "armond.txt", 'r' ) as fin:
    data = json.load( fin )

  newDict = { "syuzi" : "34", "seda" : "28", "suida" : "30" }

  # add the new dictionary to the old one
  newData = data.copy( )
  newData.update( newDict )

  # print the new dictionary
  pprint( newData )

if( __name__ == ( "__main__" ) ):
  exit( main( ) )
