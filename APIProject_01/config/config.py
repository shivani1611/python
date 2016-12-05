#!/usr/bin/env python3

import base64

class Config( object ):


    #--------------------------------------------------------------------------------


    # database config - mysql_connect.py (db: mysql)
    DB_HOST = ( r"127.0.0.1" )
    DB_PORT = ( 3306 )
    DB_USER = ( r"root" )                   # TODO: base64
    DB_PASS = ( r"pqowieuryt" )             # TODO: base64
    DB_NAME = ( r"wp690" )                  # TODO: base64

    # api request config - request.py
    API_URL = ( r"http://127.0.0.1/api_test01/" )                        # TODO: base64
    API_KEY = ( r"ck_3c39facaa33d0e7dd953167c6f627a4d25022f18" )         # TODO: base64
    API_SEC = ( r"cs_967e8d9ecd7e75f2254d5a15aaae3a13339235e7" )         # TODO: base64
    API_VER = ( r"wc/v1" )
    API_WP  = ( True )

    # main module config - main.py
    MAIN_START_SLEEP = ( 5 )
    MAIN_END_SLEEP   = ( 5 )

    # interface module config - interface.py
    INTF_NAME        = ( "interface.py" )
    INTF_MOD_NAME    = ( "interface" )


    #--------------------------------------------------------------------------------

