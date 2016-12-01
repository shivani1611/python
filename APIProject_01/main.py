#!/usr/bin/env python3

from tools.module_handler import ModuleHandler as mh
from sys import exit

def main( ):

    # add all the paths
    mh.process_paths( is_display_paths = ( False ) )

    # load interface.py
    mh.load_source_file( "interface", "interface.py" )
    from interface import Interface

    # load all the modules
    mh.load_modules( )

    # load the main interface
    intf = ( Interface( ) )

    # TODO: setup argv to determine which tests user wants to run
    intf.execute_all_tests( )

    # exit the automation
    return( 0 )


#--------------------------------------------------------------------------------


if( __name__ == ( "__main__" ) ):
    exit( main( ) )
