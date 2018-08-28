# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:46:24 2018

@author: Benny Y. Pratama
"""

#def fizzBuzzFunc(fb):
#    for i in range(fb):
#        if ((i + 1) % 15 == 0):
#            print("FizzBuzz")
#        elif ((i + 1) % 3 == 0):
#            print("Fizz")
#        elif ((i + 1) % 5 == 0):
#            print("Buzz")
#        else:
#            print(i + 1)
#
#print("Ini adalah program FizzBuzz!")
#userInput = int(input("Masukkan angka: "))
#fizzBuzzFunc(userInput)

#def fibo(a):
#    if (a == 1 or a == 2):
#        return 1
#    else:
#        return fibo(a - 1) + fibo(a - 2)
#    
#print("Program Fibonacci")
#userFibo = int(input("Masukkan angka: "))
#print(fibo(userFibo))

#import math
#def reverseList(listBack):
#    for i in range(1, math.ceil(len(listBack) / 2) + 1):
#        temp = listBack[i - 1]
#        listBack[i - 1] = listBack[-i]
#        listBack[-i] = temp
#    return listBack
#            
#print("Program reverse list")
#newList = [1, 2, 9, 3, 8, 4, 7, 5]
#print("List awal adalah " + str(newList))
#print("Hasil reverse adalah " + str(reverseList(newList)))

import math
def meanFunc(data):
    total = 0
    for i in data:
        total += i
    return total / len(data)

def medianFunc(data):
    for i in range(0, len(data) - 1):
        for j in range(i + 1, len(data)):
            if (data[i] > data[j]):
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    if (len(data) % 2 != 0):
        return data[math.floor(len(data) / 2)]
    else:
        return (data[int((len(data) / 2) - 1)] + data[int(len(data) / 2)]) / 2
    
def modeFunc(data):
    newSet = list(set(data))
    setCount = []
    for i in range(len(newSet)):
        setCount.append(data.count(newSet[i]))
    result = setCount.index(max(setCount))
    return newSet[result]

newList = [1, 2, 3, 2, 5, 2, 7, 2]
print(meanFunc(newList))
print(medianFunc(newList))
print(modeFunc(newList))