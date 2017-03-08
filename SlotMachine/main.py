#!/usr/bin/env python3

from sys import exit
from random import randint

class Slots(object):

    # all columns
    column_1 = []
    column_2 = []
    column_3 = []

    @classmethod
    def initialize_columns( cls ):

        cls.column_1.append( "Cherry" )
        cls.column_1.append( "Bananna" )
        cls.column_1.append( "Apple" )
        cls.column_1.append( "Kiwi" )
        cls.column_1.append( "Pear" )
        cls.column_1.append( "Orange" )
        cls.column_1.append( "Watermellon" )

        cls.column_2.append( "Bananna" )
        cls.column_2.append( "Kiwi" )
        cls.column_2.append( "Orange" )
        cls.column_2.append( "Apple" )
        cls.column_2.append( "Watermellon" )
        cls.column_2.append( "Pear" )
        cls.column_2.append( "Cherry" )

        cls.column_3.append( "Pear" )
        cls.column_3.append( "Orange" )
        cls.column_3.append( "Kiwi" )
        cls.column_3.append( "Watermellon" )
        cls.column_3.append( "Cherry" )
        cls.column_3.append( "Apple" )
        cls.column_3.append( "Bananna" )

    @classmethod
    def play( cls ):

        while( True ):

            for i in cls.column_1:

                print( i )



def main( ):

    Slots.initialize_columns( )
    Slots.play( )


if __name__ == ( "__main__" ):
    exit( main( ) )
