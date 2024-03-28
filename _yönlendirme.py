from _cokgen import cokgenKenar
from _icaci import icaciToplam


def yonlendirme():
    while True:
        giris = input("Lütfen belirtilen rakamlardan birini giriniz: ")
        if giris.isdigit():
            if giris == "1":
                cokgenKenar()
                

            elif giris == "2":
                
                icaciToplam()

            else:
                print("\nHatalı numara girdiniz.\n")
                continue
        else:
            print("\nHatalı karakter girdiniz.\n")
            continue
        break





