#!/usr/bin/env python3

import json
from pprint import pprint

def main( ):
  data = {}
  data['key'] = 'value'
  data['key2'] = 'value2'
  data['key3'] = 'value3'
  json_data = json.dumps( data )

  pprint( json_data )

if( __name__ == ( "__main__" ) ):
  main( )
