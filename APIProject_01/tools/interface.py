#!/usr/bin/env python3

from module_handler import ModuleHandler as mh

mh.load_source_file( "test_create_product", "../test_cases/test_create_product.py" )
from test_create_product import TestCase_Create_Product

class Interface( object ):

    #--------------------------------------------------------------------------------


    def __init__( self ):
        return None


    #--------------------------------------------------------------------------------


    def execute_all_tests( self ):
        with TestCase_Create_Product( ) as tc:

            # execute all the test cases
            tc.start_test( )


    #--------------------------------------------------------------------------------



