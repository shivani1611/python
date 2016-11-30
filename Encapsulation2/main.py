#!/usr/bin/env python3

from sys import exit

class Example( object ):
  def __init__( self, val ):
    self._val = ( val )

  @property
  def val( self ):
    print( "Accessing" )
    return( self._val )

  @val.setter
  def val( self, new_val ):
    print( "Setter" )
    self._val = ( new_val )

  @val.deleter
  def val( self ):
    print( "Deleter" )
    self._val = ( None )

def main( ):
  ex = Example( 5 )

  print( ex.val )
  ex.val = 5
  print( ex.val )
  del ex.val
  print( ex.val )

  return( 0 )

if( __name__ == ( "__main__" ) ):
  exit( main( ) )
