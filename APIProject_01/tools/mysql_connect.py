#!/usr/bin/env python3

from config import Config as Conf
import pymysql

class Mysql_Connect( object ):


    #--------------------------------------------------------------------------------


    def __init__( self ):

        # establish the mysql connection
        self._conn = pymysql.connect( host   = ( Conf.DB_HOST ), 
                                      port   = ( Conf.DB_PORT ), 
                                      user   = ( Conf.DB_USER ),
                                      passwd = ( Conf.DB_PASS ),
                                      db     = ( Conf.DB_NAME ) )

        print( "\nMySQL Connection Established: {0}\n".format( str( self._conn ) ) )

        return None


    #--------------------------------------------------------------------------------


    def close( self ):

        # terminate the mysql connection
        self._conn.close( )

        return None

    #--------------------------------------------------------------------------------

 
    def select( self, query ):

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

       # close the cursor
        cur.close( ) 

        # return list of lists for every row
        return all_rows


    #--------------------------------------------------------------------------------


    def update( self, query ):

        # establish the cursor
        cur  = ( conn.cursor( ) )

        # retrieve results from query
        result = ( cur.execute( query ) )

        # save the results
        conn.commit( )

        # close the connection
        conn.close( )

        # close the cursor
        cur.close( )

        return result


    #--------------------------------------------------------------------------------


