# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 13:55:29 2018

@author: Benny Y. Pratama
"""

list4x4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14 ,15, 16]]

def menuOne():
    again = 0
    global list4x4
    while(again != 2):
        again = 0
        direct = 0
        numSpin = -1
        while(numSpin < 0):
            numSpin = int(input("Berapa kali anda ingin memutar kotaknya? "))
        while(direct < 1 or direct > 2):
            direct = int(input("Kearah mana anda ingin memutar kotaknya? [1. Kiri, 2. Kanan]: "))
        list4x4 = spinTheBox(numSpin, direct)
        print("Hasil spin anda adalah:")
        showTheBox()
        while(again < 1 or again > 2):
            again = int(input("Apakah anda ingin memutar kotaknya lagi? [1. Ya, 2. Tidak]: "))
    input("Terima kasih. Tekan ENTER untuk melanjutkan . . .")
    
def menuTwo():
    again = 0
    global list4x4
    while(again != 2):
        again = 0
        sort = 0
        rc = 0
        position = 0
        while(rc < 1 or rc > 2):
            rc = int(input("Elemen apa yang ingin anda urutkan? [1. Baris, 2. Kolom]: "))
        while(position < 1 or position > 4):
            position = int(input("Baris/kolom keberapa yang ingin anda urutkan? [1-4]: "))
        while(sort < 1 or sort > 2):
            sort = int(input("Bagaimana anda ingin mengurutkannya? [1. Ascending, 2. Descending]: "))
        sortTheBox(rc, position, sort)
        print("Hasil sort anda adalah:")
        showTheBox()
        while(again < 1 or again > 2):
            again = int(input("Apakah anda ingin mengurutkan kotaknya lagi? [1. Ya, 2. Tidak]: "))
    input("Terima kasih. Tekan ENTER untuk melanjutkan . . .")

def spinTheBox(number, direction):
    listSpin = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    if((number % 4 == 1 and direction == 2) or
       (number % 4 == 3 and direction == 1)):
        for i in range(4):
            for j in range(4):
                listSpin[i][j] = list4x4[-(j+1)][i]
    elif(number % 4 == 2):
        for i in range(4):
            for j in range(4):
                listSpin[i][j] = list4x4[-(i+1)][-(j+1)]
    elif((number % 4 == 1 and direction == 1) or
       (number % 4 == 3 and direction == 2)):
        for i in range(4):
            for j in range(4):
                listSpin[i][j] = list4x4[j][-(i+1)]
    elif(number % 4 == 0):
        listSpin = list4x4
    return listSpin

def sortTheBox(rowcolumn, post, sort):
    global list4x4
    num = 1
    if(sort == 1):
        if(rowcolumn == 1):
            for i in range(3):
                for j in range(num, 4):
                    if(list4x4[post-1][i] > list4x4[post-1][j]):
                        temp = list4x4[post-1][i]
                        list4x4[post-1][i] = list4x4[post-1][j]
                        list4x4[post-1][j] = temp
                num += 1
        elif(rowcolumn == 2):
            for i in range(3):
                for j in range(num, 4):
                    if(list4x4[i][post-1] > list4x4[j][post-1]):
                        temp = list4x4[i][post-1]
                        list4x4[i][post-1] = list4x4[j][post-1]
                        list4x4[j][post-1] = temp
                num += 1
    elif(sort == 2):
        if(rowcolumn == 1):
            for i in range(3):
                for j in range(num, 4):
                    if(list4x4[post-1][i] < list4x4[post-1][j]):
                        temp = list4x4[post-1][i]
                        list4x4[post-1][i] = list4x4[post-1][j]
                        list4x4[post-1][j] = temp
                num += 1
        elif(rowcolumn == 2):
            for i in range(3):
                for j in range(num, 4):
                    if(list4x4[i][post-1] < list4x4[j][post-1]):
                        temp = list4x4[i][post-1]
                        list4x4[i][post-1] = list4x4[j][post-1]
                        list4x4[j][post-1] = temp
                num += 1

def showTheBox():
    for i in list4x4:
        print(i)
        
def mainMenu():
    choice = 0
    print("\n\n\n\n\n\n\n\n\n\n")
    print("Program Spin and Sort the Box!\n")
    showTheBox()
    print("\n1. Spin the box")
    print("2. Sort the box")
    print("3. Keluar")
    while(choice < 1 or choice > 3):
        choice = int(input("Masukkan pilihan anda: "))
    return choice
    
while True:
    mainChoice = mainMenu()
    if(mainChoice == 1):
        print("\n\n\n\n\n\n\n\n\n\n")
        menuOne()
    elif(mainChoice == 2):
        print("\n\n\n\n\n\n\n\n\n\n")
        menuTwo()
    elif(mainChoice == 3):
        input("Terima kasih. Tekan ENTER untuk menutup program.")
        break