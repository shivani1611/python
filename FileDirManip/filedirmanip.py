#!/usr/bin/env python3

import os

def main( ):
  while True:
    print( "A) Create new folder" )
    print( "B) Create new file" )
    print( "C) Read from file" )
    print( "D) Write to file" )
    print( "E) Remove folder" )
    print( "F) Remove file" )
    print( "X) Exit Program" )

    choice = ( input( "Enter a selection: " ) )
    choice = ( choice.upper( ) )

    if( not choice ):
      continue
    elif( len( choice ) > ( 2 ) ):
      continue
    elif( choice == ( 'A' ) ):
      folderName = ( input( "Enter new folder name to create: " ) )
      while( not folderName ):
        folderName = ( input( "Enter new folder name to create: " ) )

      if( os.path.exists( folderName ) ):
        print( "Folder already exists!" )
      else:
        os.makedirs( folderName )
      
    elif( choice == ( 'B' ) ):
      fileName = ( input( "Enter new file name to create: " ) )
      while( not fileName ):
        fileName = ( input( "Enter new file name to create: " ) )

      if( os.path.exists( fileName ) ):
        print( "File already exists!" )
      else:
        fileObj = ( open( fileName, 'w' ) )
        fileObj.close( )

    elif( choice == ( 'C' ) ):
      fileName = ( input( "Enter new file name to read from: " ) )
      while( not fileName ):
        fileName = ( input( "Enter new file name to read from: " ) )

      if( not os.path.exists( fileName ) ):
        print( "File does not exist!" )
      else:
        fileObj = ( open( fileName, 'r' ) )
        print( fileObj.read( ) )
        fileObj.close( )

    elif( choice == ( 'D' ) ):
      fileName = ( input( "Enter new file name to write from: " ) )
      while( not fileName ):
        fileName = ( input( "Enter new file name to write from: " ) )

      if( os.path.exists( fileName ) ):
        print( "File already exist!" )
      else:
        fileObj = ( open( fileName, 'w' ) )
        fileContent = ( input( "Enter text to write to new file: " ) )
        fileObj.write( fileContent + "\n" )
        fileObj.close( )

    elif( choice == ( 'E' ) ):
      folderName = ( input( "Enter empty folder name to remove: " ) )
      while( not folderName ):
        folderName = ( input( "Enter empty folder name to remove: " ) )
      
      os.rmdir( folderName ) 

    elif( choice == ( 'F' ) ):
      fileName = ( input( "Enter file name to remove: " ) )
      while( not fileName ):
        folderName = ( input( "Enter file name to remove: " ) )
      
      os.remove( fileName ) 

    elif( choice == ( 'X' ) ):
      break
    else:
      print( "No such option!" )


if( __name__ == ( "__main__" ) ):
  main( )
