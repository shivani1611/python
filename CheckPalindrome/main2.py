#!/usr/bin/env python

def main( ):
    while( True ):
        word = raw_input( "Enter a palindrome: " )

        if word[::1] == word[::-1]:
            print "Palindrome found!"
        else:
            print "Palindrome not found!"

main( )
