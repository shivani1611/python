#!/usr/bin/env python3

from pprint import pprint

import json
import sys

def main( ):
  options = []

  with open( "game.dat", 'r' ) as fin:  
    options = json.load( fin )

  for item in options:
    if( "isMinimize" in item.keys( ) ):
      isMinimize = ( list( item.values( ) ) )
    elif( "isMaximize" in item.keys( ) ):
      isMaximize = ( list( item.values( ) ) )
    elif( "isRestart" in item.keys( ) ):
      isRestart = ( list( item.values( ) ) )
    elif( "isPrompt" in item.keys( ) ):
      isPrompt = ( list( item.values( ) ) )
    elif( "isBonus" in item.keys( ) ):
      isBonus = ( list( item.values( ) ) )
    elif( "isWeapon" in item.keys( ) ):
      isWeapon = ( list( item.values( ) ) )
    elif( "armor" in item.keys( ) ):
      armor = ( list( item.values( ) ) )
    elif( "height" in item.keys( ) ):
      height = ( list( item.values( ) ) )
    elif( "width" in item.keys( ) ):
      width = ( list( item.values( ) ) )
    elif( "length" in item.keys( ) ):
      length =( list( item.values( ) ) )
    elif( "health" in item.keys( ) ):
      health = ( list( item.values( ) ) )
    elif( "gun" in item.keys( ) ):
      gun = ( list( item.values( ) ) )

  print( "isMinimize:", isMinimize )
  print( "isMaximize:", isMaximize )
  print( "isRestart :", isRestart )
  print( "isPrompt  :", isPrompt )
  print( "isBonus   :", isBonus )
  print( "isWeapon  :", isWeapon )
  print( "armor     :", armor )
  print( "height    :", height )
  print( "width     :", width )
  print( "length    :", length )
  print( "health    :", health )
  print( "gun       :", gun )

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
