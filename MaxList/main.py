#!/usr/bin/env python3

class MaxList( object ):
    lst = []

    def __init__( self, maxNum ):
        self.maxNum = ( maxNum )

    def push( self, obj ):
        MaxList.lst.insert( 0, obj )
        if( len( MaxList.lst ) > self.maxNum ):
            MaxList.lst.pop( )

    def get_lst( self ):
      print( self.lst )

my_list = MaxList( 3 )

my_list.push( "1" )
my_list.push( "2" )
my_list.push( "3" )
my_list.push( "4" )

my_list.get_lst( )
