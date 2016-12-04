#!/usr/bin/env python3

from woocommerce import API
import base64


class Request( object ):


    #--------------------------------------------------------------------------------


    def __init__( self ):

        CONFIG_PATH = ( "../config/config.py" )
        CONFIG_MOD_NAME = ( "config" )
        mh.load_source_file( CONFIG_MOD_NAME, CONFIG_PATH )
        from config import Config as Conf

        self._wcapi = API(
            url             = ( Conf.API_URL ),
            consumer_key    = ( Conf.API_KEY ),
            consumer_secret = ( Conf.API_SEC ),
            wp_api          = ( Conf.API_WP ),
            version         = ( Conf.API_VER ), )

        print( "\nAPI Connection Established: {0}\n".format( str( self._wcapi ) )

        return None


    #--------------------------------------------------------------------------------


    def test_api_connection( self ):
        return self._wcapi.get( "" ).json( )

 
    #--------------------------------------------------------------------------------


    def post( self, end_point, payload ):
        result        = ( self._wcapi.post( end_point, payload ) )
        response_code = ( result.status_code )
        body          = ( result.json( ) )
        url           = ( result.url )

        return [response_code, body, url] 


    #--------------------------------------------------------------------------------


    def get( self, end_point ):
        result        = ( self._wcapi.get( end_point ) )
        response_code = ( result.status_code )
        body          = ( result.json( ) )
        url           = ( result.url )

        return [response_code, body, url] 


    #--------------------------------------------------------------------------------


