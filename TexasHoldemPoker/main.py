#!/usr/bin/env python3

from random import randint
from sys import exit

class TexasHoldemPoker(object):
    
    # entire deck
    the_deck = []

    # hands
    human_hand = []
    computer_hand = []
    table_hand = []

    # money
    PAY_PER_HAND = 5.00
    the_balance = 500.00

    @classmethod
    def display_deck( cls ):
        for i in cls.the_deck:
            print( "All Cards: ", i )


    @classmethod
    def display_human_hand( cls ):
        print( "Human Hand:\t", end = ' ' )
        for i in cls.human_hand:
            print( i , end = ' ')
        print( )


    @classmethod
    def display_computer_hand( cls ):
        print( "Computer Hand:\t", end = ' ' )
        for i in cls.computer_hand:
            print( i , end = ' ')
        print( )


    @classmethod
    def display_table_hand( cls ):
        print( "Table Hand:\t", end = ' ' )
        for i in cls.table_hand:
            print( i , end = ' ')
        print( )


    def _prep_hands( cls, who ):

        temp_deck = None

        who = str( who ).strip( ).lower( )

        if who == "human":
            cls.human_hand.extend( cls.table_hand )
            temp_deck = cls.human_hand
        elif who == "computer":
            cls.computer_hand.extend( cls.table_hand )
            temp_deck = cls.computer_hand
        else:
            raise ValueError( "Error: Not able to determine whose hand to prep" )

        return temp_deck


    @classmethod
    def determine_high_card( cls, who )

        isAce = False
        isKing = False
        isQueen = False
        isJack = False
        isTen = False
        isNine = False
        isEight = False
        isSeven = False
        isSix = False
        isFive = False
        isFour = False
        isThree = False
        isTwo = False

        temp_high_card = None

        # determine high card for specified player
        temp_deck = _prep_hands( who )

        # determine the highest card for the hand
        for i in temp_deck:
            if i[0] == 'A':
                isAce = True
            elif i[0] == 'K':
                isKing = True
            elif i[0] == 'Q':
                isQueen = True
            elif i[0] == 'J':
                isJack = True
            elif i[0] == '1':
                isTen = True
            elif i[0] == '9':
                isNine = True
            elif i[0] == '8':
                isEight = True
            elif i[0] == '7':
                isSeven = True
            elif i[0] == '6':
                isSix = True
            elif i[0] == '5':
                isFive = True
            elif i[0] == '4':
                isFour = True
            elif i[0] == '3':
                isThree = True
            elif i[0] == '2':
                isTwo = True
            else:
                raise ValueError( "Error: Not able to determine highest card" )
        
        if isAce:
            temp_high_card = 14
        elif isKing:
            temp_high_card = 13
        elif isQueen:
            temp_high_card = 12
        elif isJack:
            temp_high_card = 11
        elif isTen:
            temp_high_card = 10
        elif isNine:
            temp_high_card = 9
        elif isEight:
            temp_high_card = 8
        elif isSeven:
            temp_high_card = 7
        elif isSix:
            temp_high_card = 6
        elif isFive:
            temp_high_card = 5
        elif isFour:
            temp_high_card = 4
        elif isThree:
            temp_high_card = 3
        elif isTwo:
            temp_high_card = 2
        else:
            raise ValueError( "Error: Not able to determine highest card" )

        return temp_high_card


    @classmethod
    def determine_hand( cls, who ):

        hand_value = None

        # determine whose hand to evaluate
        temp_deck = _prep_hands( who )

        # determine if royal flush
        hand_value = 10

        # determine if straight flush
        hand_value = 9

        # determine if four of a kind
        hand_value = 8

        # determine if full house
        hand_value = 7

        # determine flush
        hand_value = 6

        # determine straight
        hand_value = 5

        # determine if three of a kind
        hand_value = 4

        # determine if two pair
        hand_value = 3

        # determine if pair
        hand_value = 2

        # determine highest card
        hand_value = 1

        return hand_value


    @classmethod
    def deal_card( cls, who ):

        who = str( who ).strip( ).lower( )

        if who == "human":
            cls.human_hand.append( cls.the_deck.pop( ) )
        elif who == "computer":
            cls.computer_hand.append( cls.the_deck.pop( ) )
        elif who == "table":
            cls.table_hand.append( cls.the_deck.pop( ) )
        elif who == "trash":
            cls.the_deck.pop( )
        else:
            raise ValueError( "Error: Not able to determine who to deal cards to!" )


    @classmethod
    def shuffle_deck( cls ):

        elements_used = []
        temp_deck = []

        while True:
            rand_num = randint( 0, 51 )

            if rand_num not in elements_used:
                elements_used.append( rand_num )
                temp_deck.append( cls.the_deck[rand_num] )

                if len( temp_deck ) == len( cls.the_deck ):
                    break

        cls.the_deck = temp_deck


    @classmethod
    def initialize_deck( cls ):

        the_deck = []

        # Ace
        cls.the_deck.append( "AC" )
        cls.the_deck.append( "AH" )
        cls.the_deck.append( "AS" )
        cls.the_deck.append( "AD" )

        # Two
        cls.the_deck.append( "2C" )
        cls.the_deck.append( "2H" )
        cls.the_deck.append( "2S" )
        cls.the_deck.append( "2D" )

        # Three
        cls.the_deck.append( "3C" )
        cls.the_deck.append( "3H" )
        cls.the_deck.append( "3S" )
        cls.the_deck.append( "3D" )

        # Four
        cls.the_deck.append( "4C" )
        cls.the_deck.append( "4H" )
        cls.the_deck.append( "4S" )
        cls.the_deck.append( "4D" )

        # Five
        cls.the_deck.append( "5C" )
        cls.the_deck.append( "5H" )
        cls.the_deck.append( "5S" )
        cls.the_deck.append( "5D" )

        # Six
        cls.the_deck.append( "6C" )
        cls.the_deck.append( "6H" )
        cls.the_deck.append( "6S" )
        cls.the_deck.append( "6D" )

        # Seven
        cls.the_deck.append( "7C" )
        cls.the_deck.append( "7H" )
        cls.the_deck.append( "7S" )
        cls.the_deck.append( "7D" )

        # Eight
        cls.the_deck.append( "8C" )
        cls.the_deck.append( "8H" )
        cls.the_deck.append( "8S" )
        cls.the_deck.append( "8D" )

        # Nine
        cls.the_deck.append( "9C" )
        cls.the_deck.append( "9H" )
        cls.the_deck.append( "9S" )
        cls.the_deck.append( "9D" )

        # Ten
        cls.the_deck.append( "10C" )
        cls.the_deck.append( "10H" )
        cls.the_deck.append( "10S" )
        cls.the_deck.append( "10D" )

        # Jack
        cls.the_deck.append( "JC" )
        cls.the_deck.append( "JH" )
        cls.the_deck.append( "JS" )
        cls.the_deck.append( "JD" )

        # Queen
        cls.the_deck.append( "QC" )
        cls.the_deck.append( "QH" )
        cls.the_deck.append( "QS" )
        cls.the_deck.append( "QD" )

        # King
        cls.the_deck.append( "KC" )
        cls.the_deck.append( "KH" )
        cls.the_deck.append( "KS" )
        cls.the_deck.append( "KD" )

def main( ):

    thp = TexasHoldemPoker( )

    thp.initialize_deck( )
    thp.shuffle_deck( )

    thp.deal_card( "computer" )
    thp.deal_card( "human" )

    thp.deal_card( "computer" )
    thp.deal_card( "human" )

    thp.deal_card( "table" )
    thp.deal_card( "table" )
    thp.deal_card( "table" )
    thp.deal_card( "table" )
    thp.deal_card( "table" )

    # check this to determine the players hand
    human_hand_value = thp.determine_hand( "human" )
    computer_hand_value = thp.determine_hand( "computer" )

    # only check this if the hand value is equal
    human_highest_card = thp.determine_high_card( "human" )
    computer_highest_card = thp.determine_high_card( "computer" )
    

if __name__ == "__main__":
    exit( main( ) )
