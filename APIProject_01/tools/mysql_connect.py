from pymysql import connect

class Mysql_Connect( object ):

    def __init__( self ):
        pass


    def __connect( self, host, port, user, db  ):

        # establish the connection
        conn = ( connect( host = ( host ), 
                          port = ( port ), 
                          user = ( user ), 
                          db = ( db ) ), )

        return conn


    def select( self, db, query ):

        # make a call to establish the connection
        conn = ( self.__connect( db ) )

        # establish the cursor
        cur  = ( self._conn.cursor( ) )

        # execute the specified query
        cur.execute( query )

        # retrieve results from query
        result = ( cur.fetchall( ) )

        # organize the results
        all_rows = []
        for line in result:
            row = []
            for col in line:
                row.append( str( col ) )
            all_rows.append( row )

        # close the connection
        conn.close( )

        # close the cursor
        cur.close( ) 

        return all_rows


def update( self, db, query ):

    # make a call to establish the connection
    conn = self.__connect( db )

    # establish the cursor
    cur  = conn.cursor( )

    # retrieve results from query
    result = ( cur.execute( query ) )

    # save the results
    conn.commit( )

    # close the connection
    conn.close( )

    # close the cursor
    cur.close( )

    return result



