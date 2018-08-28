# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:24:02 2018

@author: Benny Y. Pratama
"""

def mainMenu():
    choice = 0
    print("\n\n\n\n\n\n\n\n\n\n")
    print("Program Seven Segments")
    print("1. Lihat list angka")
    print("2. Print list angka")
    print("3. Keluar")
    while(choice < 1 or choice > 3):
        choice = int(input("Masukkan pilihan anda: "))
    return choice

def menuOne():
    numInput = -1
    print("\n\n\n\n\n\n\n\n\n\n")
    print("Isi list saat ini adalah: " + str(numList))
    while(numInput < 0 or numInput > 9):
        numInput = int(input("Masukkan angka yang diinginkan: "))
    numList.append(numInput)
    input("Angka yang anda masukkan telah disimpan. Tekan ENTER untuk melanjutkan . . .")
    
def menuTwo():
    stringList = []
    print("\n\n\n\n\n\n\n\n\n\n")
    print("Isi list saat ini adalah: " + str(numList))
    print("Isi list yang dicetak dalam bentuk score board adalah seperti berikut:")
    for i in range(3):
        for j in numList:
            if(i == 0):
                stringList.append(sevenSegments(j, "upper"))
            elif(i == 1):
                stringList.append(sevenSegments(j, "middle"))
            elif(i == 2):
                stringList.append(sevenSegments(j, "lower"))
        stringList.append("  ")
        if(i != 2):
            stringList.append("\n")
    print("".join(stringList))
    input("Tekan ENTER untuk melanjutkan . . .")

def sevenSegments(number, part):
    if(part == "upper"):
        if(number == 1 or number == 4):
            return "    "
        else:
            return " __ "
    elif(part == "middle"):
        if(number == 1 or number == 7):
            return "   |"
        elif(number == 0):
            return "|  |"
        elif(number == 2 or number == 3):
            return " __|"
        elif(number == 5 or number == 6):
            return "|__ "
        else:
            return "|__|"
    elif(part == "lower"):
        if(number == 1 or number == 4 or number == 7):
            return "   |"
        elif(number == 2):
            return "|__ "
        elif(number == 3 or number == 5 or number == 9):
            return " __|"
        else:
            return "|__|"

numList = []        
while True:
    mainChoice = mainMenu()
    if(mainChoice == 1):
        menuOne()
    elif(mainChoice == 2):
        menuTwo()
    elif(mainChoice == 3):
        input("Terima kasih. Tekan ENTER untuk menutup program.")
        break