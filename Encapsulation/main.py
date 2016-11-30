#!/usr/bin/env python3

from sys import exit

class Example(object):
  _var = ( 0 )

  def __init__( self, value ):
    self._var = ( value )

  @property
  def var( self ):
    print( "Retrieving!" )
    return( self._var )

  @var.setter
  def var( self, value ):
    print( "Setting!" )
    self._var = ( value )

  @var.deleter
  def var( self ):
    print( "Deleting!" )
    self._var = ( None )

def main( ):
  a = Example( 5 )
  print( a.var )
  a.var = 1000
  print( a.var )
  del a.var
  

if( __name__ == ( "__main__" ) ):
  exit( main( ) )
