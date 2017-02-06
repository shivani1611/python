#!/usr/bin/env python3

class Student(object):

    def __init__( self, percentage ):
        self.calcStudentGrade( percentage )
        self.displayLetterGrade( )

    def calcStudentGrade( self, percentage ):
        if( percentage >= 90 and percentage <= 100 ):
            lg = 'A'
        elif( percentage >= 80 and percentage <= 89 ):
            lg = 'B'
        elif( percentage >= 70 and percentage <= 79 ):
            lg = 'C'
        elif( percentage >= 60 and percentage <= 69 ):
            lg = 'D'
        elif( percentage >= 0 and percentage <= 59 ):
            lg = 'F'
        else:
            lg = '?'

        self.letterGrade = ( lg )

    def displayLetterGrade( self ):
        print( "Letter Grade: ", self.letterGrade )

student1 = Student( 75 )
