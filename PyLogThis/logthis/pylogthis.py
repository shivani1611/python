#!/usr/bin/env python3

from abc      import ABCMeta
from abc      import abstractmethod
from datetime import datetime
from os       import path
from os       import remove
from re       import search

#abstract class
class LogThis( object, metaclass = ( ABCMeta ) ):
    _is_conf_enabled = ( False )
    _is_err_enabled  = ( False )
    _is_log_enabled  = ( False )

    def __init__( self, conf_file, err_file, log_file ):
        #iterate through the supplied files
        for file in ( conf_file, err_file, log_file ):
            file = ( str( file ).strip( ) )

            #if the file name field is empty
            if( not file ):
                raise ValueError( "Missing file name! Be sure to supply a proper file name." )
                break

            #if the file name field is invalid
            if( not search( r"[a-zA-Z0-9_]{1,25}\.[a-zA-Z]{1,8}", file ) ):
                raise ValueError( "Invalid file name provided! Be sure "
                                  "to supply a proper extension." )
                break

        #if everything is good, store the files in the instance
        self._config_file_name = ( str( conf_file ) )
        self._error_file_name  = ( str( err_file ) )
        self._log_file_name    = ( str( log_file ) )
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
    def is_conf_enabled( self ):
        """_is_conf_enabled property"""
        return( self._is_conf_enabled )

    @property
    def is_err_enabled( self ):
        """_is_err_enabled property"""
        return( self._is_err_enabled )

    @property
    def is_log_enabled( self ):
        """_is_log_enabled property"""
        return( self._is_log_enabled )

    @is_conf_enabled.setter
    def is_conf_enabled( self, value ):
        """_is_conf_enabled setter"""
        if( isinstance( value, bool ) ):
            self._is_conf_enabled = ( value )
        elif( isinstance( value, int ) ):
            if( value == ( 1 ) ):
                self._is_conf_enabled = ( True )
            elif( value == ( 0 ) ):
                self._is_conf_enabled = ( False )
        else:
            self._is_conf_enabled = ( False )
        return

    @is_err_enabled.setter
    def is_err_enabled( self, value ):
        """_is_err_enabled setter"""
        if( isinstance( value, bool ) ):
            self._is_err_enabled = ( value )
        elif( isinstance( value, int ) ):
            if( value == ( 1 ) ):
                self._is_err_enabled = ( True )
            elif( value == ( 0 ) ):
                self._is_err_enabled = ( False )
        else:
            self._is_err_enabled = ( False )
        return

    @is_log_enabled.setter
    def is_log_enabled( self, value ):
        """_is_log_enabled setter"""
        if( isinstance( value, bool ) ):
            self._is_log_enabled = ( value )
        elif( isinstance( value, int ) ):
            if( value == ( 1 ) ):
                self._is_log_enabled = ( True )
            elif( value == ( 0 ) ):
                self._is_log_enabled = ( False )
        else:
            self._is_log_enabled = ( False )
        return

    def is_content_valid( self, content ):
        is_valid = ( True )

        content = ( str( content ) )
        if( len( content ) <= ( 0 ) ):
            is_valid = ( False )
            raise( ValueError( "Missing content! Please be sure to supply it." ) )
        return( is_valid )

    def determine_output_type( self, out_type ):
        output_file = ( "" )

        if( not out_type ):
            raise( ValueError( "Empty output type! Please be sure to supply either"
                               " conf, err or log." ) )

        if( out_type == ( "conf" ) ):
            output_file = ( self.config_file_name )
        elif( out_type == ( "err" ) ):
            output_file = ( self.error_file_name )
        elif( out_type == ( "log" ) ):
            output_file = ( self.log_file_name )
        else:
            raise( ValueError( "Incorrect output type! Please be sure to supply either"
                               " conf, err or log." ) )
        return( output_file )

    @abstractmethod
    def show_doc( self ):
         """display information about the class object"""
         return

    @abstractmethod
    def string_output( self, output_type, string_content ):
        """write log content (string) to a specified file"""
        return

    @abstractmethod
    def list_output( self, output_type, list_content, delim ):
        """write log content (list) to a specified file"""
        return

    @abstractmethod
    def is_file_exist( self, file_name ):
        """check if a specified file exists"""
        return

    @abstractmethod
    def create_file( self, file_name ):
        """touch and create an empty new file"""
        return

    @abstractmethod
    def remove_file( self, file_name ):
        """discard a file and permanently remove it"""
        return

