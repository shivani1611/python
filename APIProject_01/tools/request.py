from woocommerce import API

class Request( object ):

    def __init__( self ):
        url             = ( r"http://127.0.0.1/api_test01/" )
        consumer_key    = ( r"ck_3c39facaa33d0e7dd953167c6f627a4d25022f18" )
        consumer_secret = ( r"cs_967e8d9ecd7e75f2254d5a15aaae3a13339235e7" )
        wp_api          = ( True )
        version         = ( r"wc/v1" )

        self._wcapi = API(
            url             = ( url ),
            consumer_key    = ( consumer_key ),
            consumer_secret = ( consumer_secret ),
            wp_api          = ( wp_api ),
            version         = ( version ), )

        return None


    def test_api_connection( self ):
        return self._wcapi.get( "" ).json( )

 
    def post(self, end_point, payload ):
        result        = ( self._wcapi.post( end_point, payload ) )
        response_code = ( result.status_code )
        body          = ( result.json( ) )
        url           = ( result.url )

        return [response_code, body, url] 


    def get( self, end_point ):
        result        = ( self._wcapi.get( end_point ) )
        response_code = ( result.status_code )
        body          = ( result.json( ) )
        url           = ( result.url )

        return [response_code, body, url] 


