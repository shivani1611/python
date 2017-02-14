#!/usr/bin/env python3

from sys import exit

def calcLetterGrade( percentage ):

    letter_grade = ' '

    if( percentage >= 90 and percentage <= 100 ):
        letter_grade = 'A'
    elif( percentage >= 80 and percentage <= 89 ):
        letter_grade = 'B'
    elif( percentage >= 70 and percentage <= 79 ):
        letter_grade = 'C'
    elif( percentage >= 60 and percentage <= 69 ):
        letter_grade = 'D'
    elif( percentage >= 0 and percentage <= 59 ):
        letter_grade = 'F'
    else:
        letter_grade = '?'

    return letter_grade

def main( ):
    print( "Your grade: ", calcLetterGrade( 85 ) )

if __name__ == "__main__":
    exit( main( ) )
