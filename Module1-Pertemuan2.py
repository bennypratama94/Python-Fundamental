# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:34:04 2018

@author: Benny Y. Pratama
"""

#angka =  int(input("Masukkan angka: "))
#if(angka % 2 == 1):
#    print("Angka " + str(angka)
#    + " tergolong bilangan GANJIL!")
#else:
#    print("Angka " + str(angka)
#    + " tergolong bilangan GENAP!")

massa = input("Masukkan Massa(kg): ")
tinggi = input("Masukkan Tinggi(cm): ")

imt = float(massa) / ((float(tinggi) / 100) ** 2)

print("Massa " + massa
      + " kg & tinggi " + str(float(tinggi)/100) + " m.")

if(imt < 18.5):
    print("IMT = " + str(imt)
    + ", BERAT BADAN KURANG!")
elif(imt >= 18.5 and imt <= 24.9):
    print("IMT = " + str(imt)
    + ", BERAT BADAN IDEAL!")
elif(imt >= 25.0 and imt <= 29.9):
    print("IMT = " + str(imt)
    + ", BERAT BADAN BERLEBIH!")
elif(imt >= 30.0 and imt <= 39.9):
    print("IMT = " + str(imt)
    + ", BERAT BADAN SANGAT BERLEBIH!")
else:
    print("IMT = " + str(imt)
    + ", OBESITAS!")