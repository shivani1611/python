#!/usr/bin/env python3

from random import randint
from sys import exit

class TexasHoldemPoker(object):
    
    my_deck = []

    @staticmethod
    def generate_random_number( ):

        rand_num = randint( 1, 52 )

        return rand_num


    @classmethod
    def shuffle_deck( cls ):

        elements_used = []
        temp_deck = []

        while True:
            rand_num = randint( 0, 51 )

            if rand_num not in elements_used:
                print (rand_num )
                elements_used.append( rand_num )
                temp_deck.append( cls.my_deck[rand_num] )

                if len( temp_deck ) == len( cls.my_deck ):
                    break

        cls.my_deck = temp_deck


    @classmethod
    def display_deck( cls ):
        for i in cls.my_deck:
            print( "Card: ", i )


    @classmethod
    def initialize_deck( cls ):

        my_deck = []

        # Ace
        cls.my_deck.append( "AC" )
        cls.my_deck.append( "AH" )
        cls.my_deck.append( "AS" )
        cls.my_deck.append( "AD" )

        # Two
        cls.my_deck.append( "2C" )
        cls.my_deck.append( "2H" )
        cls.my_deck.append( "2S" )
        cls.my_deck.append( "2D" )

        # Three
        cls.my_deck.append( "3C" )
        cls.my_deck.append( "3H" )
        cls.my_deck.append( "3S" )
        cls.my_deck.append( "3D" )

        # Four
        cls.my_deck.append( "4C" )
        cls.my_deck.append( "4H" )
        cls.my_deck.append( "4S" )
        cls.my_deck.append( "4D" )

        # Five
        cls.my_deck.append( "5C" )
        cls.my_deck.append( "5H" )
        cls.my_deck.append( "5S" )
        cls.my_deck.append( "5D" )

        # Six
        cls.my_deck.append( "6C" )
        cls.my_deck.append( "6H" )
        cls.my_deck.append( "6S" )
        cls.my_deck.append( "6D" )

        # Seven
        cls.my_deck.append( "7C" )
        cls.my_deck.append( "7H" )
        cls.my_deck.append( "7S" )
        cls.my_deck.append( "7D" )

        # Eight
        cls.my_deck.append( "8C" )
        cls.my_deck.append( "8H" )
        cls.my_deck.append( "8S" )
        cls.my_deck.append( "8D" )

        # Nine
        cls.my_deck.append( "9C" )
        cls.my_deck.append( "9H" )
        cls.my_deck.append( "9S" )
        cls.my_deck.append( "9D" )

        # Ten
        cls.my_deck.append( "10C" )
        cls.my_deck.append( "10H" )
        cls.my_deck.append( "10S" )
        cls.my_deck.append( "10D" )

        # Jack
        cls.my_deck.append( "JC" )
        cls.my_deck.append( "JH" )
        cls.my_deck.append( "JS" )
        cls.my_deck.append( "JD" )

        # Queen
        cls.my_deck.append( "QC" )
        cls.my_deck.append( "QH" )
        cls.my_deck.append( "QS" )
        cls.my_deck.append( "QD" )

        # King
        cls.my_deck.append( "KC" )
        cls.my_deck.append( "KH" )
        cls.my_deck.append( "KS" )
        cls.my_deck.append( "KD" )

def main( ):

    thp = TexasHoldemPoker( )

    thp.initialize_deck( )
    thp.shuffle_deck( )
    thp.display_deck( )

if __name__ == "__main__":
    exit( main( ) )
