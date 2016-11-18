# write a program where a list is taken along with N. If any two unique values
# add up to N, return true otherwise return false

def FindPair(lst, n):
    for i in range( 0, len( lst ), 1 ):
        for x in range( 0, len( lst ), 1 ):
            if( i != ( x ) ):
                if( lst[i] + lst[x] == ( n ) ):
                    return( True )
    return( False )
    
print( FindPair( [4, 5, 3, 1, 2], 8 ) )
