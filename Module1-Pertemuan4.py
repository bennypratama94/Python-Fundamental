# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:22:47 2018

@author: Benny Y. Pratama
"""

def sortAsc(A):
    for i in range(0, len(A) - 1):
        for j in range(i + 1, len(A)):
            if (A[i] > A[j]):
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    return A

def sortDesc(B):
    for i in range(0, len(B) - 1):
        for j in range(i + 1, len(B)):
            if (B[i] < B[j]):
                temp = B[i]
                B[i] = B[j]
                B[j] = temp
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
    
numList = [40, 100, 1, 5, 25, 10]

a = sortAsc(numList)
print("Hasil sorting secara ascending adalah " + str(a).strip("[]"))
b = sortDesc(numList)
print("Hasil sorting secara descending adalah " + str(b).strip("[]"))
c = minmax(numList)
print("Nilai minimal dan maksimal dari list adalah " + str(c[0]) + " dan " + str(c[1]))