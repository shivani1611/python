#!/usr/bin/env python3


# Instructions on adding test cases:
#
#
#
#
#


from abc           import abstractmethod
from abc           import ABCMeta       as ABC
from mysql_connect import Mysql_Connect as Conn
from request       import Request       as Req


class TestSuper( object, metaclass = ( ABC ) ):


    #--------------------------------------------------------------------------------


    def __init__( self ):
        # establish the request connection
        self._req_conn = ( Req( ) )

        # establish the db connection
        self._db_conn  = ( Conn( ) )


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


    def close( self ):
        self.__exit__( )

        return None


    #--------------------------------------------------------------------------------


    @abstractmethod
    def display_response_information( res_all = ( None ), res_code = ( None ), resp_body = ( None ) ):
        return None


    #--------------------------------------------------------------------------------


    @abstractmethod
    def validate_api_negative_responses( ):
        return None


    #--------------------------------------------------------------------------------


    @abstractmethod
    def validate_api_positive_responses( ):
        return None


    #--------------------------------------------------------------------------------


    @abstractmethod
    def validate_db_responses( ):
        return None


    #--------------------------------------------------------------------------------


    @abstractmethod
    def start_tests( ):
        return None


    #--------------------------------------------------------------------------------



