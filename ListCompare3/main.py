#!/usr/bin/env python3

import sys

def main( ):

  # list # 1
  list1 = [ "network", "router", "switch", "datalink", "igmp", "icmp", "rip", "stp", "utp", "hub", "cisco", "juniper", "arista", "osi" ]

  # list # 2
  list2 = [ "osi", "cisco", "switch", "igmp" ]

  #compare both lists
  for a in range( len( list1 ) - ( 1 ), -1, -1 ):
    for b in range( len( list2 ) - ( 1 ), -1, -1 ):
      if( list2[b] == list1[a] ):
        del( list1[a] )

  for a in range( 0, len( list1 ), 1 ):
    print( list1[a] )

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
