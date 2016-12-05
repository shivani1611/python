#!/usr/bin/env python3

from _super import TestSuper
import json

class TestCase_Create_Product( TestSuper ):


    #--------------------------------------------------------------------------------


    def __init__( self ):
        # information about this test case
        self._test_case_title    = ( "Create New Product" )
        self._end_point          = ( "products" )

        self.is_test_case_passed = ( True )

       # call the superclass constructor (superclass constructor in: _super.py)
        super( ).__init__( )

        return None


    #--------------------------------------------------------------------------------


    def start_tests( self ):

        # positive test(s)
        self.test_api_create_product( )
        self.test_db_create_product( )

        # negative test(s)
        self.test_api_blank_payload( )
        self.test_api_missing_fields( )
        self.test_api_empty_fields( )

        return None


    #--------------------------------------------------------------------------------


    @staticmethod
    def display_response_information( res_all = ( None ), res_code = ( None ), res_body = ( None ) ):
        if( res_all ):
            print( "\n--> Response All : {0}".format( str( res_all ) ) )

        if( res_code ):
            print( "\n--> Response Code: {0}".format( str( res_code ) ) )

        if( res_body ):
            print( "\n--> Response Body: {0}".format( str( res_body ) ) )

        print( )

        return None


    #--------------------------------------------------------------------------------


    def validate_api_negative_responses( self,
                                         response_all,
                                         use_case_name,
                                         error_msg,
                                         exp_res_code,
                                         exp_res_type,
                                         exp_res_msg ):
        
        # flag to determine if test passed
        is_use_case_passed = ( True )

        # actual outcomes
        act_res_code      = ( response_all[0] )
        act_res_body      = ( response_all[1] )
        act_res_msg       = ( act_res_body['message'] )
        act_res_type      = ( act_res_body['code'] )

        # display information about the response
        #self.display_response_information( res_all  = ( response_all ), 
        #                                   res_code = ( act_res_code ), 
        #                                   res_body = ( act_res_body ) )

        # assert: 1 (response code check)
        assert( act_res_code == ( exp_res_code ) ),\
        r"MSG: {err_msg} for use case: '{uc_title}' - [API Negative Test] -"\
        " [{tc_title}] - Expected: {exp_res}, Actual: {act_res}"\
        "".format( err_msg = ( error_msg ), uc_title = ( use_case_name ),
        tc_title = ( self._test_case_title ), exp_res = ( exp_res_code ),\
        act_res = ( act_res_code ) )

        # assert: 2 (response type check)
        assert( act_res_type == ( exp_res_type ) ),\
        r"MSG: {err_msg} for use case: '{uc_title}' - [API Negative Test] -"\
        " [{tc_title}] - Expected: {exp_res}, Actual: {act_res}"\
        "".format( err_msg = ( error_msg ), uc_title = ( use_case_name ),
        tc_title = ( self._test_case_title ), exp_res = ( exp_res_type ),\
        act_res = ( act_res_type ) )

        # assert: 3 (response message check)
        assert( act_res_msg == ( exp_res_msg ) ),\
        r"MSG: {err_msg} for use case: '{uc_title}' - [API Negative Test] -"\
        " [{tc_title}] - Expected: {exp_res}, Actual: {act_res}"\
        "".format( err_msg = ( error_msg ), uc_title = ( use_case_name ),
        tc_title = ( self._test_case_title ), exp_res = ( exp_res_msg ),\
        act_res = ( act_res_msg ) )

        return is_use_case_passed
 

    #--------------------------------------------------------------------------------


    def validate_api_positive_responses( self,
                                         response_all,
                                         use_case_name,
                                         err_msg,
                                         exp_res_code,
                                         exp_name,
                                         exp_regular_price ):
        
        # flag to determine if test passed
        is_use_case_passed = ( True )

        # actual outcomes
        act_res_code      = ( response_all[0] )
        act_res_body      = ( response_all[1] )
        self._act_id      = ( act_res_body["id"] )
        act_name          = ( act_res_body["name"] )
        act_regular_price = ( act_res_body["regular_price"] )

        # display information about the response
        #self.display_response_information( res_all  = ( response_all ), 
        #                                   res_code = ( act_res_code ), 
        #                                   res_body = ( act_res_body ) )

        # assert: 1 (response code check)
        assert( act_res_code == ( exp_res_code ) ),\
        r"MSG: {err_msg} for use case: '{uc_title}' - [API Positive Test] -"\
        " [{tc_title}] - Expected: {exp_res}, Actual: {act_res}"\
        "".format( err_msg = ( error_msg ), uc_title = ( use_case_name ),
        tc_title = ( self._test_case_title ), exp_res = ( exp_res_code ),\
        act_res = ( act_res_code ) )

        # assert: 2 (title/name check)
        assert( act_name == ( exp_name ) ),\
        r"MSG: {err_msg} for use case: '{uc_title}' - [API Positive Test] -"\
        " [{tc_title}] - Expected: {exp_res}, Actual: {act_res}"\
        "".format( err_msg = ( error_msg ), uc_title = ( use_case_name ),
        tc_title = ( self._test_case_title ), exp_res = ( exp_res_code ),\
        act_res = ( act_res_code ) )

        # assert: 3 (price check)
        assert( act_regular_price == ( exp_regular_price ) ),\
        r"MSG: {err_msg} for use case: '{uc_title}' - [API Positive Test] -"\
        " [{tc_title}] - Expected: {exp_res}, Actual: {act_res}"\
        "".format( err_msg = ( error_msg ), uc_title = ( use_case_name ),
        tc_title = ( self._test_case_title ), exp_res = ( exp_res_code ),\
        act_res = ( act_res_code ) )

        return is_use_case_passed
 

    #--------------------------------------------------------------------------------

    def validate_db_responses( self,
                               use_case_name,
                               db_id,
                               qry_res,
                               err_msg,
                               exp_name,
                               exp_regular_price ):
       
        # flag to determine if test passed
        is_use_case_passed = ( True )

        # expected outcomes
        exp_type          = ( "product" ) 

        # actual outcomes
        act_name          = ( qry_res[0][0] )
        act_type          = ( qry_res[0][1] )
        act_regular_price = ( qry_res[0][2] )


        # assert: 1 (title/name check)
        assert( act_name == ( exp_name ) ),\
        r"MSG: {err_msg} for use case: '{uc_title}' - [DB Test] -"\
        " [{tc_title}] - Expected: {exp_title}, Actual: {act_title}"\
        "".format( err_msg = ( error_msg ), uc_title = ( use_case_name ),
        tc_title = ( self._test_case_title ), exp_title = ( exp_name ),\
        act_title = ( act_name ) )

        # assert: 2 (type check)
        assert( act_type == ( exp_type ) ),\
        r"MSG: {err_msg} for use case: '{uc_title}' - [DB Test] -"\
        " [{tc_title}] - Expected: {_exp_type}, Actual: {_act_type}"\
        "".format( err_msg = ( error_msg ), uc_title = ( use_case_name ),
        tc_title = ( self._test_case_title ), exp_type = ( exp_type ),\
        act_type = ( act_type ) )

        # assert: 3 (price check)
        assert( act_regular_price == ( exp_regular_price ) ),\
        r"MSG: {err_msg} for use case: '{uc_title}' - [DB Test] -"\
        " [{tc_title}] - Expected: {_exp_regular_price}, Actual: {_act_regular_price}"\
        "".format( err_msg = ( error_msg ), uc_title = ( use_case_name ),
        tc_title = ( self._test_case_title ), exp_regular_price = ( _exp_regular_price ),\
        act_regular_price = ( _act_regular_price ) )

        return is_use_case_passed
 

    #--------------------------------------------------------------------------------


    # negative test
    def test_api_empty_fields( self ):

        use_case_title = ( "Empty Fields" )
        use_case_error = ( "Required fields cannot be empty" )

        # expected outcomes
        expected_response_code    = ( 400 )
        expected_response_type    = ( "rest_invalid_param" )
        expected_response_message = ( "Invalid parameter(s): type" )

        # test case payload (missing required fields - expected response code is 400) 
        payload = { "regular_price" : "", "type" : "", "title" : "" }

        # extract necessary information 
        response_all = ( self._req_conn.post( self._end_point, payload ) )

        result = (\
        self.validate_api_negative_responses( response_all,
                                              use_case_title,
                                              use_case_error,
                                              expected_response_code,
                                              expected_response_type,
                                              expected_response_message ) )
        
        print( "  ==> API test passed: Negative Test ['{tc_title}'] - ['{uc_title}']"
        "".format( uc_title = ( use_case_title  ), tc_title = ( self._test_case_title ) ) )

        return result


    #--------------------------------------------------------------------------------


    # negative test
    def test_api_missing_fields( self ):

        use_case_title = ( "Missing Fields" )
        use_case_error = ( "Required fields must be supplied in the payload" )

        # expected outcomes
        expected_response_code    = ( 400 )
        expected_response_message = ( "Content, title, and excerpt are empty." )
        expected_response_type    = ( "empty_content" )

        # test case payload (missing required fields - expected response code is 400) 
        payload = { "regular_price" : "19.99", "type" : "simple" }
        
        # extract necessary information 
        response_all = ( self._req_conn.post( self._end_point, payload ) )

        result = (\
        self.validate_api_negative_responses( response_all,
                                              use_case_title,
                                              use_case_error,
                                              expected_response_code,
                                              expected_response_type,
                                              expected_response_message ) )
        
        print( "  ==> API test passed: Negative Test ['{tc_title}'] - ['{uc_title}']"
        "".format( uc_title = ( use_case_title  ), tc_title = ( self._test_case_title ) ) )

        return result


    #--------------------------------------------------------------------------------


    # negative test
    def test_api_blank_payload( self ):

        use_case_title = ( "Blank Payload" )
        use_case_error = ( "Payload cannot be blank" )

        # expected outcomes
        expected_response_code    = ( 400 )
        expected_response_message = ( "Content, title, and excerpt are empty." )
        expected_response_type    = ( "empty_content" )

        # test case payload ( empty payload - expected response code is 400 )
        payload = { }

        # extract necessary information 
        response_all = ( self._req_conn.post( self._end_point, payload ) )

        result = (\
        self.validate_api_negative_responses( response_all,
                                              use_case_title,
                                              use_case_error,
                                              expected_response_code,
                                              expected_response_type,
                                              expected_response_message ) )
        
        print( "  ==> API test passed: Negative Test ['{tc_title}'] - ['{uc_title}']"
        "".format( uc_title = ( use_case_title  ), tc_title = ( self._test_case_title ) ) )

        return result


    #--------------------------------------------------------------------------------


    # positive test
    def test_api_create_product( self ):

        use_case_title = ( "Create Product" )
        use_case_error = ( "Unable to create new product" )

        # expected outcomes
        expected_response_code       = ( 201 )
        self._expected_name          = ( "test_positive_create_product" )
        self._expected_regular_price = ( "1.99" )

        # test case payload ( populated payload - expected response code is 201 )
        payload = {
            "name": "{name}".format( name = ( self._expected_name ) ),
            "type": "simple",
            "regular_price": "{price}".format( price = ( self._expected_regular_price ) ),
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

        # extract necessary information 
        response_all  = ( self._req_conn.post( self._end_point, payload ) )

        self._expected_name          = ( "test_positive_create_product" )
        self._expected_regular_price = ( "1.99" )

        result = (\
        self.validate_api_positive_responses( response_all,
                                              use_case_title,
                                              use_case_error,
                                              expected_response_code,
                                              self._expected_name,
                                              self._expected_regular_price ) )

        print( "  ==> API test passed: Positive Test ['{test_case_title}'] - ['Populated Payload']"
        "".format( test_case_title = ( self._test_case_title ) ) )

        return result


    #--------------------------------------------------------------------------------


    def test_db_create_product( self ):

         # mysql query 
        query = r"SELECT p.post_title, p.post_type, pm.meta_value from wp690.apitest_posts p JOIN wp690.apitest_postmeta pm on p.id=pm.post_id WHERE p.id={pid} AND pm.meta_key='_regular_price';".format( pid = ( self._act_id ) )

        # process the query
        query_results = ( self._db_conn.select( query ) )

    def validate_db_responses( self,
                               use_case_name,
                               db_id,
                               qry_res,
                               err_msg,
                               exp_name,
                               exp_regular_price ):

        result = (\
        self.validate_db_responses( use_case_title,
                                    self._act_id,
                                    query_results,
                                    use_case_error,
                                    self._expected_name,
                                    self._expected_regular_price ) )

        print( "  ==> DB  test passed: ['{test_case_title}'] - ['Populated Payload']"
        "".format( test_case_title = ( self._test_case_title ) ) )

        return result


    #--------------------------------------------------------------------------------



