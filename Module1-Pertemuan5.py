# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 13:35:34 2018

@author: Benny Y. Pratama
"""

#d = {"key1" : "item1",
#     "key2" : "item2",
#     "kucing" : [3, "jerapah"]}
#
#print(d["key1"])
#print(d["kucing"])
#print(d["kucing"][1])
#
#s = {1, 3, 1, 2, 2, 3}
#print(s)
#print(list(s)[2])
#
#newList = [1, 3, "test1",
#           "test2", 2, 3, "test1"]
#s = set(newList)
#
#print(s)
#print(list(s)[2])

#listNum = [1, 2, 3, 4, 5]
#listNum = [item * 2 for item in listNum]
#print(listNum)

#numList = [1, 2, 3]
#input = "x"
#
#check1 = input in numList
#check2 = "x" in ["x", "y", "z"]
#check3 = "ka" in "kurakas"
#
#print(check1)
#print(check2)
#print(check3)

wordList = ["Merdeka", "Hello", "Hellos", "Sohib", "Kari Ayam"]
print(wordList)
user = input("Search: ")

#def checking(keyword, checkList):
#    newList = list(filter(lambda item: keyword.lower()in item.lower(), checkList))
#    return newList

result = list(filter(lambda item: user.lower() in item.lower(), wordList))
print(result)