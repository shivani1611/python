#!/usr/bin/env python3

def remove_duplicates( l ):

    is_match = False
    temp_l = l

    for x in range( len( l ) - 1, -1, -1 ):
        for y in range( len( temp_l ) -1, -1, -1 ):
            if x != y:
                if l[x] == temp_l[y]:
                   temp_l.pop( y )

    return temp_l

def main( ):

    a = [1, 2, 3, 3, 3, 3, 1, 4, 5, 6]

    a = remove_duplicates( a )

    print( "Unique List: ", a )

    return 0

if __name__ == "__main__":
    main( )
