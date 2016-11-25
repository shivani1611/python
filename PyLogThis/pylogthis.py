#!/usr/bin/env python3

from abc      import ABCMeta
from abc      import abstractmethod
from datetime import datetime
from re       import search

#abstract class
class LogThis( object, metaclass = ( ABCMeta ) ):
    _is_enabled = ( False )

    def __init__( self, conf_file, err_file, log_file, is_en = ( False ) ):
        #iterate through the supplied files
        for file in ( err_file, log_file, conf_file ):
            file = ( str( file ).strip( ) )

            #if the file name is empty
            if( not file ):
                raise ValueError( "Missing file name! Be sure to supply a proper file name." )
                break

            #if the file name is invalid
            if( not search( r"[a-zA-Z0-9_]{1,25}\.[a-zA-Z]{1,8}", file ) ):
                raise ValueError( "Invalid file name provided! Be sure "
                                  "to supply a proper extension." )
                break

        #if everything is good, store the files in the instance
        self._config_file_name = ( str( conf_file ) )
        self._error_file_name = ( str( err_file ) )
        self._log_file_name = ( str( log_file ) )

        LogThis.is_enabled = ( is_en )
        return

    @property
    def config_file_name( self ):
        """config_file_name property"""
        return( self._config_file_name )

    @property
    def error_file_name( self ):
        """error_file_name property"""
        return( self._error_file_name )

    @property
    def log_file_name( self ):
        """log_file_name property"""
        return( self._log_file_name )

    @property
    @classmethod
    def is_enabled( cls ):
        """_is_enabled property"""
        return( cls._is_enabled )

    @is_enabled.setter
    @classmethod
    def is_enabled( cls, value ):
        """_is_enabled setter"""
        if( isinstance( value, bool ) ):
            cls._is_enabled = ( value )
        elif( isinstance( value, int ) ):
            if( value == ( 1 ) ):
                cls._is_enabled = ( True )
            elif( value == ( 0 ) ):
                cls._is_enabled = ( False )
        else:
            cls._is_enabled = ( False )

    def is_valid_content( self, content ):
        is_valid = ( True )

        content = ( str( content ) )
        if( len( content ) <= ( 0 ) ):
            raise( "Missing content! Please be sure to supply content." )
            is_valid = ( False )

        return( is_valid )

    def determine_output_type( self, out_type ):
        output_file = ( "" )

        if( not out_type ):
            raise( "Empty output type! Please be sure to supply either"
                   " config, error or log." )

        if( str( out_type ).strip( ).lower( ) == ( "config" ) ):
            output_file = ( self.config_file_name )
        elif( str( out_type ).strip( ).lower( ) == ( "error" ) ):
            output_file = ( self.error_file_name )
        elif( str( out_type ).strip( ).lower( ) == ( "log" ) ):
            output_file = ( self.log_file_name )
        else:
            raise( "Incorrect output type! Please be sure to supply either"
                   " config, error or log." )
        return( output_file )

    @abstractmethod
    def show_doc( self ):
         """display information about the class object"""
         return

    @abstractmethod
    def string_output( self, output_type, content ):
        """write log content (string) to a specified file"""
        if( WriteThis.is_enabled ):
            pass
        return

    @abstractmethod
    def list_output( self, output_type, content, delim ):
        """write log content (list) to a specified file"""
        if( WriteThis.is_enabled ):
            pass
        return

#non-abstract class
class WriteThis( LogThis ):
    def show_doc( self ):
        print( "{x} id ({y}), only accepts three "
               "string values representing file names".format( x = ( self ), y = ( id( self ) ) ) )

    def string_output( self, output_type, content ):
        """write log content (string) to a specified filer"""
        file_name = ( self.determine_output_type( output_type ) )

        if( not file_name ):
            raise( ValueError( "File name seems to be empty!" ) )

        with open( file_name, 'a' ) as fout:
            if( self.is_valid_content( content ) ):
                fout.write( "[{0}] [{1}]\n".format( str( datetime.now( ) )[0:19:1], content.lower( ) ) )
        return

    def list_output( self, output_type, content, delim ):
        """write log content (list) to a specified file using a delimiter"""
        file_name = ( determine_output_type( out_type ) )
        if( not file_name ):
            raise( ValueError( "File name seems to be empty!" ) )
        return
