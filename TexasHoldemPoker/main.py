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


    @staticmethod
    def is_play_again( ):

        is_play = False

        choice = ''

        while( choice != 'y' and choice != 'n' ): 

            choice = input( "Play again? (y/n): " )
            choice = str( choice ).strip( ).lower( )

            if choice == 'y':
                is_play = True
                break
            elif choice == 'n':
                is_play = False
                break
            else:
                print( "No such option!" )

        return is_play



    @classmethod
    def determine_winner( cls ):

        # check this to determine the players hand value
        human_hand_value = cls.determine_hand( "human" )
        computer_hand_value = cls.determine_hand( "computer" )

        if human_hand_value < computer_hand_value:
            print( "Computer wins with a \'{hand}\'".format( hand = cls.display_winners_hand( computer_hand_value ) ) )
        elif human_hand_value > computer_hand_value:
            print( "Human wins with a \'{hand}\'".format( hand = cls.display_winners_hand( human_hand_value ) ) )
        else:

            # only check this if the hand value is equal
            human_hand_count = cls.determine_hand_count( "human" )
            computer_hand_count = cls.determine_hand_count( "computer" )

            if human_hand_count < computer_hand_count:
                print( "Close but computer wins with a higher \'{hand}\'".format( hand = cls.display_winners_hand( computer_hand_value ) ) )
            elif human_hand_count > computer_hand_count:
                print( "Close but human wins with a higher \'{hand}\'".format( hand = cls.display_winners_hand( human_hand_value ) ) )
            else:
                print( "Draw!" )


    @staticmethod
    def display_winners_hand( count ):

        winners_hand = ( None )

        if count == 10:
            winners_hand = "Royal Flush"
        elif count == 9:
            winners_hand = "Straight Flush"
        elif count == 8:
            winners_hand = "Four Of A Kind"
        elif count == 7:
            winners_hand = "Full House"
        elif count == 6:
            winners_hand = "Flush"
        elif count == 5:
            winners_hand = "Straight"
        elif count == 4:
            winners_hand = "Three Of A Kind"
        elif count == 3:
            winners_hand = "Two Pair"
        elif count == 2:
            winners_hand = "Pair"
        elif count == 1:
            winners_hand = "High Card"

        return winners_hand 


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


    @classmethod
    def _prep_hands( cls, who ):

        temp_deck = None

        who = str( who ).strip( ).lower( )

        if who == "human":
            temp_deck = cls.human_hand + cls.table_hand
        elif who == "computer":
            temp_deck = cls.computer_hand + cls.table_hand
        else:
            raise ValueError( "Error: Not able to determine whose hand to prep!" )

        return temp_deck

    
    @classmethod
    def is_royal_flush( cls, who ):

        is_hand = False

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )
        
        # club
        if all( [ 'AC' in temp_deck, '10C' in temp_deck, 'JC' in temp_deck, 'QC' in temp_deck, 'KC' in temp_deck] ): 
            is_hand = True

        # heart
        elif all( [ 'AH' in temp_deck, '10H' in temp_deck, 'JH' in temp_deck, 'QH' in temp_deck, 'KH' in temp_deck] ): 
            is_hand = True

        # spade
        elif all( [ 'AS' in temp_deck, '10S' in temp_deck, 'JS' in temp_deck, 'QS' in temp_deck, 'KS' in temp_deck] ): 
            is_hand = True

        # diamond
        elif all( [ 'AD' in temp_deck, '10D' in temp_deck, 'JD' in temp_deck, 'QD' in temp_deck, 'KD' in temp_deck] ): 
            is_hand = True

        return is_hand
    
    
    @classmethod
    def is_straight_flush( cls, who ):
    
        is_hand = False

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )

        # search for all possible straights

        # club
        if all( [ '9C' in temp_deck, '10C' in temp_deck, 'JC' in temp_deck, 'QC' in temp_deck, 'KC' in temp_deck] ): 
            is_hand = True
        elif all( [ '8C' in temp_deck, '9C' in temp_deck, '10C' in temp_deck, 'JC' in temp_deck, 'QC' in temp_deck] ): 
            is_hand = True
        elif all( [ '7C' in temp_deck, '8C' in temp_deck, '9C' in temp_deck, '10C' in temp_deck, 'JC' in temp_deck] ): 
            is_hand = True
        elif all( [ '6C' in temp_deck, '7C' in temp_deck, '8C' in temp_deck, '9C' in temp_deck, '10C' in temp_deck] ): 
            is_hand = True
        elif all( [ '5C' in temp_deck, '6C' in temp_deck, '7C' in temp_deck, '8C' in temp_deck, '9C' in temp_deck] ): 
            is_hand = True
        elif all( [ '4C' in temp_deck, '5C' in temp_deck, '6C' in temp_deck, '7C' in temp_deck, '8C' in temp_deck] ): 
            is_hand = True
        elif all( [ '3C' in temp_deck, '4C' in temp_deck, '5C' in temp_deck, '6C' in temp_deck, '7C' in temp_deck] ): 
            is_hand = True
        elif all( [ '2C' in temp_deck, '3C' in temp_deck, '4C' in temp_deck, '5C' in temp_deck, '6C' in temp_deck] ): 
            is_hand = True

        # heart
        elif all( [ '9H' in temp_deck, '10H' in temp_deck, 'JH' in temp_deck, 'QH' in temp_deck, 'KH' in temp_deck] ): 
            is_hand = True
        elif all( [ '8H' in temp_deck, '9H' in temp_deck, '10H' in temp_deck, 'JH' in temp_deck, 'QH' in temp_deck] ): 
            is_hand = True
        elif all( [ '7H' in temp_deck, '8H' in temp_deck, '9H' in temp_deck, '10H' in temp_deck, 'JH' in temp_deck] ): 
            is_hand = True
        elif all( [ '6H' in temp_deck, '7H' in temp_deck, '8H' in temp_deck, '9H' in temp_deck, '10H' in temp_deck] ): 
            is_hand = True
        elif all( [ '5H' in temp_deck, '6H' in temp_deck, '7H' in temp_deck, '8H' in temp_deck, '9H' in temp_deck] ): 
            is_hand = True
        elif all( [ '4H' in temp_deck, '5H' in temp_deck, '6H' in temp_deck, '7H' in temp_deck, '8H' in temp_deck] ): 
            is_hand = True
        elif all( [ '3H' in temp_deck, '4H' in temp_deck, '5H' in temp_deck, '6H' in temp_deck, '7H' in temp_deck] ): 
            is_hand = True
        elif all( [ '2H' in temp_deck, '3H' in temp_deck, '4H' in temp_deck, '5H' in temp_deck, '6H' in temp_deck] ): 
            is_hand = True

        # spade
        elif all( [ '9S' in temp_deck, '10S' in temp_deck, 'JS' in temp_deck, 'QS' in temp_deck, 'KS' in temp_deck] ): 
            is_hand = True
        elif all( [ '8S' in temp_deck, '9S' in temp_deck, '10S' in temp_deck, 'JS' in temp_deck, 'QS' in temp_deck] ): 
            is_hand = True
        elif all( [ '7S' in temp_deck, '8S' in temp_deck, '9S' in temp_deck, '10S' in temp_deck, 'JS' in temp_deck] ): 
            is_hand = True
        elif all( [ '6S' in temp_deck, '7S' in temp_deck, '8S' in temp_deck, '9S' in temp_deck, '10S' in temp_deck] ): 
            is_hand = True
        elif all( [ '5S' in temp_deck, '6S' in temp_deck, '7S' in temp_deck, '8S' in temp_deck, '9S' in temp_deck] ): 
            is_hand = True
        elif all( [ '4S' in temp_deck, '5S' in temp_deck, '6S' in temp_deck, '7S' in temp_deck, '8S' in temp_deck] ): 
            is_hand = True
        elif all( [ '3S' in temp_deck, '4S' in temp_deck, '5S' in temp_deck, '6S' in temp_deck, '7S' in temp_deck] ): 
            is_hand = True
        elif all( [ '2S' in temp_deck, '3S' in temp_deck, '4S' in temp_deck, '5S' in temp_deck, '6S' in temp_deck] ): 
            is_hand = True

        # diamond
        elif all( [ '9D' in temp_deck, '10D' in temp_deck, 'JD' in temp_deck, 'QD' in temp_deck, 'KD' in temp_deck] ): 
            is_hand = True
        elif all( [ '8D' in temp_deck, '9D' in temp_deck, '10D' in temp_deck, 'JD' in temp_deck, 'QD' in temp_deck] ): 
            is_hand = True
        elif all( [ '7D' in temp_deck, '8D' in temp_deck, '9D' in temp_deck, '10D' in temp_deck, 'JD' in temp_deck] ): 
            is_hand = True
        elif all( [ '6D' in temp_deck, '7D' in temp_deck, '8D' in temp_deck, '9D' in temp_deck, '10D' in temp_deck] ): 
            is_hand = True
        elif all( [ '5D' in temp_deck, '6D' in temp_deck, '7D' in temp_deck, '8D' in temp_deck, '9D' in temp_deck] ): 
            is_hand = True
        elif all( [ '4D' in temp_deck, '5D' in temp_deck, '6D' in temp_deck, '7D' in temp_deck, '8D' in temp_deck] ): 
            is_hand = True
        elif all( [ '3D' in temp_deck, '4D' in temp_deck, '5D' in temp_deck, '6D' in temp_deck, '7D' in temp_deck] ): 
            is_hand = True
        elif all( [ '2D' in temp_deck, '3D' in temp_deck, '4D' in temp_deck, '5D' in temp_deck, '6D' in temp_deck] ): 
            is_hand = True

        return is_hand
    
    
    @classmethod
    def is_four_kind( cls, who ):
    
        is_hand = False

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )
    
        # set all the counts to zero
        c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = cj = cq = ck = ca = 0

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )

        # traverse the hand
        for i in temp_deck:

            if i[0] == '2':
                c2 += 1
            elif i[0] == '3':
                c3 += 1
            elif i[0] == '4':
                c4 += 1
            elif i[0] == '5':
                c5 += 1
            elif i[0] == '6':
                c6 += 1
            elif i[0] == '7':
                c7 += 1
            elif i[0] == '8':
                c8 += 1
            elif i[0] == '9':
                c9 += 1
            elif i[0] == '1':
                c10 += 1
            elif i[0] == 'J':
                cj += 1
            elif i[0] == 'Q':
                cq += 1
            elif i[0] == 'K':
                ck += 1
            elif i[0] == 'A':
                ca += 1

        # check to see if the hand can be spotted
        if c2 > 3 or c3 > 3 or c4 > 3 or c5 > 3 or c6 > 3 or c7 > 3 or c8 > 3 or c9 > 3 or c10 > 3 or cj > 3 or cq > 3 or ck > 3 or ca > 3:
            is_hand = True

        return is_hand
    
    
    @classmethod
    def is_full_house( cls, who ):
    
        is_hand = False

        is_pair = False
        is_three_of_a_kind = False

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )
    
        # set all the counts to zero
        c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = cj = cq = ck = ca = 0

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )

        # traverse the hand
        for i in temp_deck:

            if i[0] == '2':
                c2 += 1
            elif i[0] == '3':
                c3 += 1
            elif i[0] == '4':
                c4 += 1
            elif i[0] == '5':
                c5 += 1
            elif i[0] == '6':
                c6 += 1
            elif i[0] == '7':
                c7 += 1
            elif i[0] == '8':
                c8 += 1
            elif i[0] == '9':
                c9 += 1
            elif i[0] == '1':
                c10 += 1
            elif i[0] == 'J':
                cj += 1
            elif i[0] == 'Q':
                cq += 1
            elif i[0] == 'K':
                ck += 1
            elif i[0] == 'A':
                ca += 1

        if any( [ c2 == 3, c3 == 3, c4 == 3, c5 == 3, c6 == 3, c7 == 3, c8 == 3, c9 == 3, c10 == 3, cj == 3, cq == 3, ck == 3 ] ):
            is_three_of_a_kind = True

        if any( [ c2 == 2, c2 == 2, c4 == 2, c5 == 2, c6 == 2, c7 == 2, c8 == 2, c9 == 2, c10 == 2, cj == 2, cq == 2, ck == 2 ] ):
            is_pair = True

        if is_three_of_a_kind and is_pair:
            is_hand = True

        return is_hand
    
    
    @classmethod
    def is_flush( cls, who ):
    
        is_hand = False

        # set all the counts to zero
        c = h = s = d = 0

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )
    
        # traverse the hand
        for i in temp_deck:

            if i[1] == 'C':
                c += 1
            elif i[1] == 'H':
                h += 1
            elif i[1] == 'S':
                s += 1
            elif i[1] == 'D':
                d += 1

        # check to see if the hand can be spotted
        if c > 4 or h > 4 or s > 4 or d > 4:
            is_hand = True

        return is_hand
    
    
    @classmethod
    def is_straight( cls, who ):
    
        is_hand = False

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )
    
        # search for all possible straights
        if all( [ '10' in temp_deck, 'J' in temp_deck, 'Q' in temp_deck, 'K' in temp_deck, 'A' in temp_deck] ): 
            is_hand = True
        elif all( [ '9' in temp_deck, '10' in temp_deck, 'J' in temp_deck, 'Q' in temp_deck, 'K' in temp_deck] ): 
            is_hand = True
        elif all( [ '8' in temp_deck, '9' in temp_deck, '10' in temp_deck, 'J' in temp_deck, 'Q' in temp_deck] ): 
            is_hand = True
        elif all( [ '7' in temp_deck, '8' in temp_deck, '9' in temp_deck, '10' in temp_deck, 'J' in temp_deck] ): 
            is_hand = True
        elif all( [ '6' in temp_deck, '7' in temp_deck, '8' in temp_deck, '9' in temp_deck, '10' in temp_deck] ): 
            is_hand = True
        elif all( [ '5' in temp_deck, '6' in temp_deck, '7' in temp_deck, '8' in temp_deck, '9' in temp_deck] ): 
            is_hand = True
        elif all( [ '4' in temp_deck, '5' in temp_deck, '6' in temp_deck, '7' in temp_deck, '8' in temp_deck] ): 
            is_hand = True
        elif all( [ '3' in temp_deck, '4' in temp_deck, '5' in temp_deck, '6' in temp_deck, '7' in temp_deck] ): 
            is_hand = True
        elif all( [ '2' in temp_deck, '3' in temp_deck, '4' in temp_deck, '5' in temp_deck, '6' in temp_deck] ): 
            is_hand = True

        return is_hand
    
    
    @classmethod
    def is_three_pair( cls, who ):
    
        is_hand = False

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )
    
        # set all the counts to zero
        c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = cj = cq = ck = ca = 0

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )

        # traverse the hand
        for i in temp_deck:

            if i[0] == '2':
                c2 += 1
            elif i[0] == '3':
                c3 += 1
            elif i[0] == '4':
                c4 += 1
            elif i[0] == '5':
                c5 += 1
            elif i[0] == '6':
                c6 += 1
            elif i[0] == '7':
                c7 += 1
            elif i[0] == '8':
                c8 += 1
            elif i[0] == '9':
                c9 += 1
            elif i[0] == '1':
                c10 += 1
            elif i[0] == 'J':
                cj += 1
            elif i[0] == 'Q':
                cq += 1
            elif i[0] == 'K':
                ck += 1
            elif i[0] == 'A':
                ca += 1

        # check to see if the hand can be spotted
        if c2 > 2 or c3 > 2 or c4 > 2 or c5 > 2 or c6 > 2 or c7 > 2 or c8 > 2 or c9 > 2 or c10 > 2 or cj > 2 or cq > 2 or ck > 2 or ca > 2:
            is_hand = True

        return is_hand
    
    
    @classmethod
    def is_two_pair( cls, who ):
    
        is_hand = False

        # set all the counts to zero
        c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = cj = cq = ck = ca = 0

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )

        # traverse the hand
        for i in temp_deck:

            if i[0] == '2':
                c2 += 1
            elif i[0] == '3':
                c3 += 1
            elif i[0] == '4':
                c4 += 1
            elif i[0] == '5':
                c5 += 1
            elif i[0] == '6':
                c6 += 1
            elif i[0] == '7':
                c7 += 1
            elif i[0] == '8':
                c8 += 1
            elif i[0] == '9':
                c9 += 1
            elif i[0] == '1':
                c10 += 1
            elif i[0] == 'J':
                cj += 1
            elif i[0] == 'Q':
                cq += 1
            elif i[0] == 'K':
                ck += 1
            elif i[0] == 'A':
                ca += 1

        # checking for the number of actual pairs spotted
        pair_count = 0
            
        if c2 > 1:
            pair_count += 1
        if c3 > 1:
            pair_count += 1
        if c4 > 1:
            pair_count += 1
        if c5 > 1:
            pair_count += 1
        if c6 > 1:
            pair_count += 1
        if c7 > 1:
            pair_count += 1
        if c8 > 1:
            pair_count += 1
        if c9 > 1:
            pair_count += 1
        if c10 > 1:
            pair_count += 1
        if cj > 1:
            pair_count += 1
        if cq > 1:
            pair_count += 1
        if ck > 1:
            pair_count += 1
        if ca > 1:
            pair_count += 1

        if pair_count > 1:
            is_hand = True

        return is_hand
    

    @classmethod
    def is_pair( cls, who ):
    
        is_hand = False

        # set all the counts to zero
        c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = cj = cq = ck = ca = 0

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )

        # traverse the hand
        for i in temp_deck:

            if i[0] == '2':
                c2 += 1
            elif i[0] == '3':
                c3 += 1
            elif i[0] == '4':
                c4 += 1
            elif i[0] == '5':
                c5 += 1
            elif i[0] == '6':
                c6 += 1
            elif i[0] == '7':
                c7 += 1
            elif i[0] == '8':
                c8 += 1
            elif i[0] == '9':
                c9 += 1
            elif i[0] == '1':
                c10 += 1
            elif i[0] == 'J':
                cj += 1
            elif i[0] == 'Q':
                cq += 1
            elif i[0] == 'K':
                ck += 1
            elif i[0] == 'A':
                ca += 1

        # check to see if the hand can be spotted
        if c2 > 1 or c3 > 1 or c4 > 1 or c5 > 1 or c6 > 1 or c7 > 1 or c8 > 1 or c9 > 1 or c10 > 1 or cj > 1 or cq > 1 or ck > 1 or ca > 1:
            is_hand = True

        return is_hand


    # this function is deprecated
    @classmethod
    def determine_high_card( cls, who ):

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

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )

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
    def determine_hand_count( cls, who ):

        temp_hand_count = 0

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )

        # determine the highest card for the hand
        for i in temp_deck:
            if i[0] == 'A':
                temp_hand_count += 300000000
            elif i[0] == 'K':
                temp_hand_count += 59999999
            elif i[0] == 'Q':
                temp_hand_count += 1199999
            elif i[0] == 'J':
                temp_hand_count += 310000
            elif i[0] == '1':
                temp_hand_count += 76000
            elif i[0] == '9':
                temp_hand_count += 19000
            elif i[0] == '8':
                temp_hand_count += 4600
            elif i[0] == '7':
                temp_hand_count += 1250
            elif i[0] == '6':
                temp_hand_count += 300
            elif i[0] == '5':
                temp_hand_count += 85
            elif i[0] == '4':
                temp_hand_count += 20
            elif i[0] == '3':
                temp_hand_count += 10
            elif i[0] == '2':
                temp_hand_count += 1
            else:
                raise ValueError( "Error: Not able to determine count for the specified hand!" )
        
        return temp_hand_count


    @classmethod
    def determine_hand( cls, who ):

        hand_value = None

        # prep the hands by combining the players hand and the table hand
        temp_deck = cls._prep_hands( who )

        # determine if royal flush
        if cls.is_royal_flush( who ):
            hand_value = 10
        # determine if straight flush
        elif cls.is_straight_flush( who ):
            hand_value = 9
        # determine elif four of a kind
        elif cls.is_four_kind( who ):
            hand_value = 8
        # determine elif full house
        elif cls.is_full_house( who ):
            hand_value = 7
        # determine flush
        elif cls.is_flush( who ):
            hand_value = 6
        # determine straight
        elif cls.is_straight( who ):
            hand_value = 5
        # determine elif three of a kind
        elif cls.is_three_pair( who ):
            hand_value = 4
        # determine elif two pair
        elif cls.is_two_pair( who ):
            hand_value = 3
        # determine elif pair
        elif cls.is_pair( who ):
            hand_value = 2
        else:
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

        # initialize the main deck
        cls.the_deck = []

        # reset the hands
        cls.human_hand = []
        cls.computer_hand = []
        cls.table_hand = []

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

    while( True ): 

        TexasHoldemPoker.initialize_deck( )
        TexasHoldemPoker.shuffle_deck( )

        TexasHoldemPoker.deal_card( "trash" )
        TexasHoldemPoker.deal_card( "computer" )
        TexasHoldemPoker.deal_card( "human" )
        TexasHoldemPoker.deal_card( "computer" )
        TexasHoldemPoker.deal_card( "human" )

        TexasHoldemPoker.deal_card( "trash" )
        TexasHoldemPoker.deal_card( "table" )
        TexasHoldemPoker.deal_card( "table" )
        TexasHoldemPoker.deal_card( "table" )

        TexasHoldemPoker.deal_card( "trash" )
        TexasHoldemPoker.deal_card( "table" )

        TexasHoldemPoker.deal_card( "trash" )
        TexasHoldemPoker.deal_card( "table" )

        TexasHoldemPoker.display_human_hand( )
        TexasHoldemPoker.display_computer_hand( )
        TexasHoldemPoker.display_table_hand( )

        TexasHoldemPoker.determine_winner( )

        if not TexasHoldemPoker.is_play_again( ):
            break
        print( )

if __name__ == "__main__":
   exit( main( ) )
