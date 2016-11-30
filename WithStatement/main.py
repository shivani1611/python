#!/usr/bin/env python3

class MyMethod(object):
  def __init__( self ):
    print( "constructing" )

  def __enter__( self ):
    print( "entering" )
    return self

  def __exit__( self, type, value, traceback ):
    print( "exiting" )
    print( "error type: {0}".format( type ) )
    print( "error value: {0}".format( value ) )
    print( "error traceback: {0}".format( traceback ) )

  def say_hi( self ):
    print( "hello" )

with MyMethod( ) as mm:
  mm.say_hi( )

  
