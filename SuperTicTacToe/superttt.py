#!/usr/bin/env python3

from os     import system
from random import randint
from sys    import exit

class SuperTTT( object ):

    title = "Super Tic Tac Toe By Armond"

    # count number of wins per player
    x_wins_times = 0
    y_wins_times = 0

    # grid elements
    a = []
    b = []
    c = []
    d = []
    e = []

    # determine the game mode
    game_mode = ""

    # determine who goes first
    x_player = ""
    y_player = ""


    @staticmethod
    def clearScreen( ):

        system( "clear" )


    @classmethod
    def tie_logic( cls ):
        is_tie = False

        if( cls.a[0] != " " and cls.a[1] != " " and cls.a[2] != " " and cls.a[3] != " " and cls.a[4] != " "
        and cls.b[0] != " " and cls.b[1] != " " and cls.b[2] != " " and cls.b[3] != " " and cls.b[4] != " "
        and cls.c[0] != " " and cls.c[1] != " " and cls.c[2] != " " and cls.c[3] != " " and cls.c[4] != " "
        and cls.d[0] != " " and cls.d[1] != " " and cls.d[2] != " " and cls.d[3] != " " and cls.d[4] != " "
        and cls.e[0] != " " and cls.e[1] != " " and cls.e[2] != " " and cls.e[3] != " " and cls.e[4] != " " ):
            is_tie = True

        return( is_tie )

    @classmethod
    def is_tie( cls ):

        is_tie_game = False

        if( cls.tie_logic( ) ):
            is_tie_game = True
            print( "Tie Game!" )

        return( is_tie_game )

    @classmethod
    def win_logic( cls, symbol ):

        is_win = False

        if( ( symbol == cls.a[0] and symbol == cls.a[1] and symbol == cls.a[2] and symbol == cls.a[3] and symbol == cls.a[4] )
         or ( symbol == cls.b[0] and symbol == cls.b[1] and symbol == cls.b[2] and symbol == cls.b[3] and symbol == cls.b[4] )
         or ( symbol == cls.c[0] and symbol == cls.c[1] and symbol == cls.c[2] and symbol == cls.c[3] and symbol == cls.c[4] )
         or ( symbol == cls.d[0] and symbol == cls.d[1] and symbol == cls.d[2] and symbol == cls.d[3] and symbol == cls.d[4] )
         or ( symbol == cls.e[0] and symbol == cls.e[1] and symbol == cls.e[2] and symbol == cls.e[3] and symbol == cls.e[4] )
         or ( symbol == cls.a[0] and symbol == cls.b[0] and symbol == cls.c[0] and symbol == cls.d[0] and symbol == cls.e[0] )
         or ( symbol == cls.a[1] and symbol == cls.b[1] and symbol == cls.c[1] and symbol == cls.d[1] and symbol == cls.e[1] )
         or ( symbol == cls.a[2] and symbol == cls.b[2] and symbol == cls.c[2] and symbol == cls.d[2] and symbol == cls.e[2] )
         or ( symbol == cls.a[3] and symbol == cls.b[3] and symbol == cls.c[3] and symbol == cls.d[3] and symbol == cls.e[3] )
         or ( symbol == cls.a[4] and symbol == cls.b[4] and symbol == cls.c[4] and symbol == cls.d[4] and symbol == cls.e[4] )
         or ( symbol == cls.a[0] and symbol == cls.b[1] and symbol == cls.c[2] and symbol == cls.d[3] and symbol == cls.e[4] )
         or ( symbol == cls.a[4] and symbol == cls.b[3] and symbol == cls.c[2] and symbol == cls.d[1] and symbol == cls.e[0] ) ):
            is_win = True

        return( is_win )


    # is player x the winner?
    @classmethod
    def is_player_x_win( cls ):

        is_x_win = False

        if( cls.win_logic( "X" ) ):
            print( "Player X Is The Winner!" )
            is_x_win = True
            cls.x_wins_times = cls.x_wins_times + 1
        return( is_x_win )


    # is player y the winner?
    @classmethod
    def is_player_y_win( cls ):

        is_y_win = False

        if( cls.win_logic( "O" ) ):
            print( "Player O Is The Winner!" )
            is_y_win = True
            cls.y_wins_times = cls.y_wins_times + 1
        return( is_y_win )


    # all the logic pertaining to the human
    @classmethod
    def human_play_logic( cls, symbol ):

        choice = ""
        symbol = symbol.upper( )

        while( True ):
            choice = str( input( "{0} - Provide input: ".format( symbol ) ) )
            choice = choice.upper( )

            if( choice != "A1" and choice != "A2" and choice != "A3" and choice != "A4" and choice != "A5"
            and choice != "B1" and choice != "B2" and choice != "B3" and choice != "B4" and choice != "B5"
            and choice != "C1" and choice != "C2" and choice != "C3" and choice != "C4" and choice != "C5"
            and choice != "D1" and choice != "D2" and choice != "D3" and choice != "D4" and choice != "D5"
            and choice != "E1" and choice != "E2" and choice != "E3" and choice != "E4" and choice != "E5" ):
                continue
            else:

                # handling the A row
                if( choice == "A1" and cls.a[0] == " " ):
                    cls.a[0] = symbol
                elif( choice == "A2" and cls.a[1] == " " ):
                    cls.a[1] = symbol
                elif( choice == "A3" and cls.a[2] == " " ):
                    cls.a[2] = symbol
                elif( choice == "A4" and cls.a[3] == " " ):
                    cls.a[3] = symbol
                elif( choice == "A5" and cls.a[4] == " " ):
                    cls.a[4] = symbol

                # handling the B row
                elif( choice == "B1" and cls.b[0] == " " ):
                    cls.b[0] = symbol
                elif( choice == "B2" and cls.b[1] == " " ):
                    cls.b[1] = symbol
                elif( choice == "B3" and cls.b[2] == " " ):
                    cls.b[2] = symbol
                elif( choice == "B4" and cls.b[3] == " " ):
                    cls.b[3] = symbol
                elif( choice == "B5" and cls.b[4] == " " ):
                    cls.b[4] = symbol

                # handling the C row
                elif( choice == "C1" and cls.c[0] == " " ):
                    cls.c[0] = symbol
                elif( choice == "C2" and cls.c[1] == " " ):
                    cls.c[1] = symbol
                elif( choice == "C3" and cls.c[2] == " " ):
                    cls.c[2] = symbol
                elif( choice == "C4" and cls.c[3] == " " ):
                    cls.c[3] = symbol
                elif( choice == "C5" and cls.c[4] == " " ):
                    cls.c[4] = symbol

                # handling the D row
                elif( choice == "D1" and cls.d[0] == " " ):
                    cls.d[0] = symbol
                elif( choice == "D2" and cls.d[1] == " " ):
                    cls.d[1] = symbol
                elif( choice == "D3" and cls.d[2] == " " ):
                    cls.d[2] = symbol
                elif( choice == "D4" and cls.d[3] == " " ):
                    cls.d[3] = symbol
                elif( choice == "D5" and cls.d[4] == " " ):
                    cls.d[4] = symbol

                # handling the E row
                elif( choice == "E1" and cls.e[0] == " " ):
                    cls.e[0] = symbol
                elif( choice == "E2" and cls.e[1] == " " ):
                    cls.e[1] = symbol
                elif( choice == "E3" and cls.e[2] == " " ):
                    cls.e[2] = symbol
                elif( choice == "E4" and cls.e[3] == " " ):
                    cls.e[3] = symbol
                elif( choice == "E5" and cls.e[4] == " " ):
                    cls.e[4] = symbol
                else:
                    continue

                break


    # all the logic pertaining to the computer
    @classmethod
    def computer_play_logic( cls, symbol ):

        # determine what symbol the opponent is
        opponent = ""
        if( symbol == "X" ):
            opponent = "O"
        elif( symbol == "O" ):
            opponent = "X"
        else:
            print( "Error: Not able to decide what symbol the opponent is!" )

        # capture the middle (center)
        if( cls.c[2] == " " ):
            cls.c[2] = symbol

        ##########################
        # 4-filled offensive logic
        # a (rows)
        elif( cls.a[0] == symbol and cls.a[1] == symbol and cls.a[2] == symbol and cls.a[3] == symbol and cls.a[4] == " " ):
            cls.a[4] = symbol
        elif( cls.a[0] == symbol and cls.a[1] == symbol and cls.a[2] == symbol and cls.a[3] == " " and cls.a[4] == symbol ):
            cls.a[3] = symbol
        elif( cls.a[0] == symbol and cls.a[1] == symbol and cls.a[2] == " " and cls.a[3] == symbol and cls.a[4] == symbol ):
            cls.a[2] = symbol
        elif( cls.a[0] == symbol and cls.a[1] == " " and cls.a[2] == symbol and cls.a[3] == symbol and cls.a[4] == symbol ):
            cls.a[1] = symbol
        elif( cls.a[0] == " " and cls.a[1] == symbol and cls.a[2] == symbol and cls.a[3] == symbol and cls.a[4] == symbol ):
            cls.a[0] = symbol

        # b (rows)
        elif( cls.b[0] == symbol and cls.b[1] == symbol and cls.b[2] == symbol and cls.b[3] == symbol and cls.b[4] == " " ):
            cls.b[4] = symbol
        elif( cls.b[0] == symbol and cls.b[1] == symbol and cls.b[2] == symbol and cls.b[3] == " " and cls.b[4] == symbol ):
            cls.b[3] = symbol
        elif( cls.b[0] == symbol and cls.b[1] == symbol and cls.b[2] == " " and cls.b[3] == symbol and cls.b[4] == symbol ):
            cls.b[2] = symbol
        elif( cls.b[0] == symbol and cls.b[1] == " " and cls.b[2] == symbol and cls.b[3] == symbol and cls.b[4] == symbol ):
            cls.b[1] = symbol
        elif( cls.b[0] == " " and cls.b[1] == symbol and cls.b[2] == symbol and cls.b[3] == symbol and cls.b[4] == symbol ):
            cls.b[0] = symbol

        # c (rows)
        elif( cls.c[0] == symbol and cls.c[1] == symbol and cls.c[2] == symbol and cls.c[3] == symbol and cls.c[4] == " " ):
            cls.c[4] = symbol
        elif( cls.c[0] == symbol and cls.c[1] == symbol and cls.c[2] == symbol and cls.c[3] == " " and cls.c[4] == symbol ):
            cls.c[3] = symbol
        elif( cls.c[0] == symbol and cls.c[1] == symbol and cls.c[2] == " " and cls.c[3] == symbol and cls.c[4] == symbol ):
            cls.c[2] = symbol
        elif( cls.c[0] == symbol and cls.c[1] == " " and cls.c[2] == symbol and cls.c[3] == symbol and cls.c[4] == symbol ):
            cls.c[1] = symbol
        elif( cls.c[0] == " " and cls.c[1] == symbol and cls.c[2] == symbol and cls.c[3] == symbol and cls.c[4] == symbol ):
            cls.c[0] = symbol

        # d (rows)
        elif( cls.d[0] == symbol and cls.d[1] == symbol and cls.d[2] == symbol and cls.d[3] == symbol and cls.d[4] == " " ):
            cls.d[4] = symbol
        elif( cls.d[0] == symbol and cls.d[1] == symbol and cls.d[2] == symbol and cls.d[3] == " " and cls.d[4] == symbol ):
            cls.d[3] = symbol
        elif( cls.d[0] == symbol and cls.d[1] == symbol and cls.d[2] == " " and cls.d[3] == symbol and cls.d[4] == symbol ):
            cls.d[2] = symbol
        elif( cls.d[0] == symbol and cls.d[1] == " " and cls.d[2] == symbol and cls.d[3] == symbol and cls.d[4] == symbol ):
            cls.d[1] = symbol
        elif( cls.d[0] == " " and cls.d[1] == symbol and cls.d[2] == symbol and cls.d[3] == symbol and cls.d[4] == symbol ):
            cls.d[0] = symbol

        # e (rows)
        elif( cls.e[0] == symbol and cls.e[1] == symbol and cls.e[2] == symbol and cls.e[3] == symbol and cls.e[4] == " " ):
            cls.e[4] = symbol
        elif( cls.e[0] == symbol and cls.e[1] == symbol and cls.e[2] == symbol and cls.e[3] == " " and cls.e[4] == symbol ):
            cls.e[3] = symbol
        elif( cls.e[0] == symbol and cls.e[1] == symbol and cls.e[2] == " " and cls.e[3] == symbol and cls.e[4] == symbol ):
            cls.e[2] = symbol
        elif( cls.e[0] == symbol and cls.e[1] == " " and cls.e[2] == symbol and cls.e[3] == symbol and cls.e[4] == symbol ):
            cls.e[1] = symbol
        elif( cls.e[0] == " " and cls.e[1] == symbol and cls.e[2] == symbol and cls.e[3] == symbol and cls.e[4] == symbol ):
            cls.e[0] = symbol

        # 1 (columns)
        elif( cls.a[0] == symbol and cls.b[0] == symbol and cls.c[0] == symbol and cls.d[0] == symbol and cls.e[0] == " " ):
            cls.e[0] = symbol
        elif( cls.a[0] == symbol and cls.b[0] == symbol and cls.c[0] == symbol and cls.d[0] == " " and cls.e[0] == symbol ):
            cls.d[0] = symbol
        elif( cls.a[0] == symbol and cls.b[0] == symbol and cls.c[0] == " " and cls.d[0] == symbol and cls.e[0] == symbol ):
            cls.c[0] = symbol
        elif( cls.a[0] == symbol and cls.b[0] == " " and cls.c[0] == symbol and cls.d[0] == symbol and cls.e[0] == symbol ):
            cls.b[0] = symbol
        elif( cls.a[0] == " " and cls.b[0] == symbol and cls.c[0] == symbol and cls.d[0] == symbol and cls.e[0] == symbol ):
            cls.a[0] = symbol

        # 2 (columns)
        elif( cls.a[1] == symbol and cls.b[1] == symbol and cls.c[1] == symbol and cls.d[1] == symbol and cls.e[1] == " " ):
            cls.e[1] = symbol
        elif( cls.a[1] == symbol and cls.b[1] == symbol and cls.c[1] == symbol and cls.d[1] == " " and cls.e[1] == symbol ):
            cls.d[1] = symbol
        elif( cls.a[1] == symbol and cls.b[1] == symbol and cls.c[1] == " " and cls.d[1] == symbol and cls.e[1] == symbol ):
            cls.c[1] = symbol
        elif( cls.a[1] == symbol and cls.b[1] == " " and cls.c[1] == symbol and cls.d[1] == symbol and cls.e[1] == symbol ):
            cls.b[1] = symbol
        elif( cls.a[1] == " " and cls.b[1] == symbol and cls.c[1] == symbol and cls.d[1] == symbol and cls.e[1] == symbol ):
            cls.a[1] = symbol

        # 3 (columns)
        elif( cls.a[2] == symbol and cls.b[2] == symbol and cls.c[2] == symbol and cls.d[2] == symbol and cls.e[2] == " " ):
            cls.e[2] = symbol
        elif( cls.a[2] == symbol and cls.b[2] == symbol and cls.c[2] == symbol and cls.d[2] == " " and cls.e[2] == symbol ):
            cls.d[2] = symbol
        elif( cls.a[2] == symbol and cls.b[2] == symbol and cls.c[2] == " " and cls.d[2] == symbol and cls.e[2] == symbol ):
            cls.c[2] = symbol
        elif( cls.a[2] == symbol and cls.b[2] == " " and cls.c[2] == symbol and cls.d[2] == symbol and cls.e[2] == symbol ):
            cls.b[2] = symbol
        elif( cls.a[2] == " " and cls.b[2] == symbol and cls.c[2] == symbol and cls.d[2] == symbol and cls.e[2] == symbol ):
            cls.a[2] = symbol

        # 4 (columns)
        elif( cls.a[3] == symbol and cls.b[3] == symbol and cls.c[3] == symbol and cls.d[3] == symbol and cls.e[3] == " " ):
            cls.e[3] = symbol
        elif( cls.a[3] == symbol and cls.b[3] == symbol and cls.c[3] == symbol and cls.d[3] == " " and cls.e[3] == symbol ):
            cls.d[3] = symbol
        elif( cls.a[3] == symbol and cls.b[3] == symbol and cls.c[3] == " " and cls.d[3] == symbol and cls.e[3] == symbol ):
            cls.c[3] = symbol
        elif( cls.a[3] == symbol and cls.b[3] == " " and cls.c[3] == symbol and cls.d[3] == symbol and cls.e[3] == symbol ):
            cls.b[3] = symbol
        elif( cls.a[3] == " " and cls.b[3] == symbol and cls.c[3] == symbol and cls.d[3] == symbol and cls.e[3] == symbol ):
            cls.a[3] = symbol

        # 5 (columns)
        elif( cls.a[4] == symbol and cls.b[4] == symbol and cls.c[4] == symbol and cls.d[4] == symbol and cls.e[4] == " " ):
            cls.e[4] = symbol
        elif( cls.a[4] == symbol and cls.b[4] == symbol and cls.c[4] == symbol and cls.d[4] == " " and cls.e[4] == symbol ):
            cls.d[4] = symbol
        elif( cls.a[4] == symbol and cls.b[4] == symbol and cls.c[4] == " " and cls.d[4] == symbol and cls.e[4] == symbol ):
            cls.c[4] = symbol
        elif( cls.a[4] == symbol and cls.b[4] == " " and cls.c[4] == symbol and cls.d[4] == symbol and cls.e[4] == symbol ):
            cls.b[4] = symbol
        elif( cls.a[4] == " " and cls.b[4] == symbol and cls.c[4] == symbol and cls.d[4] == symbol and cls.e[4] == symbol ):
            cls.a[4] = symbol

        # left (diagonal)
        elif( cls.a[0] == symbol and cls.b[1] == symbol and cls.c[2] == symbol and cls.d[3] == symbol and cls.e[4] == " " ):
            cls.e[4] = symbol
        elif( cls.a[0] == symbol and cls.b[1] == symbol and cls.c[2] == symbol and cls.d[3] == " " and cls.e[4] == symbol ):
            cls.d[3] = symbol
        elif( cls.a[0] == symbol and cls.b[1] == symbol and cls.c[2] == " " and cls.d[3] == symbol and cls.e[4] == symbol ):
            cls.c[2] = symbol
        elif( cls.a[0] == symbol and cls.b[1] == " " and cls.c[2] == symbol and cls.d[3] == symbol and cls.e[4] == symbol ):
            cls.b[1] = symbol
        elif( cls.a[0] == " " and cls.b[1] == symbol and cls.c[2] == symbol and cls.d[3] == symbol and cls.e[4] == symbol ):
            cls.a[0] = symbol

        # right (diagonal)
        elif( cls.a[4] == symbol and cls.b[3] == symbol and cls.c[2] == symbol and cls.d[1] == symbol and cls.e[0] == " " ):
            cls.e[0] = symbol
        elif( cls.a[4] == symbol and cls.b[3] == symbol and cls.c[2] == symbol and cls.d[1] == " " and cls.e[0] == symbol ):
            cls.d[1] = symbol
        elif( cls.a[4] == symbol and cls.b[3] == symbol and cls.c[2] == " " and cls.d[1] == symbol and cls.e[0] == symbol ):
            cls.c[2] = symbol
        elif( cls.a[4] == symbol and cls.b[3] == " " and cls.c[2] == symbol and cls.d[1] == symbol and cls.e[0] == symbol ):
            cls.b[3] = symbol
        elif( cls.a[4] == " " and cls.b[3] == symbol and cls.c[2] == symbol and cls.d[1] == symbol and cls.e[0] == symbol ):
            cls.a[4] = symbol

        ##########################
        # 4-filled defensive logic
        # a (rows)
        elif( cls.a[0] == opponent and cls.a[1] == opponent and cls.a[2] == opponent and cls.a[3] == opponent and cls.a[4] == " " ):
            cls.a[4] = symbol
        elif( cls.a[0] == opponent and cls.a[1] == opponent and cls.a[2] == opponent and cls.a[3] == " " and cls.a[4] == opponent ):
            cls.a[3] = symbol
        elif( cls.a[0] == opponent and cls.a[1] == opponent and cls.a[2] == " " and cls.a[3] == opponent and cls.a[4] == opponent ):
            cls.a[2] = symbol
        elif( cls.a[0] == opponent and cls.a[1] == " " and cls.a[2] == opponent and cls.a[3] == opponent and cls.a[4] == opponent ):
            cls.a[1] = symbol
        elif( cls.a[0] == " " and cls.a[1] == opponent and cls.a[2] == opponent and cls.a[3] == opponent and cls.a[4] == opponent ):
            cls.a[0] = symbol

        # b (rows)
        elif( cls.b[0] == opponent and cls.b[1] == opponent and cls.b[2] == opponent and cls.b[3] == opponent and cls.b[4] == " " ):
            cls.b[4] = symbol
        elif( cls.b[0] == opponent and cls.b[1] == opponent and cls.b[2] == opponent and cls.b[3] == " " and cls.b[4] == opponent ):
            cls.b[3] = symbol
        elif( cls.b[0] == opponent and cls.b[1] == opponent and cls.b[2] == " " and cls.b[3] == opponent and cls.b[4] == opponent ):
            cls.b[2] = symbol
        elif( cls.b[0] == opponent and cls.b[1] == " " and cls.b[2] == opponent and cls.b[3] == opponent and cls.b[4] == opponent ):
            cls.b[1] = symbol
        elif( cls.b[0] == " " and cls.b[1] == opponent and cls.b[2] == opponent and cls.b[3] == opponent and cls.b[4] == opponent ):
            cls.b[0] = symbol

        # c (rows)
        elif( cls.c[0] == opponent and cls.c[1] == opponent and cls.c[2] == opponent and cls.c[3] == opponent and cls.c[4] == " " ):
            cls.c[4] = symbol
        elif( cls.c[0] == opponent and cls.c[1] == opponent and cls.c[2] == opponent and cls.c[3] == " " and cls.c[4] == opponent ):
            cls.c[3] = symbol
        elif( cls.c[0] == opponent and cls.c[1] == opponent and cls.c[2] == " " and cls.c[3] == opponent and cls.c[4] == opponent ):
            cls.c[2] = symbol
        elif( cls.c[0] == opponent and cls.c[1] == " " and cls.c[2] == opponent and cls.c[3] == opponent and cls.c[4] == opponent ):
            cls.c[1] = symbol
        elif( cls.c[0] == " " and cls.c[1] == opponent and cls.c[2] == opponent and cls.c[3] == opponent and cls.c[4] == opponent ):
            cls.c[0] = symbol

        # d (rows)
        elif( cls.d[0] == opponent and cls.d[1] == opponent and cls.d[2] == opponent and cls.d[3] == opponent and cls.d[4] == " " ):
            cls.d[4] = symbol
        elif( cls.d[0] == opponent and cls.d[1] == opponent and cls.d[2] == opponent and cls.d[3] == " " and cls.d[4] == opponent ):
            cls.d[3] = symbol
        elif( cls.d[0] == opponent and cls.d[1] == opponent and cls.d[2] == " " and cls.d[3] == opponent and cls.d[4] == opponent ):
            cls.d[2] = symbol
        elif( cls.d[0] == opponent and cls.d[1] == " " and cls.d[2] == opponent and cls.d[3] == opponent and cls.d[4] == opponent ):
            cls.d[1] = symbol
        elif( cls.d[0] == " " and cls.d[1] == opponent and cls.d[2] == opponent and cls.d[3] == opponent and cls.d[4] == opponent ):
            cls.d[0] = symbol

        # e (rows)
        elif( cls.e[0] == opponent and cls.e[1] == opponent and cls.e[2] == opponent and cls.e[3] == opponent and cls.e[4] == " " ):
            cls.e[4] = symbol
        elif( cls.e[0] == opponent and cls.e[1] == opponent and cls.e[2] == opponent and cls.e[3] == " " and cls.e[4] == opponent ):
            cls.e[3] = symbol
        elif( cls.e[0] == opponent and cls.e[1] == opponent and cls.e[2] == " " and cls.e[3] == opponent and cls.e[4] == opponent ):
            cls.e[2] = symbol
        elif( cls.e[0] == opponent and cls.e[1] == " " and cls.e[2] == opponent and cls.e[3] == opponent and cls.e[4] == opponent ):
            cls.e[1] = symbol
        elif( cls.e[0] == " " and cls.e[1] == opponent and cls.e[2] == opponent and cls.e[3] == opponent and cls.e[4] == opponent ):
            cls.e[0] = symbol

        # 1 (columns)
        elif( cls.a[0] == opponent and cls.b[0] == opponent and cls.c[0] == opponent and cls.d[0] == opponent and cls.e[0] == " " ):
            cls.e[0] = symbol
        elif( cls.a[0] == opponent and cls.b[0] == opponent and cls.c[0] == opponent and cls.d[0] == " " and cls.e[0] == opponent ):
            cls.d[0] = symbol
        elif( cls.a[0] == opponent and cls.b[0] == opponent and cls.c[0] == " " and cls.d[0] == opponent and cls.e[0] == opponent ):
            cls.c[0] = symbol
        elif( cls.a[0] == opponent and cls.b[0] == " " and cls.c[0] == opponent and cls.d[0] == opponent and cls.e[0] == opponent ):
            cls.b[0] = symbol
        elif( cls.a[0] == " " and cls.b[0] == opponent and cls.c[0] == opponent and cls.d[0] == opponent and cls.e[0] == opponent ):
            cls.a[0] = symbol

        # 2 (columns)
        elif( cls.a[1] == opponent and cls.b[1] == opponent and cls.c[1] == opponent and cls.d[1] == opponent and cls.e[1] == " " ):
            cls.e[1] = symbol
        elif( cls.a[1] == opponent and cls.b[1] == opponent and cls.c[1] == opponent and cls.d[1] == " " and cls.e[1] == opponent ):
            cls.d[1] = symbol
        elif( cls.a[1] == opponent and cls.b[1] == opponent and cls.c[1] == " " and cls.d[1] == opponent and cls.e[1] == opponent ):
            cls.c[1] = symbol
        elif( cls.a[1] == opponent and cls.b[1] == " " and cls.c[1] == opponent and cls.d[1] == opponent and cls.e[1] == opponent ):
            cls.b[1] = symbol
        elif( cls.a[1] == " " and cls.b[1] == opponent and cls.c[1] == opponent and cls.d[1] == opponent and cls.e[1] == opponent ):
            cls.a[1] = symbol

        # 3 (columns)
        elif( cls.a[2] == opponent and cls.b[2] == opponent and cls.c[2] == opponent and cls.d[2] == opponent and cls.e[2] == " " ):
            cls.e[2] = symbol
        elif( cls.a[2] == opponent and cls.b[2] == opponent and cls.c[2] == opponent and cls.d[2] == " " and cls.e[2] == opponent ):
            cls.d[2] = symbol
        elif( cls.a[2] == opponent and cls.b[2] == opponent and cls.c[2] == " " and cls.d[2] == opponent and cls.e[2] == opponent ):
            cls.c[2] = symbol
        elif( cls.a[2] == opponent and cls.b[2] == " " and cls.c[2] == opponent and cls.d[2] == opponent and cls.e[2] == opponent ):
            cls.b[2] = symbol
        elif( cls.a[2] == " " and cls.b[2] == opponent and cls.c[2] == opponent and cls.d[2] == opponent and cls.e[2] == opponent ):
            cls.a[2] = symbol

        # 4 (columns)
        elif( cls.a[3] == opponent and cls.b[3] == opponent and cls.c[3] == opponent and cls.d[3] == opponent and cls.e[3] == " " ):
            cls.e[3] = symbol
        elif( cls.a[3] == opponent and cls.b[3] == opponent and cls.c[3] == opponent and cls.d[3] == " " and cls.e[3] == opponent ):
            cls.d[3] = symbol
        elif( cls.a[3] == opponent and cls.b[3] == opponent and cls.c[3] == " " and cls.d[3] == opponent and cls.e[3] == opponent ):
            cls.c[3] = symbol
        elif( cls.a[3] == opponent and cls.b[3] == " " and cls.c[3] == opponent and cls.d[3] == opponent and cls.e[3] == opponent ):
            cls.b[3] = symbol
        elif( cls.a[3] == " " and cls.b[3] == opponent and cls.c[3] == opponent and cls.d[3] == opponent and cls.e[3] == opponent ):
            cls.a[3] = symbol

        # 5 (columns)
        elif( cls.a[4] == opponent and cls.b[4] == opponent and cls.c[4] == opponent and cls.d[4] == opponent and cls.e[4] == " " ):
            cls.e[4] = symbol
        elif( cls.a[4] == opponent and cls.b[4] == opponent and cls.c[4] == opponent and cls.d[4] == " " and cls.e[4] == opponent ):
            cls.d[4] = symbol
        elif( cls.a[4] == opponent and cls.b[4] == opponent and cls.c[4] == " " and cls.d[4] == opponent and cls.e[4] == opponent ):
            cls.c[4] = symbol
        elif( cls.a[4] == opponent and cls.b[4] == " " and cls.c[4] == opponent and cls.d[4] == opponent and cls.e[4] == opponent ):
            cls.b[4] = symbol
        elif( cls.a[4] == " " and cls.b[4] == opponent and cls.c[4] == opponent and cls.d[4] == opponent and cls.e[4] == opponent ):
            cls.a[4] = symbol

        # left (diagonal)
        elif( cls.a[0] == opponent and cls.b[1] == opponent and cls.c[2] == opponent and cls.d[3] == opponent and cls.e[4] == " " ):
            cls.e[4] = symbol
        elif( cls.a[0] == opponent and cls.b[1] == opponent and cls.c[2] == opponent and cls.d[3] == " " and cls.e[4] == opponent ):
            cls.d[3] = symbol
        elif( cls.a[0] == opponent and cls.b[1] == opponent and cls.c[2] == " " and cls.d[3] == opponent and cls.e[4] == opponent ):
            cls.c[2] = symbol
        elif( cls.a[0] == opponent and cls.b[1] == " " and cls.c[2] == opponent and cls.d[3] == opponent and cls.e[4] == opponent ):
            cls.b[1] = symbol
        elif( cls.a[0] == " " and cls.b[1] == opponent and cls.c[2] == opponent and cls.d[3] == opponent and cls.e[4] == opponent ):
            cls.a[0] = symbol

        # right (diagonal)
        elif( cls.a[4] == opponent and cls.b[3] == opponent and cls.c[2] == opponent and cls.d[1] == opponent and cls.e[0] == " " ):
            cls.e[0] = symbol
        elif( cls.a[4] == opponent and cls.b[3] == opponent and cls.c[2] == opponent and cls.d[1] == " " and cls.e[0] == opponent ):
            cls.d[1] = symbol
        elif( cls.a[4] == opponent and cls.b[3] == opponent and cls.c[2] == " " and cls.d[1] == opponent and cls.e[0] == opponent ):
            cls.c[2] = symbol
        elif( cls.a[4] == opponent and cls.b[3] == " " and cls.c[2] == opponent and cls.d[1] == opponent and cls.e[0] == opponent ):
            cls.b[3] = symbol
        elif( cls.a[4] == " " and cls.b[3] == opponent and cls.c[2] == opponent and cls.d[1] == opponent and cls.e[0] == opponent ):
            cls.a[4] = symbol

        ##########################
        # 3-filled offensive logic
        # a (rows)
        elif( cls.a[0] == symbol and cls.a[1] == symbol and cls.a[2] == symbol and cls.a[3] == " " and cls.a[4] == " " ):
            cls.a[4] = symbol
        elif( cls.a[0] == symbol and cls.a[1] == symbol and cls.a[2] == " " and cls.a[3] == " " and cls.a[4] == symbol ):
            cls.a[2] = symbol
        elif( cls.a[0] == symbol and cls.a[1] == " " and cls.a[2] == " " and cls.a[3] == symbol and cls.a[4] == symbol ):
            cls.a[2] = symbol
        elif( cls.a[0] == " " and cls.a[1] == " " and cls.a[2] == symbol and cls.a[3] == symbol and cls.a[4] == symbol ):
            cls.a[0] = symbol
        elif( cls.a[0] == " " and cls.a[1] == symbol and cls.a[2] == " " and cls.a[3] == symbol and cls.a[4] == symbol ):
            cls.a[0] = symbol
        elif( cls.a[0] == " " and cls.a[1] == symbol and cls.a[2] == symbol and cls.a[3] == " " and cls.a[4] == symbol ):
            cls.a[0] = symbol
        elif( cls.a[0] == " " and cls.a[1] == symbol and cls.a[2] == symbol and cls.a[3] == symbol and cls.a[4] == " " ):
            cls.a[0] = symbol
        elif( cls.a[0] == symbol and cls.a[1] == " " and cls.a[2] == symbol and cls.a[3] == " " and cls.a[4] == symbol ):
            cls.a[3] = symbol
        elif( cls.a[0] == symbol and cls.a[1] == symbol and cls.a[2] == " " and cls.a[3] == symbol and cls.a[4] == " " ):
            cls.a[4] = symbol
        elif( cls.a[0] == symbol and cls.a[1] == " " and cls.a[2] == symbol and cls.a[3] == symbol and cls.a[4] == " " ):
            cls.a[4] = symbol

        # b (rows)
        elif( cls.b[0] == symbol and cls.b[1] == symbol and cls.b[2] == symbol and cls.b[3] == " " and cls.b[4] == " " ):
            cls.b[4] = symbol
        elif( cls.b[0] == symbol and cls.b[1] == symbol and cls.b[2] == " " and cls.b[3] == " " and cls.b[4] == symbol ):
            cls.b[2] = symbol
        elif( cls.b[0] == symbol and cls.b[1] == " " and cls.b[2] == " " and cls.b[3] == symbol and cls.b[4] == symbol ):
            cls.b[2] = symbol
        elif( cls.b[0] == " " and cls.b[1] == " " and cls.b[2] == symbol and cls.b[3] == symbol and cls.b[4] == symbol ):
            cls.b[0] = symbol
        elif( cls.b[0] == " " and cls.b[1] == symbol and cls.b[2] == " " and cls.b[3] == symbol and cls.b[4] == symbol ):
            cls.b[0] = symbol
        elif( cls.b[0] == " " and cls.b[1] == symbol and cls.b[2] == symbol and cls.b[3] == " " and cls.b[4] == symbol ):
            cls.b[0] = symbol
        elif( cls.b[0] == " " and cls.b[1] == symbol and cls.b[2] == symbol and cls.b[3] == symbol and cls.b[4] == " " ):
            cls.b[0] = symbol
        elif( cls.b[0] == symbol and cls.b[1] == " " and cls.b[2] == symbol and cls.b[3] == " " and cls.b[4] == symbol ):
            cls.b[3] = symbol
        elif( cls.b[0] == symbol and cls.b[1] == symbol and cls.b[2] == " " and cls.b[3] == symbol and cls.b[4] == " " ):
            cls.b[4] = symbol
        elif( cls.b[0] == symbol and cls.b[1] == " " and cls.b[2] == symbol and cls.b[3] == symbol and cls.b[4] == " " ):
            cls.b[4] = symbol

        # c (rows)
        elif( cls.c[0] == symbol and cls.c[1] == symbol and cls.c[2] == symbol and cls.c[3] == " " and cls.c[4] == " " ):
            cls.c[4] = symbol
        elif( cls.c[0] == symbol and cls.c[1] == symbol and cls.c[2] == " " and cls.c[3] == " " and cls.c[4] == symbol ):
            cls.c[2] = symbol
        elif( cls.c[0] == symbol and cls.c[1] == " " and cls.c[2] == " " and cls.c[3] == symbol and cls.c[4] == symbol ):
            cls.c[2] = symbol
        elif( cls.c[0] == " " and cls.c[1] == " " and cls.c[2] == symbol and cls.c[3] == symbol and cls.c[4] == symbol ):
            cls.c[0] = symbol
        elif( cls.c[0] == " " and cls.c[1] == symbol and cls.c[2] == " " and cls.c[3] == symbol and cls.c[4] == symbol ):
            cls.c[0] = symbol
        elif( cls.c[0] == " " and cls.c[1] == symbol and cls.c[2] == symbol and cls.c[3] == " " and cls.c[4] == symbol ):
            cls.c[0] = symbol
        elif( cls.c[0] == " " and cls.c[1] == symbol and cls.c[2] == symbol and cls.c[3] == symbol and cls.c[4] == " " ):
            cls.c[0] = symbol
        elif( cls.c[0] == symbol and cls.c[1] == " " and cls.c[2] == symbol and cls.c[3] == " " and cls.c[4] == symbol ):
            cls.c[3] = symbol
        elif( cls.c[0] == symbol and cls.c[1] == symbol and cls.c[2] == " " and cls.c[3] == symbol and cls.c[4] == " " ):
            cls.c[4] = symbol
        elif( cls.c[0] == symbol and cls.c[1] == " " and cls.c[2] == symbol and cls.c[3] == symbol and cls.c[4] == " " ):
            cls.c[4] = symbol

        # d (rows)
        elif( cls.d[0] == symbol and cls.d[1] == symbol and cls.d[2] == symbol and cls.d[3] == " " and cls.d[4] == " " ):
            cls.d[4] = symbol
        elif( cls.d[0] == symbol and cls.d[1] == symbol and cls.d[2] == " " and cls.d[3] == " " and cls.d[4] == symbol ):
            cls.d[2] = symbol
        elif( cls.d[0] == symbol and cls.d[1] == " " and cls.d[2] == " " and cls.d[3] == symbol and cls.d[4] == symbol ):
            cls.d[2] = symbol
        elif( cls.d[0] == " " and cls.d[1] == " " and cls.d[2] == symbol and cls.d[3] == symbol and cls.d[4] == symbol ):
            cls.d[0] = symbol
        elif( cls.d[0] == " " and cls.d[1] == symbol and cls.d[2] == " " and cls.d[3] == symbol and cls.d[4] == symbol ):
            cls.d[0] = symbol
        elif( cls.d[0] == " " and cls.d[1] == symbol and cls.d[2] == symbol and cls.d[3] == " " and cls.d[4] == symbol ):
            cls.d[0] = symbol
        elif( cls.d[0] == " " and cls.d[1] == symbol and cls.d[2] == symbol and cls.d[3] == symbol and cls.d[4] == " " ):
            cls.d[0] = symbol
        elif( cls.d[0] == symbol and cls.d[1] == " " and cls.d[2] == symbol and cls.d[3] == " " and cls.d[4] == symbol ):
            cls.d[3] = symbol
        elif( cls.d[0] == symbol and cls.d[1] == symbol and cls.d[2] == " " and cls.d[3] == symbol and cls.d[4] == " " ):
            cls.d[4] = symbol
        elif( cls.d[0] == symbol and cls.d[1] == " " and cls.d[2] == symbol and cls.d[3] == symbol and cls.d[4] == " " ):
            cls.d[4] = symbol

        # e (rows)
        elif( cls.e[0] == symbol and cls.e[1] == symbol and cls.e[2] == symbol and cls.e[3] == " " and cls.e[4] == " " ):
            cls.e[4] = symbol
        elif( cls.e[0] == symbol and cls.e[1] == symbol and cls.e[2] == " " and cls.e[3] == " " and cls.e[4] == symbol ):
            cls.e[2] = symbol
        elif( cls.e[0] == symbol and cls.e[1] == " " and cls.e[2] == " " and cls.e[3] == symbol and cls.e[4] == symbol ):
            cls.e[2] = symbol
        elif( cls.e[0] == " " and cls.e[1] == " " and cls.e[2] == symbol and cls.e[3] == symbol and cls.e[4] == symbol ):
            cls.d[0] = symbol
        elif( cls.e[0] == " " and cls.e[1] == symbol and cls.e[2] == " " and cls.e[3] == symbol and cls.e[4] == symbol ):
            cls.e[0] = symbol
        elif( cls.e[0] == " " and cls.e[1] == symbol and cls.e[2] == symbol and cls.e[3] == " " and cls.e[4] == symbol ):
            cls.e[0] = symbol
        elif( cls.e[0] == " " and cls.e[1] == symbol and cls.e[2] == symbol and cls.e[3] == symbol and cls.e[4] == " " ):
            cls.e[0] = symbol
        elif( cls.e[0] == symbol and cls.e[1] == " " and cls.e[2] == symbol and cls.e[3] == " " and cls.e[4] == symbol ):
            cls.e[3] = symbol
        elif( cls.e[0] == symbol and cls.e[1] == symbol and cls.e[2] == " " and cls.e[3] == symbol and cls.e[4] == " " ):
            cls.e[4] = symbol
        elif( cls.e[0] == symbol and cls.e[1] == " " and cls.e[2] == symbol and cls.e[3] == symbol and cls.e[4] == " " ):
            cls.d[4] = symbol

        # 1 (columns)
        elif( cls.a[0] == symbol and cls.b[0] == symbol and cls.c[0] == symbol and cls.d[0] == " " and cls.e[0] == " " ):
            cls.e[0] = symbol
        elif( cls.a[0] == symbol and cls.b[0] == symbol and cls.c[0] == " " and cls.d[0] == " " and cls.e[0] == symbol ):
            cls.c[0] = symbol
        elif( cls.a[0] == symbol and cls.b[0] == " " and cls.c[0] == " " and cls.d[0] == symbol and cls.e[0] == symbol ):
            cls.c[0] = symbol
        elif( cls.a[0] == " " and cls.b[0] == " " and cls.c[0] == symbol and cls.d[0] == symbol and cls.e[0] == symbol ):
            cls.a[0] = symbol
        elif( cls.a[0] == " " and cls.b[0] == symbol and cls.c[0] == " " and cls.d[0] == symbol and cls.e[0] == symbol ):
            cls.a[0] = symbol
        elif( cls.a[0] == " " and cls.b[0] == symbol and cls.c[0] == symbol and cls.d[0] == " " and cls.e[0] == symbol ):
            cls.a[0] = symbol
        elif( cls.a[0] == " " and cls.b[0] == symbol and cls.c[0] == symbol and cls.d[0] == symbol and cls.e[0] == " " ):
            cls.e[0] = symbol
        elif( cls.a[0] == symbol and cls.b[0] == " " and cls.c[0] == symbol and cls.d[0] == " " and cls.e[0] == symbol ):
            cls.b[0] = symbol
        elif( cls.a[0] == symbol and cls.b[0] == symbol and cls.c[0] == " " and cls.d[0] == symbol and cls.e[0] == " " ):
            cls.e[0] = symbol
        elif( cls.a[0] == symbol and cls.b[0] == " " and cls.c[0] == symbol and cls.d[0] == symbol and cls.e[0] == " " ):
            cls.e[0] = symbol

        # 2 (columns)
        elif( cls.a[1] == symbol and cls.b[1] == symbol and cls.c[1] == symbol and cls.d[1] == " " and cls.e[1] == " " ):
            cls.e[1] = symbol
        elif( cls.a[1] == symbol and cls.b[1] == symbol and cls.c[1] == " " and cls.d[1] == " " and cls.e[1] == symbol ):
            cls.c[1] = symbol
        elif( cls.a[1] == symbol and cls.b[1] == " " and cls.c[1] == " " and cls.d[1] == symbol and cls.e[1] == symbol ):
            cls.c[1] = symbol
        elif( cls.a[1] == " " and cls.b[1] == " " and cls.c[1] == symbol and cls.d[1] == symbol and cls.e[1] == symbol ):
            cls.a[1] = symbol
        elif( cls.a[1] == " " and cls.b[1] == symbol and cls.c[1] == " " and cls.d[1] == symbol and cls.e[1] == symbol ):
            cls.a[1] = symbol
        elif( cls.a[1] == " " and cls.b[1] == symbol and cls.c[1] == symbol and cls.d[1] == " " and cls.e[1] == symbol ):
            cls.a[1] = symbol
        elif( cls.a[1] == " " and cls.b[1] == symbol and cls.c[1] == symbol and cls.d[1] == symbol and cls.e[1] == " " ):
            cls.e[1] = symbol
        elif( cls.a[1] == symbol and cls.b[1] == " " and cls.c[1] == symbol and cls.d[1] == " " and cls.e[1] == symbol ):
            cls.b[1] = symbol
        elif( cls.a[1] == symbol and cls.b[1] == symbol and cls.c[1] == " " and cls.d[1] == symbol and cls.e[1] == " " ):
            cls.e[1] = symbol
        elif( cls.a[1] == symbol and cls.b[1] == " " and cls.c[1] == symbol and cls.d[1] == symbol and cls.e[1] == " " ):
            cls.e[1] = symbol

        # 3 (columns)
        elif( cls.a[2] == symbol and cls.b[2] == symbol and cls.c[2] == symbol and cls.d[2] == " " and cls.e[2] == " " ):
            cls.e[2] = symbol
        elif( cls.a[2] == symbol and cls.b[2] == symbol and cls.c[2] == " " and cls.d[2] == " " and cls.e[2] == symbol ):
            cls.c[2] = symbol
        elif( cls.a[2] == symbol and cls.b[2] == " " and cls.c[2] == " " and cls.d[2] == symbol and cls.e[2] == symbol ):
            cls.c[2] = symbol
        elif( cls.a[2] == " " and cls.b[2] == " " and cls.c[2] == symbol and cls.d[2] == symbol and cls.e[2] == symbol ):
            cls.a[2] = symbol
        elif( cls.a[2] == " " and cls.b[2] == symbol and cls.c[2] == " " and cls.d[2] == symbol and cls.e[2] == symbol ):
            cls.a[2] = symbol
        elif( cls.a[2] == " " and cls.b[2] == symbol and cls.c[2] == symbol and cls.d[2] == " " and cls.e[2] == symbol ):
            cls.a[2] = symbol
        elif( cls.a[2] == " " and cls.b[2] == symbol and cls.c[2] == symbol and cls.d[2] == symbol and cls.e[2] == " " ):
            cls.e[2] = symbol
        elif( cls.a[2] == symbol and cls.b[2] == " " and cls.c[2] == symbol and cls.d[2] == " " and cls.e[2] == symbol ):
            cls.b[2] = symbol
        elif( cls.a[2] == symbol and cls.b[2] == symbol and cls.c[2] == " " and cls.d[2] == symbol and cls.e[2] == " " ):
            cls.e[2] = symbol
        elif( cls.a[2] == symbol and cls.b[2] == " " and cls.c[2] == symbol and cls.d[2] == symbol and cls.e[2] == " " ):
            cls.e[2] = symbol

        # 4 (columns)
        elif( cls.a[3] == symbol and cls.b[3] == symbol and cls.c[3] == symbol and cls.d[3] == " " and cls.e[3] == " " ):
            cls.e[3] = symbol
        elif( cls.a[3] == symbol and cls.b[3] == symbol and cls.c[3] == " " and cls.d[3] == " " and cls.e[3] == symbol ):
            cls.c[3] = symbol
        elif( cls.a[3] == symbol and cls.b[3] == " " and cls.c[3] == " " and cls.d[3] == symbol and cls.e[3] == symbol ):
            cls.c[3] = symbol
        elif( cls.a[3] == " " and cls.b[3] == " " and cls.c[3] == symbol and cls.d[3] == symbol and cls.e[3] == symbol ):
            cls.a[3] = symbol
        elif( cls.a[3] == " " and cls.b[3] == symbol and cls.c[3] == " " and cls.d[3] == symbol and cls.e[3] == symbol ):
            cls.a[3] = symbol
        elif( cls.a[3] == " " and cls.b[3] == symbol and cls.c[3] == symbol and cls.d[3] == " " and cls.e[3] == symbol ):
            cls.a[3] = symbol
        elif( cls.a[3] == " " and cls.b[3] == symbol and cls.c[3] == symbol and cls.d[3] == symbol and cls.e[3] == " " ):
            cls.e[3] = symbol
        elif( cls.a[3] == symbol and cls.b[3] == " " and cls.c[3] == symbol and cls.d[3] == " " and cls.e[3] == symbol ):
            cls.b[3] = symbol
        elif( cls.a[3] == symbol and cls.b[3] == symbol and cls.c[3] == " " and cls.d[3] == symbol and cls.e[3] == " " ):
            cls.e[3] = symbol
        elif( cls.a[3] == symbol and cls.b[3] == " " and cls.c[3] == symbol and cls.d[3] == symbol and cls.e[3] == " " ):
            cls.e[3] = symbol

        # 5 (columns)
        elif( cls.a[4] == symbol and cls.b[4] == symbol and cls.c[4] == symbol and cls.d[4] == " " and cls.e[4] == " " ):
            cls.e[4] = symbol
        elif( cls.a[4] == symbol and cls.b[4] == symbol and cls.c[4] == " " and cls.d[4] == " " and cls.e[4] == symbol ):
            cls.c[4] = symbol
        elif( cls.a[4] == symbol and cls.b[4] == " " and cls.c[4] == " " and cls.d[4] == symbol and cls.e[4] == symbol ):
            cls.c[4] = symbol
        elif( cls.a[4] == " " and cls.b[4] == " " and cls.c[4] == symbol and cls.d[4] == symbol and cls.e[4] == symbol ):
            cls.a[4] = symbol
        elif( cls.a[4] == " " and cls.b[4] == symbol and cls.c[4] == " " and cls.d[4] == symbol and cls.e[4] == symbol ):
            cls.a[4] = symbol
        elif( cls.a[4] == " " and cls.b[4] == symbol and cls.c[4] == symbol and cls.d[4] == " " and cls.e[4] == symbol ):
            cls.a[4] = symbol
        elif( cls.a[4] == " " and cls.b[4] == symbol and cls.c[4] == symbol and cls.d[4] == symbol and cls.e[4] == " " ):
            cls.e[4] = symbol
        elif( cls.a[4] == symbol and cls.b[4] == " " and cls.c[4] == symbol and cls.d[4] == " " and cls.e[4] == symbol ):
            cls.b[4] = symbol
        elif( cls.a[4] == symbol and cls.b[4] == symbol and cls.c[4] == " " and cls.d[4] == symbol and cls.e[4] == " " ):
            cls.e[4] = symbol
        elif( cls.a[4] == symbol and cls.b[4] == " " and cls.c[4] == symbol and cls.d[4] == symbol and cls.e[4] == " " ):
            cls.e[4] = symbol

        # left (diagonal)
        elif( cls.e[4] == symbol and cls.d[3] == symbol and cls.c[2] == symbol and cls.b[1] == " " and cls.a[0] == " " ):
            cls.a[0] = symbol
        elif( cls.e[4] == symbol and cls.d[3] == symbol and cls.c[2] == " " and cls.b[1] == " " and cls.a[0] == symbol ):
            cls.b[1] = symbol
        elif( cls.e[4] == symbol and cls.d[3] == " " and cls.c[2] == " " and cls.b[1] == symbol and cls.a[0] == symbol ):
            cls.d[3] = symbol
        elif( cls.e[4] == " " and cls.d[3] == " " and cls.c[2] == symbol and cls.b[1] == symbol and cls.a[0] == symbol ):
            cls.e[4] = symbol
        elif( cls.e[4] == " " and cls.d[3] == symbol and cls.c[2] == " " and cls.b[1] == symbol and cls.a[0] == symbol ):
            cls.e[4] = symbol
        elif( cls.e[4] == " " and cls.d[3] == symbol and cls.c[2] == symbol and cls.b[1] == " " and cls.a[0] == symbol ):
            cls.b[1] = symbol
        elif( cls.e[4] == " " and cls.d[3] == symbol and cls.c[2] == symbol and cls.b[1] == symbol and cls.a[0] == " " ):
            cls.a[0] = symbol
        elif( cls.e[4] == symbol and cls.d[3] == " " and cls.c[2] == symbol and cls.b[1] == " " and cls.a[0] == symbol ):
            cls.d[3] = symbol
        elif( cls.e[4] == symbol and cls.d[3] == symbol and cls.c[2] == " " and cls.b[1] == symbol and cls.a[0] == " " ):
            cls.a[0] = symbol
        elif( cls.e[4] == symbol and cls.d[3] == " " and cls.c[2] == symbol and cls.b[1] == symbol and cls.a[0] == " " ):
            cls.a[0] = symbol

        # right (diagonal)
        elif( cls.e[0] == symbol and cls.d[1] == symbol and cls.c[2] == symbol and cls.b[3] == " " and cls.a[4] == " " ):
            cls.a[4] = symbol
        elif( cls.e[0] == symbol and cls.d[1] == symbol and cls.c[2] == " " and cls.b[3] == " " and cls.a[4] == symbol ):
            cls.b[3] = symbol
        elif( cls.e[0] == symbol and cls.d[1] == " " and cls.c[2] == " " and cls.b[3] == symbol and cls.a[4] == symbol ):
            cls.d[1] = symbol
        elif( cls.e[0] == " " and cls.d[1] == " " and cls.c[2] == symbol and cls.b[3] == symbol and cls.a[4] == symbol ):
            cls.d[1] = symbol
        elif( cls.e[0] == " " and cls.d[1] == symbol and cls.c[2] == " " and cls.b[3] == symbol and cls.a[4] == symbol ):
            cls.e[0] = symbol
        elif( cls.e[0] == " " and cls.d[1] == symbol and cls.c[2] == symbol and cls.b[3] == " " and cls.a[4] == symbol ):
            cls.e[0] = symbol
        elif( cls.e[0] == " " and cls.d[1] == symbol and cls.c[2] == symbol and cls.b[3] == symbol and cls.a[4] == " " ):
            cls.a[4] = symbol
        elif( cls.e[0] == symbol and cls.d[1] == " " and cls.c[2] == symbol and cls.b[3] == " " and cls.a[4] == symbol ):
            cls.b[3] = symbol
        elif( cls.e[0] == symbol and cls.d[1] == symbol and cls.c[2] == " " and cls.b[3] == symbol and cls.a[4] == " " ):
            cls.a[4] = symbol
        elif( cls.e[0] == symbol and cls.d[1] == " " and cls.c[2] == symbol and cls.b[3] == symbol and cls.a[4] == " " ):
            cls.d[1] = symbol

        # capture individual spaces (corners)
        elif( cls.a[0] == " " ):
            cls.a[0] = symbol
        elif( cls.a[4] == " " ):
            cls.a[4] = symbol
        elif( cls.e[4] == " " ):
            cls.e[4] = symbol
        elif( cls.e[0] == " " ):
            cls.e[0] = symbol

        # capture individual spaces (outer center edges (middle tiles))
        elif( cls.a[2] == " " ):
            cls.a[2] = symbol
        elif( cls.c[0] == " " ):
            cls.c[0] = symbol
        elif( cls.c[4] == " " ):
            cls.c[4] = symbol
        elif( cls.e[2] == " " ):
            cls.e[2] = symbol

        # capture individual spaces (inner center edges)
        elif( cls.b[2] == " " ):
            cls.b[2] = symbol
        elif( cls.c[1] == " " ):
            cls.c[1] = symbol
        elif( cls.c[3] == " " ):
            cls.c[3] = symbol
        elif( cls.d[2] == " " ):
            cls.d[2] = symbol

        # capture individual spaces (inner center corners)
        elif( cls.b[1] == " " ):
            cls.b[1] = symbol
        elif( cls.b[3] == " " ):
            cls.b[3] = symbol
        elif( cls.d[1] == " " ):
            cls.d[1] = symbol
        elif( cls.d[3] == " " ):
            cls.d[3] = symbol

        # capture individual spaces (outer center edges)
        elif( cls.a[1] == " " ):
            cls.a[1] = symbol
        elif( cls.a[3] == " " ):
            cls.a[3] = symbol
        elif( cls.e[1] == " " ):
            cls.e[1] = symbol
        elif( cls.e[3] == " " ):
            cls.e[3] = symbol


    # player x turn
    @classmethod
    def player_x_turn( cls ):

        if( cls.x_player == "HUMAN" ):
            cls.human_play_logic( "X" )
        elif( cls.x_player == "COMPUTER" ):
            cls.computer_play_logic( "X" )
        else:
            raise ValueError( "Error: Not able to determine player X's turn!" )

    # player y turn
    @classmethod
    def player_y_turn( cls ):

        if( cls.y_player == "HUMAN" ):
            cls.human_play_logic( "O" )
        elif( cls.y_player == "COMPUTER" ):
            cls.computer_play_logic( "O" )
        else:
            raise ValueError( "Error: Not able to determine player Y's turn!" )

    # randomize the player turns (only meant for game mode # 2)
    @classmethod
    def randomize_player_turn( cls ):

        # randomize a number from 1 and 2
        rand_num = str( ( randint( 1, 2 ) ) )

        if( cls.game_mode == "1" ):
            cls.x_player = "HUMAN"
            cls.y_player = "HUMAN"
        elif( cls.game_mode == "2" ):
            if( rand_num == "1" ):
                cls.x_player = "HUMAN"
                cls.y_player = "COMPUTER"
            elif( rand_num == "2" ):
                cls.x_player = "COMPUTER"
                cls.y_player = "HUMAN"
            else:
                raise ValueError( "Error: Not able to pick between Human or Computer player!" )
        elif( cls.game_mode == "3" ):
            cls.x_player = "COMPUTER"
            cls.y_player = "COMPUTER"

    # display the main menu
    @classmethod
    def main_menu( cls ):

        while( True ):

            choice = ""

            # clear the screen
            cls.clearScreen( )

            # display the main menu
            print( cls.title )
            print( "1) Human VS Human" )
            print( "2) Human VS Computer" )
            print( "3) Computer VS Computer" )
            choice = ( str( input( "Enter a choice: " ) ) )
            if( choice != "1" and choice != "2" and choice != "3" ):
                continue
            else:
                if( choice == "1" ):
                    cls.game_mode = "1"
                elif( choice == "2" ):
                    cls.game_mode = "2"
                elif( choice == "3" ):
                    cls.game_mode = "3"
                else:
                    raise ValueError( "Error: Not able to select game mode!" )
                break


    # reset the game
    @classmethod
    def reset_game( cls ):

        cls.game_mode = ""

        cls.x_player = ""
        cls.y_player = ""

        cls.a = []
        cls.b = []
        cls.c = []
        cls.d = []
        cls.e = []

        cls.a.append( " " )  # 0
        cls.a.append( " " )  # 1
        cls.a.append( " " )  # 2
        cls.a.append( " " )  # 3
        cls.a.append( " " )  # 4
        cls.b.append( " " )  # 0
        cls.b.append( " " )  # 1
        cls.b.append( " " )  # 2
        cls.b.append( " " )  # 3
        cls.b.append( " " )  # 4
        cls.c.append( " " )  # 0
        cls.c.append( " " )  # 1
        cls.c.append( " " )  # 2
        cls.c.append( " " )  # 3
        cls.c.append( " " )  # 4
        cls.d.append( " " )  # 0
        cls.d.append( " " )  # 1
        cls.d.append( " " )  # 2
        cls.d.append( " " )  # 3
        cls.d.append( " " )  # 4
        cls.e.append( " " )  # 0
        cls.e.append( " " )  # 1
        cls.e.append( " " )  # 2
        cls.e.append( " " )  # 3
        cls.e.append( " " )  # 4

    # display the grid
    @classmethod
    def display_grid_5x5( cls ):

        # clear the screen
        cls.clearScreen( )

        # display the title
        print( cls.title )

        # display 5x5 grid
        print( "\n\n" )
        print( "\t        1              2               3               4                5" )
        print( "\n" )
        print( "\t               |               |               |               |               " )
        print( "\t               |               |               |               |               " )
        print( "A\t       {0}       |       {1}       |       {2}       |       {3}       |       {4}     ".format( cls.a[0], cls.a[1], cls.a[2], cls.a[3], cls.a[4] ) )
        print( "\t               |               |               |               |               " )
        print( "\t_______________________________________________________________________________" )
        print( "\t               |               |               |               |               " )
        print( "\t               |               |               |               |               " )
        print( "B\t       {0}       |       {1}       |       {2}       |       {3}       |       {4}     ".format( cls.b[0], cls.b[1], cls.b[2], cls.b[3], cls.b[4] ) )
        print( "\t               |               |               |               |               " )
        print( "\t_______________________________________________________________________________" )
        print( "\t               |               |               |               |               " )
        print( "\t               |               |               |               |               " )
        print( "C\t       {0}       |       {1}       |       {2}       |       {3}       |       {4}     ".format( cls.c[0], cls.c[1], cls.c[2], cls.c[3], cls.c[4] ) )
        print( "\t               |               |               |               |               " )
        print( "\t_______________________________________________________________________________" )
        print( "\t               |               |               |               |               " )
        print( "\t               |               |               |               |               " )
        print( "D\t       {0}       |       {1}       |       {2}       |       {3}       |       {4}     ".format( cls.d[0], cls.d[1], cls.d[2], cls.d[3], cls.d[4] ) )
        print( "\t               |               |               |               |               " )
        print( "\t_______________________________________________________________________________" )
        print( "\t               |               |               |               |               " )
        print( "\t               |               |               |               |               " )
        print( "E\t       {0}       |       {1}       |       {2}       |       {3}       |       {4}     ".format( cls.e[0], cls.e[1], cls.e[2], cls.e[3], cls.e[4] ) )
        print( "\t               |               |               |               |               " )
        print( "\n" )


    @staticmethod
    def is_play_again( ):
        is_play = False
        choice = ""

        while( True ):
            choice = str( input( "Play again? (y/n): " ) )
            choice = choice.upper( )
            if( choice != "Y" and choice != "N" ):
                continue
            else:
                break

        if( choice == "Y" ):
            is_play = True

        return( is_play )


    @classmethod
    def start_game( cls ):

        while( True ):

            cls.reset_game( )
            cls.main_menu( )
            cls.randomize_player_turn( )
            cls.display_grid_5x5( )

            while( True ):
                # player x turn
                cls.player_x_turn( )
                cls.display_grid_5x5( )

                # check if x won
                if( cls.is_player_x_win( ) ):
                    break

                # check if tie
                if( cls.is_tie( ) ):
                    break

                # player y turn
                cls.player_y_turn( )
                cls.display_grid_5x5( )

                # check if y won
                if( cls.is_player_y_win( ) ):
                    break

            if( cls.is_play_again( ) ):
                continue
            else:
                break


def main( ):

    SuperTTT.start_game( )

    return( 0 )


if __name__ == ( "__main__" ):
    exit( main( ) )
