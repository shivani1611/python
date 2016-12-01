#!/usr/bin/env python3

from os  import getcwd
from os  import chdir
from imp import load_source

import sys
import os

class ModuleHandler( object ):

    #--------------------------------------------------------------------------------


    @staticmethod
    def load_source_file( _module_name, _file_path ):
        return( load_source( _module_name, os.path.join( os.path.dirname( __file__ ), _file_path ) ) )


    #--------------------------------------------------------------------------------


    @staticmethod
    def load_modules( ):
        pass


    #--------------------------------------------------------------------------------


    @staticmethod
    def print_paths( ):
        for i in sys.path:
            print( "PATH: " + str( i ) + '\n' )

        return None


    #--------------------------------------------------------------------------------


    @staticmethod
    def append_paths( *_paths ):
        for i in range( 0, len( _paths ), 1 ):
            sys.path.append( _paths[i] )

        return None


    #--------------------------------------------------------------------------------


    @staticmethod
    def process_paths( is_display_paths = ( False ) ):

        # get the current working directory
        wd = ( str( ModuleHandler.get_working_directory( ) ) )

        # append new paths to path
        ModuleHandler.append_paths( wd,
                                    wd + "/lib",
                                    wd + "/bin",
                                    wd + "/test_cases",
                                    wd + "/tools" )

        # print the completed path list
        if( is_display_paths == ( True ) ):
            ModuleHandler.print_paths( )
    
        return None


    #--------------------------------------------------------------------------------


    @staticmethod
    def get_working_directory( ):
        return( getcwd( ) )


    #--------------------------------------------------------------------------------


    @staticmethod
    def set_working_directory( _path ):
        chdir( _path )

        return None


    #--------------------------------------------------------------------------------



