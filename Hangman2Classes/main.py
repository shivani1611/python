#!/usr/bin/env python3


########################################################
from sys  import exit
from time import sleep
import os


########################################################
class Hangman:
    # class variables
    play_attempts     = ( 0 )
    secret_word       = ( "" )
    secret_word_temp  = ( "" )
    secret_word_len   = ( 0 )
    user_letter       = ( '' )
    secret_hint       = ( "" )
    is_win            = ( False )

    # constants
    PLAY_MAX_ATTEMPTS = ( 6 )

    @classmethod
    def displayTitle( cls ):
        print( "Hangman by Armond" )
        print( "-----------------" )
        return( 0 )


    @classmethod
    def clearScreen( cls ):
        os.system( 'cls' ) if str( os.name ).lower( ) in ( 'nt' ) else os.system( 'clear' ) 
        return( 0 )


    @classmethod
    def resetScreen( cls ):
        cls.clearScreen( )
        cls.displayTitle( )


    @classmethod
    def reset( cls ):
        cls.play_attempts   = ( 0 )
        cls.secret_word_len = ( 0 )
        cls.secret_word     = ( "" )
        cls.user_letter     = ( '' )
        cls.secret_hint     = ( "" )
        cls.is_win          = ( False )
        return( 0 )


    @classmethod
    def displayGrid( cls ):
        head = ( 'O' ) if cls.play_attempts >= ( 1 ) else ( ' ' )
        left_arm = ( '\\' ) if cls.play_attempts >= ( 3 ) else ( ' ' )
        neck = ( '|' ) if cls.play_attempts >= ( 2 ) else ( ' ' )
        right_arm = ( '/' ) if cls.play_attempts >= ( 4 ) else ( ' ' )
        left_leg = ( '/' ) if cls.play_attempts >= ( 5 ) else ( ' ' )
        right_leg = ( '\\' ) if cls.play_attempts >= ( 6 ) else ( ' ' )

        print( "\nSecret word: ", sep = ( '' ), end = ( '' ) )
        if( cls.is_win == ( True ) ):
            print( cls.secret_word_temp, sep = ( '' ), end = ( '' ) )
        else:
            for i in range( 0, len( cls.secret_word ), 1 ):
                print( cls.secret_word_temp[i], sep = ( '' ), end = ( '' ) ) if cls.secret_word[i] == ( '*' ) else print( '*', sep = ( '' ), end = ( '' ) )
        print( "\nSecret hint: {0}\n".format( cls.secret_hint.title( ) ) )

        print( "       /----------\\" )
        print( "       |          |" )
        print( "       {0}          |".format( head ) )
        print( "      {0}{1}{2}         |".format( left_arm, neck, right_arm ) )
        print( "      {0} {1}         |".format( left_leg, right_leg ) )
        print( "                  |" )
        print( "           ===============\n\n" )        
        return( 0 )


    @classmethod
    def isWin( cls ):
      result = ( True )

      for i in range( 0, len( cls.secret_word ) ):
          if( cls.secret_word[i] != ( '*' ) ):
              result = ( False )
      return( result )


    @classmethod
    def playerOne( cls ):
        cls.resetScreen( )

        while( True ):

            cls.secret_word = ( str( input( "(Player One) Enter a secret word: " ) ) )

            if( len( cls.secret_word ) > ( 1 ) ):
                break

        cls.secret_word_temp = ( cls.secret_word )
        cls.secret_word_len  = ( int( len( cls.secret_word ) ) )

        cls.secret_hint      = ( str( input( "(Player One) Provide a brief hint for the word \"{0}\": ".format( cls.secret_word ) ) ) )

        if( len( cls.secret_hint ) <= ( 0 ) ):
            cls.secret_hint = ( "None" )

        return( 0 )

    @classmethod
    def playerTwo( cls ):
        while( True ):
            cls.resetScreen( )
            cls.displayGrid( )

            if( cls.play_attempts >= ( cls.PLAY_MAX_ATTEMPTS ) ):
                cls.is_win = ( False )
                break

            if( cls.isWin( ) == ( True ) ):
                cls.is_win = ( True )
                break

            cls.user_letter = ( str( input( "(Player Two) Enter a letter: " ) ) )
            cls.user_letter = ( cls.user_letter.lower( ) )

            if( len( cls.user_letter ) > ( 1 ) ):
                print( "Error: Please enter only a single letter!" )
                sleep( 1 )
                continue

            if( cls.user_letter not in ( cls.secret_word ).lower( ) ):
                cls.play_attempts += ( 1 )
            else:
                cls.secret_word = ( cls.secret_word.replace( cls.user_letter, '*' ) )

        cls.resetScreen( )
        cls.displayGrid( )
        print( "Congratulations, you win!" ) if cls.is_win == ( True ) else print( "Sorry, you lose! The word was \"{0}\"".format( cls.secret_word_temp ) )
        sleep( 1 )
        return( 0 )


    @classmethod
    def start( cls ):
        while( True ):
            cls.playerOne( )
            cls.playerTwo( )
            cls.reset( )

            if( cls.playAgain( ) == ( False ) ):
                break
        return( 0 )

    @classmethod
    def playAgain( cls ):
        result = ( False )

        while( True ):
            choice = ( str( input( "\nPlay again (y/n): " ) ) )
            choice = ( choice.lower( ) )

            if( choice == ( 'y' ) ):
                result = ( True )
                break
            elif( choice == ( 'n' ) ):
                result = ( False )
                choice = ( '' )
                break
            else:
                choice = ( '' )
                result = ( False )
        return( result )

########################################################
def main( ):
    Hangman( ).start( )
    return( 0 )


########################################################
if( __name__ == ( "__main__" ) ):
    exit( main( ) )


