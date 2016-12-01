#!/usr/bin/env python3

from test_super import TestSuper
import json

class TestCase_Create_Product( TestSuper ):

    #--------------------------------------------------------------------------------


    def __init__( self ):
        # information about this test case
        self._test_case_title    = ( "Create New Product" )
        self._test_case_category = ( "products" )
        self._end_point          = ( "products" )

        # fields to validate with api/db
        self._title     = ( "Miracle" )
        self._price     = ( "21.99" )

        super( ).__init__( )

        return None


    #--------------------------------------------------------------------------------


    def start_test( self ):
        self.test_api( )
        self.test_db( )

        return None


    #--------------------------------------------------------------------------------


    def test_api( self ):

        # actual payload
        payload = {
            "name": "{name}".format( name = ( self._title ) ),
            "type": "simple",
            "regular_price": "{price}".format( price = ( self._price ) ),
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
            "images": 
            [
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

        response_all = ( self._req_conn.post( self._end_point, payload ) )
        response_code = ( response_all[0] )
        response_body = ( response_all[1] )

        # verify status code is correct
        assert response_code == ( 201 ), r"The status code returned" \
        " creating product is not as expected.Expected: 201, Actual:" \
        " {act}".format( act = response_code )

        # check the responses and verify
        rs_title = ( response_body["name"] )
        rs_price = ( response_body["regular_price"] )
        self._id = ( response_body["id"] )

        print( "id is: {}".format( str( self._id ) ) )

        assert rs_title == ( self._title ), r"The title in response is" \
        " not the same as in the response title is: {}".format( rs_title )

        assert rs_price == ( self._price ), r"The price is not correct!"

        print( "API Testing passed - {title}!".format( title = ( self._test_case_title ) ) )

        return None


    #--------------------------------------------------------------------------------


    def test_db( self ):

        # get information from DB
        query = r"SELECT p.post_title, p.post_type, pm.meta_value from wp690.apitest_posts p JOIN wp690.apitest_postmeta pm on p.id=pm.post_id WHERE p.id={pid} AND pm.meta_key='_regular_price';".format( pid = self._id )

        query_results = ( self._db_conn.select( query ) )

        print( query_results[0] )

        # extracting the data from db
        db_title         = query_results[0][0]
        db_type          = query_results[0][1] 
        db_regular_price = query_results[0][2]

        assert db_title == self._title, r"The title in DB is not as expected. Actual Results: {}, Expected Results: {}".format( db_title, title )

        assert db_type == "product", r"The post_type in DB is not 'product.' Expected: {}".format( db_type )

        assert db_regular_price == self._price, r"The regular price in DB is not as expected. Actual Result: {}, Expected Result: {}".format( db_regular_price, price )

        print( "DB Testing passed - {title}!".format( title = ( self._test_case_title ) ) )

        return None


    #--------------------------------------------------------------------------------



