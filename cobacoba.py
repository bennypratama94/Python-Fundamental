# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 10:17:59 2018

@author: Benny Y. Pratama
"""

def sortAsc(A):
    temp = 0
    counter = 1
    for i in range(0, len(A)):
        for j in range(counter, len(A)):
            if (A[i] > A[j]):
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
        counter += 1
    return A

def sortDesc(B):
    temp = 0
    counter = 1
    for i in range(0, len(B)):
        for j in range(counter, len(B)):
            if (B[i] < B[j]):
                temp = B[i]
                B[i] = B[j]
                B[j] = temp
        counter += 1
    return B

def minmax(C):
    min = C[0]
    max = C[0]
    for i in C:
        if (i < min):
            min = i
        elif (i > max):
            max = i
    return min, max
    
numList = [81, 16, 25, 49, 9, 100, 36, 4, 64]
print(numList)
a = sortAsc(numList)
print(a)
b = sortDesc(numList)
print(b)
print(numList)
print(a)
print(b)