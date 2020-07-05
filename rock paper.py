# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 21:05:04 2020

@author: Mueen
"""
r = 'rock'
p = 'paper'
s = 'scissors' 
while True:
    from random import choice
    player = [r,p,s]
    mew = choice(player) 
    i = input("what do you choose:")
    if (mew == r and i == s ) or (mew == p and i == r ) or (mew == s and i == p):
        print("I choose {}".format(mew))
        print("I win ")  
    elif (mew ==r and i == p ) or (mew == p and i == s ) or (mew == s  and i == r ):
            print("I choose {}".format(mew))
            print("You win ")
    elif(mew ==r and i == r ) or (mew == p and i == p ) or (mew == s  and i == s ):
                    print("I choose {}".format(mew))
                    print("It is a tie")

 