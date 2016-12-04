#!/usr/bin/env python3

from tools.module_handler import ModuleHandler as mh
from sys  import exit
from time import sleep


#--------------------------------------------------------------------------------


def main( ):

    # config module - config.py
    CONFIG_PATH = ( "config/config.py" )
    CONFIG_MOD_NAME = ( "config" )
    mh.load_source_file( CONFIG_MOD_NAME, CONFIG_PATH )
    from config import Config as Conf

    # add all import paths
    mh.process_paths( is_display_paths = ( True ) )

    # interface module - interface.py
    mh.load_source_file( Conf.INTF_MOD_NAME, Conf.INTF_NAME )
    from interface import Interface as Intf
    intf = ( Intf( ) )

    # pause before starting
    sleep( Conf.MAIN_START_SLEEP )

    # TODO: setup argv to determine which tests user wants to run
    intf.load_tests( )

    # pause before exiting
    sleep( Conf.MAIN_END_SLEEP )

    # exit the automation
    return( 0 )


#--------------------------------------------------------------------------------


if( __name__ == ( "__main__" ) ):
    exit( main( ) )


