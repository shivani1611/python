#!/usr/bin/env python3

from request       import Request
from mysql_connect import Mysql_Connect

class TestSuper( object ):

    #--------------------------------------------------------------------------------


    def __init__( self ):
        # establish the request connection
        self._req_conn = ( Request( ) )

        # establish the db connection
        self._db_conn  = ( Mysql_Connect( ) )


        return None

    #--------------------------------------------------------------------------------


    def __enter__( self ):
        return( self )


    #--------------------------------------------------------------------------------


    def __exit__( self, _type, _value, _traceback ):
        # terminate the db connection
        self._db_conn.close( )

        return None

    #--------------------------------------------------------------------------------


    def close( self ):
        self.__exit__( )

        return None

    #--------------------------------------------------------------------------------