#non-abstract class
class WriteThis( LogThis ):
    def show_doc( self ):
        print( "{x} id ({y}), accepts output_type, string_content, err_func_call, err_line_num, err_type, err_msg, err_filename"
               "string values representing file names".format( 
               x = ( self ), y = ( id( self ) ) ) )
        return

    def string_output(self, output_type: object, string_content: object, err_func_call: object = (""),
                      err_line_num: object = (""), err_type: object = (""), err_msg: object = (""), err_filename: object = ("")) -> object:
        """write log content (string) to a specified filer"""
        if( self.is_content_valid( string_content ) == ( False ) ):
            return

        the_main_output = ( "" )
        write_mode = ( '' )
        output_type = str( output_type ).strip( ).lower( )
 
        file_name = ( self.determine_output_type( output_type ) )

        if( not file_name ):
            raise( ValueError( "File name field seems to be empty!" ) )

        if( "conf" in ( output_type ) ):
            if( not self.is_conf_enabled ):
                return
            the_main_output += ( str( string_content ).lower( ) + '\n' )
            write_mode = ( 'w' )
        elif( "err" in ( output_type ) ):
            if( not self.is_err_enabled ):
                return
            the_main_output += ( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                               "[ {0} ]\n[ {1} ]\n[ {2} ]\n[ {3} ]\n[ {4} ]\n[ {5} ]"
                               "\n\n".format( 
                               "DATE: " + str( datetime.now( ) )[0:19:1], 
                               "FILE: " + str( err_filename ),
                               "FUNC: " + str( err_func_call ) + 
                               " (" + str( id( err_func_call ) ) + ')',                         
                               "LINE: " + str( err_line_num ), 
                               "TYPE: " + str( err_type ), 
                               "ERR : " + str( string_content ).lower( ) ) )
            write_mode = ( 'a' )
        elif( "log" in ( output_type ) ):
            if( not self.is_log_enabled ):
                return
            the_main_output += ( "[ {0} ] [ {1} ]\n".format( 
                               "DATE: " + str( datetime.now( ) )[0:19:1], 
                               "LOG: " + str( string_content ).lower( ) ) )

            write_mode = ( 'a' )
        else:
            raise( ValueError( "Incorrect output type! Please be sure to supply either"
                   " conf, err or log." ) )

        with open( file_name, write_mode ) as fout:
            fout.write( the_main_output )
        return

    def list_output( self, output_type, list_content, delim = ( '\n' ) ):
        """write log content (list) to a specified filer"""
        if( self.is_content_valid( list_content ) == ( False ) ):
            return

        output_type = str( output_type ).strip( ).lower( )
        write_mode = ( '' )
        file_name = ( self.determine_output_type( output_type ) )

        if( not file_name ):
            raise( ValueError( "File name seems to be empty!" ) )

        if( "config" in ( output_type ) ):
            if( not self.is_conf_enabled ):
                return
            write_mode = ( 'w' )
        elif( "log" in ( output_type ) ):
            if( not self.is_log_enabled ):
                return
            write_mode = ( 'a' )
        else:
            raise( ValueError( "Incorrect output type! Please be sure to supply either"
                   " conf or log." ) )
        with open( file_name, write_mode ) as fout:
            for item in list_content:
                 fout.write( "{0}{1}".format( str( item ), str( delim ) ) )
        return

    def is_file_exist( self, file_name ):
        _is_file_exist = ( False )
        if( path.exists( file_name ) ):
            _is_file_exist = ( True )
        return( _is_file_exist )

    def create_file( self, file_name ):
        if( not self.is_file_exist( file_name ) ):
            with open( file_name, 'w' ) as fout:
                fout.write( "" )
        return

    def remove_file( self, file_name ):
        if( self.is_file_exist( file_name ) ):
            remove( file_name )
        return
