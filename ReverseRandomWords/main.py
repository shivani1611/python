#!/usr/bin/env python3

import random
import sys

reverse_sw = ( False )
random_sw  = ( False )

def isEmptyArgs( ):

    isEmpty = ( False )

    # check if any of these switches are turned on
    if( reverse_sw == ( False ) and ( random_sw == ( False ) ) ):
        isEmpty  = ( True )

    return( isEmpty )

def checkArgs( ):
    global reverse_sw
    global random_sw

    for i in range( 0, len( sys.argv ), 1 ):

        # skip the first element which is the path/name of the script
        if( i == ( 0 ) ):
            continue

        # prepare the argument
        switch = ( str( sys.argv[i] ).strip( ).lower( ) )

        # check for the argument
        if( 'rev' in ( switch ) ):
            reverse_sw = ( True )
        elif( 'rand' in ( switch ) ):
            random_sw = ( True )

def main( ):
    reversedWords = ""
    randomWords   = ""
    temp          = []
    list          = []
    used_ele      = []
    list_length   = 0

    # validate switches
    checkArgs( )

    if( not isEmptyArgs( ) ):
        words = ( input( "Enter words: " ) )

        if( reverse_sw == ( True ) ):
            # reverse all the words
            for i in range( len( words ) - 1, -1, -1 ):
                reversedWords += ( words[i] )
            print( "Reversed Words: ", reversedWords )

        if( random_sw == ( True ) ):
            list = ( words.split( ' ' ) )
            list_length = ( len( list ) )

            # randomize order of the words
            for i in range( ( list_length - 1 ), -1, -1 ):
                randNum = ( random.randrange( list_length - 1, -1, -1 ) )
                while( randNum in ( used_ele ) ):
                    randNum = ( random.randrange( list_length - 1,  -1 , -1 ) )
                used_ele.append(randNum)
                temp.append( list[randNum] )

            # reconstruct the string
            for a in range( 0, len( temp ), 1 ):
                randomWords += ( temp[a] )
                randomWords += ( ' ' )
            print( "Random Words: ", randomWords )

if( __name__ ==  ( "__main__" ) ):
    sys.exit( main( ) )
