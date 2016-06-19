#!/usr/bin/env python3

import json
import sys

def main( ):
  isMinimize = ( True )
  isMaximize = ( False )
  isRestart  = ( False )
  isPrompt   = ( False )
  isBonus    = ( False )
  isArmor    = ( True )
  isWeapon   = ( False )

  height = ( 400 )
  width  = ( 250 )
  length = ( 102 )
  health = ( 80 )
  armor  = ( 20 )
  gun    = ( "1911" )

  opt_player1  = { "armond" : 500 } 
  opt_minimize = { "isMinimize" : isMinimize }
  opt_maximize = { "isMaximize" : isMaximize }
  opt_restart  = { "isRestart" : isRestart  }
  opt_prompt   = { "isPrompt" : isPrompt }
  opt_bonus    = { "isBonus" : isBonus }
  opt_armor    = { "isArmor" : isArmor }
  opt_weapon   = { "isWeapon" : isWeapon }

  opt_height   = { "height" : height }
  opt_width    = { "width" : width }
  opt_length   = { "length" : length }
  opt_health   = { "health" : health }
  opt_armor    = { "armor" : armor }
  opt_gun      = { "gun" : gun }

  opt_list = [ opt_player1, opt_minimize, opt_maximize, opt_restart, opt_prompt, opt_bonus, opt_armor, opt_weapon, opt_height, opt_width, opt_length, opt_health, opt_armor, opt_gun ]


  with open( 'game.dat', 'w' ) as fout:
    json.dump( opt_list, fout )

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
