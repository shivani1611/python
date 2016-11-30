#!/usr/bin/env python3

from sys import exit

class SumListAdd(object):
    def __init__( self, this_list ):
        self.mylist = this_list

    def __add__( self, other ):
        new_list = [x + y for x, y in zip( self.mylist, other.mylist )]
        return SumListAdd( new_list )

    def __repr__(self):
        return( str( self.mylist ) )

def main( ):
    cc = SumListAdd( [1, 2, 3, 4, 5] )
    dd = SumListAdd( [100, 200, 300, 400, 500] )

    ee = cc + dd

    print( ee )

    return( 0 )

if( __name__ == ( "__main__" ) ):
    exit( main( ) )
