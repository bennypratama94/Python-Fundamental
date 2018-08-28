# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 09:23:04 2018

@author: Benny Y. Pratama
"""

mainChoice = 0
totalPrice = 0
cart = []
dishes1 = ["Paket Hoki Aja: Rp20.000,-", 20000]
dishes2 = ["Paket Hoki Banget: Rp35.000,-", 35000]
dishes3 = ["Paket Hoki Ciamik: Rp55.000,-", 55000]

while (mainChoice == 0):
    while (mainChoice < 1 or mainChoice > 4):
        print("\n\n\n\n\n\n\n\n\n\n")
        print("Selamat Datang di Hoki Hoki Bento!\n")
        print("Main Menu:")
        print("1. Lihat Menu")
        print("2. Lihat Cart")
        print("3. Checkout")
        print("4. Keluar")
        mainChoice = int(input("Masukkan pilihan: "))
    
    while (mainChoice != 4):
        if (mainChoice == 1):
            menu1choice = 0
            while (menu1choice < 1 or menu1choice > 3):
                print("\n\n\n\n\n\n\n\n\n\n")
                print("Menu Andalan Hoki Hoki Bento!\n")
                print("1. " + str(dishes1[0]))
                print("2. " + str(dishes2[0]))
                print("3. " + str(dishes3[0]))
                menu1choice = int(input("Masukkan pesanan anda!: "))
            print("Pesanan anda diterima!")
            if (menu1choice == 1):
                totalPrice += int(dishes1[1])
                cart.append(dishes1[0])
            elif (menu1choice == 2):
                totalPrice += int(dishes2[1])
                cart.append(dishes2[0])
            else:
                totalPrice += int(dishes3[1])
                cart.append(dishes3[0])
            input("Tekan ENTER untuk melanjutkan! . . .")
            mainChoice = 0
            break
        
        elif (mainChoice == 2):
            print("\n\n\n\n\n\n\n\n\n\n")
            print("Isi cart anda: ")
            for i in cart:
                print(i)
            input("Tekan ENTER untuk melanjutkan! . . .")
            mainChoice = 0
            break
        
        else:
            payment = 0
            print("\n\n\n\n\n\n\n\n\n\n")
            print("Isi cart anda: ")
            for i in cart:
                print(i)
            while (payment < totalPrice):
                print("Total harga pesanan anda adalah Rp" + str(totalPrice) + ",-")
                payment = int(input("Masukkan jumlah pembayaran anda: "))
                if (payment < totalPrice):
                    print("\nJumlah pembayaran anda tidak mencukupi total harga pesanan anda.")
            print("Pembayaran diterima! Total uang kembalian anda adalah Rp"
                  + str(payment - totalPrice) + ",-")
            input("Terima kasih atas pembelian anda. Tekan ENTER untuk melanjutkan! . . . ")
            mainChoice = 0
            totalPrice = 0
            cart = []
            break
    
print("Terima kasih telah mengunjungi Hoki Hoki Bento!")
input("Tekan ENTER untuk menutup program!")