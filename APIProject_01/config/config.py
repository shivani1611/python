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
    API_URL = ( r"http://127.0.0.1/name/" ) # TODO: base64
    API_KEY = ( r"" )                       # TODO: base64
    API_SEC = ( r"" )                       # TODO: base64
    API_VER = ( r"wc/v1" )
    API_WP  = ( True )

    # home desktop
    #url             = ( r"http://127.0.0.1/wp_/" )
    #consumer_key    = ( r"ck_f919d59bfc31c2d417ecdc06c0611f17af4cb593" )
    #consumer_secret = ( r"ck_762bfdfeb5d8588eec6285345820ad548eeedb2c" )

    # home laptop
    #url             = ( r"http://127.0.0.1/wp_/" )
    #consumer_key    = ( r"ck_f919d59bfc31c2d417ecdc06c0611f17af4cb593" )
    #consumer_secret = ( r"ck_762bfdfeb5d8588eec6285345820ad548eeedb2c" )

    # work laptop
    #url             = ( r"http://127.0.0.1/api_test01/" )
    #consumer_key    = ( r"ck_3c39facaa33d0e7dd953167c6f627a4d25022f18" ) # base64
    #consumer_secret = ( r"cs_967e8d9ecd7e75f2254d5a15aaae3a13339235e7" ) # base64

    # main module config - main.py
    MAIN_START_SLEEP = ( 5 )
    MAIN_END_SLEEP   = ( 5 )

    # interface module config - interface.py
    INTF_PATH        = ( "interface.py" )
    INTF_MOD_NAME    = ( "interface" )


    #--------------------------------------------------------------------------------

