from tools.request       import Request
from tools.mysql_connect import Mysql_Connect

import json

def create_product( ):

    end_point = ( "products" )
    title  = ( "Miracle" )
    price  = ( "21.99" )

    payload = {
    "name": "Miracle",
    "type": "simple",
    "regular_price": "21.99",
    "description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.",
    "short_description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
    "categories": [
        {
            "id": 9
        },
        {
            "id": 14
        }
    ],
    "images": [
        {
            "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_front.jpg",
            "position": 0
        },
        {
            "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_back.jpg",
            "position": 1
        }
    ]
}

    req = ( Request( ) )
    response = ( req.post( end_point, payload ) )
    response_code = ( response[0] )
    response_body = ( response[1] )

    # verify status code is correct
    assert response_code == ( 201 ), r"The status code returned" \
    " creating product is not as expected.Expected: 201, Actual:" \
    " {act}".format( act = response_code )

    # check the responses and verify
    rs_title = ( response_body["name"] )
    rs_price = ( response_body["regular_price"] )
    rs_id    = ( response_body["id"] )

    assert rs_title == ( title ), r"The title in response is" \
    " not the same as in the response title is: {}".format( rs_title )

    assert rs_price == price, "The price is not correct!"
    
    print( "Product testing passed!" )

create_product( )
