

def is_match( l1, l2 ):
    match_list = []
    is_match = False

    for x in l1:
        for y in l2:
            if x == y:
                match_list.append( True )
                break
    if len( match_list ) == len( l2 ):
        is_match = True
    return is_match



