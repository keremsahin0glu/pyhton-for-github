def cokgenKenar():

    

    while True:
        kullanici_input = input("\nKöşegen sayısını bulmak istediğiniz çokgenin, kenar sayısını giriniz:")

        if kullanici_input.isdigit(): 

            kenar_sayisi = int(kullanici_input)

            if kenar_sayisi == 0 or kenar_sayisi == 1 or kenar_sayisi == 2 :
                print("Bir çokgen için en az 3 kenar gerekir")
                continue

            elif kenar_sayisi == 3:
                print("Üçgenin köşegeni yoktur.")
                continue
            

            elif kenar_sayisi >= 3:                
                kösegenSayısı = kenar_sayisi * ( kenar_sayisi - 3) // 2

                if kenar_sayisi == 4:
                    print(f"Bir Karenin {kösegenSayısı} tane köşegeni vardır.")
                    break
                elif kenar_sayisi == 5:
                    print(f"Bir Beşgenin(Pentagon) {kösegenSayısı} tane köşegeni vardır.\n")
                    break
                elif kenar_sayisi == 6:
                    print(f"Bir Altıgenin(Hexagon) {kösegenSayısı} tane köşegeni vardır.\n")
                    break
                elif kenar_sayisi == 7:
                    print(f"Bir Yedigenin(Heptagon) {kösegenSayısı} tane köşegeni vardır.\n")
                    break
                elif kenar_sayisi == 8:
                    print(f"Bir Sekizgenin(Oktagon) {kösegenSayısı} tane köşegeni vardır.\n")
                    break
                elif kenar_sayisi == 9:
                    print(f"Bir Dokuzgenin(nonagon) {kösegenSayısı} tane köşegeni vardır.\n")
                    break
                elif kenar_sayisi == 10:
                    print(f"Bir Ongenin(Dekagon) {kösegenSayısı} tane köşegeni vardır.\n")
                    break
                


                print (f"{kenar_sayisi} kenarlı bir çokgenin {kösegenSayısı} tane köşegeni vardır.\n")
                break
                
        else:
            print("Hatalı karakter girdiniz\n")
            continue









