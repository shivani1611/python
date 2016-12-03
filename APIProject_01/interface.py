#!/usr/bin/env python3

from module_handler import ModuleHandler as mh


class Interface( object ):


    #--------------------------------------------------------------------------------


    def __init__( self ):

        self.test_case_count = ( 0 )

        return None


    #--------------------------------------------------------------------------------


    def load_all_tests( self ):
        mh.load_source_file( "test_create_product", "../test_cases/test_create_product.py" )
        from test_create_product import TestCase_Create_Product as test_case

        self._execute_test( test_case )

        return None


    #--------------------------------------------------------------------------------


    def _execute_test( self, test_case ):
        with test_case( ) as tc:

            # execute all the test cases
            tc.start_tests( )

        return None


    #--------------------------------------------------------------------------------


