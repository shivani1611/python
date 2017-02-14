#!/usr/bin/env python3

def test_tc1( ):
    num1 = 5
    num2 = 10
    sum = num1 + num2
    assert( sum == 15 )

def test_tc2( ):
    num1 = 10
    num2 = 10
    sum = num1 + num2
    assert( sum == 20 )

def test_tc3( ):
    num1 = 15
    num2 = 10
    sum = num1 + num2
    assert( sum == 25 )

def test_tc4( ):
    num1 = 20
    num2 = 20
    sum = num1 + num2
    assert( sum == 40 )
