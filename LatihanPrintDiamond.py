# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 12:29:53 2018

@author: Benny Y. Pratama
"""

def printDiamond(side):
    length = side * 2 - 1
    for i in range(length):
        if(i == 0 or i == length - 1):
            print(" * " * (side * 2 - 1))
        elif(i > 0 and i < side):
            print(" * " * abs(i - side) + "   " * (2 * i - 1) + " * " * abs(i - side))
        else:
            print(" * " * (i - side + 2) + "   " * (length - 2 * (i - side + 2)) + " * " * (i - side + 2))

num = 0
while(num < 1):
    num = int(input("Masukkan jumlah sisi yang diinginkan: "))
printDiamond(num)