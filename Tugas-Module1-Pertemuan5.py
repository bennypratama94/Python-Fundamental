# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:36:43 2018

@author: Benny Y. Pratama
"""

def printDict(d):
    print("-------------------------------------------")
    print("|        Key         |       Value        |")
    print("-------------------------------------------")
    for i in d:
        if(str(type(d[i])) == "<class 'str'>"):
            print("|" + "{0: ^20}".format(i) + "|" + "{0: ^20}".format(d[i]) + "|")
        elif(str(type(d[i])) == "<class 'int'>"):
            print("|" + "{0: ^20}".format(i) + "|" + "{0: ^20}".format(str(d[i])) + "|")
    print("-------------------------------------------")

mainChoice = 0
mainDict = {}

while (mainChoice == 0):
    while (mainChoice < 1 or mainChoice > 4):
        print("\n\n\n\n\n\n\n\n\n\n")
        print("Main Menu:")
        print("1. Lihat Semua Dictionary")
        print("2. Tambahkan Isi Dictionary")
        print("3. Filtering Isi Dictionary")
        print("4. Keluar")
        mainChoice = int(input("Masukkan pilihan: "))
        
    while (mainChoice != 4):
        if (mainChoice == 1):
            print("\n\n\n\n\n\n\n\n\n\n")
            printDict(mainDict)
            input("Tekan ENTER untuk melanjutkan! . . .")
            mainChoice = 0
            break
        
        elif (mainChoice == 2):
            print("\n\n\n\n\n\n\n\n\n\n")
            printDict(mainDict)
            choice = 0
            newKey = input("Masukkan key dictionary yang baru: ")
            while (choice < 1 or choice > 2):
                choice = int(input("Pilih tipe value [1. String, 2. Integer]: "))
            newValue = input("Masukkan value dictionary yang baru: ")
            if (choice == 1):
                newValue = str('"{0}"'.format(newValue))
                print(newValue)
            else:
                newValue = int(newValue)
            input("Dictionary baru telah ditambahkan. Tekan ENTER untuk melanjutkan! . . .")
            mainDict[newKey] = newValue
            mainChoice = 0
            break
        
        else:
            print("\n\n\n\n\n\n\n\n\n\n")
            printDict(mainDict)
            userFind = input("Masukkan key yang ingin dicari: ")
            result = list(filter(lambda item: userFind.lower() in item.lower(), mainDict))
            if (result == []):
                print("Program tidak menemukan key yang dimaksud.")
            else:
                print("Hasil pencarian adalah sebagai berikut:")
                for i in result:
                    print(i)
            input("Tekan ENTER untuk melanjutkan! . . .")
            mainChoice = 0
            break
        
input("Tekan ENTER untuk menutup program!")            