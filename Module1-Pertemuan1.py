# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 13:53:15 2018

@author: Benny Y. Pratama
"""

x = 4
y = 3
z = 2
w = ((x + y * z) / (x * y)) ** z
print (w)

#angka = input("Silahkan masukkan angka berapapun: ")
#hasil = int(angka) ** 2
#print("Kuadrat dari " + angka + " = " + str(hasil))

#totalHari = 750
#
#tahun = int(totalHari / 360)
#bulan = int((totalHari % 360) / 30)
#minggu = int(((totalHari % 360) % 30) / 7)
#hari = int(((totalHari % 360) % 30) % 7)
#
#print(str(tahun) + " tahun, "
#      + str(bulan) + " bulan, "
#      + str(minggu) + " minggu, dan "
#      + str(hari) + " hari.")
#
#totalHari = 750
#
#tahun = int(totalHari / 360)
#totalHari = totalHari - tahun * 360
#bulan = int(totalHari / 30)
#totalHari = totalHari - bulan * 30
#minggu = int(totalHari / 7)
#totalHari = totalHari - minggu * 7
#hari = totalHari
#
#print(str(tahun) + " tahun, "
#      + str(bulan) + " bulan, "
#      + str(minggu) + " minggu, dan "
#      + str(hari) + " hari.")

#totalUsia = 49
#andi = 4
#budi = 10
#andi = int((andi / (andi + budi)) * totalUsia)
#budi = int(totalUsia - andi)
#
#print("Usia Andi 2 tahun lagi adalah " + str(andi + 2) + " tahun.")
#print("Usia Budi 2 tahun lagi adalah " + str(budi + 2) + " tahun.")

#totalJarak = 120
#hour = 9
#
#vA = 60
#vB = 40
#jarakA = int((vA / (vA + vB)) * totalJarak)
#tA = (jarakA / vA) * 60
#
#hour = int(hour + (tA / 60))
#minute = int(tA % 60)
#
#print("Mobil A dan mobil B akan bertabrakan pada pukul "
#      + str(hour) + ":"
#      + str(minute) + " WIB.")