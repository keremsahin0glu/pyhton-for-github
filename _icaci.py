def icaciToplam():
    

    while True:
        kullanici_input = input("\nİç açısını bulmak istediğiniz çokgenin, kenar sayısını giriniz: ")       
        

        if kullanici_input.isdigit(): 

            kullanici_input_int = int(kullanici_input)
            
            if kullanici_input_int == 0 or kullanici_input_int == 1 or kullanici_input_int == 2 :
                print("Bir çokgen için en az 3 kenar gerekir")
                continue


            elif kullanici_input_int >= 3:
                icaciToplamlari = (kullanici_input_int -2) * 180

                if kullanici_input_int == 3:
                    print(f"Bir Üçgenin iç açılar toplamı {icaciToplamlari} derecedir.\n")
                    break

                elif kullanici_input_int == 4:
                    print(f"Bir Karenin iç açılar toplamı {icaciToplamlari} derecedir.\n")
                    break
                
                elif kullanici_input_int == 5:
                    print(f"Bir Beşgenin(Pentagon) iç açılar toplamı {icaciToplamlari} derecedir.\n")
                    break
                elif kullanici_input_int == 6:
                    print(f"Bir Altıgenin(Hexagon) iç açılar toplamı {icaciToplamlari} derecedir.\n")
                    break
                elif kullanici_input_int == 7:
                    print(f"Bir Yedigenin(Heptagon) iç açılar toplamı {icaciToplamlari} derecedir.\n")
                    break
                elif kullanici_input_int == 8:
                    print(f"Bir Sekizgenin(Oktagon) iç açılar toplamı {icaciToplamlari} derecedir.\n")
                    break
                elif kullanici_input_int == 9:
                    print(f"Bir Dokuzgenin(nonagon) iç açılar toplamı {icaciToplamlari} derecedir.\n")
                    break
                elif kullanici_input_int == 10:
                    print(f"Bir Ongenin(Dekagon) iç açılar toplamı {icaciToplamlari} derecedir.\n")
                    break
                    
                print(f"{kullanici_input_int} kenarlı bir çokgenin iç açılar toplamı {icaciToplamlari} derecedir.")
                break 



                
        else:
            print("Geçerli kenar sayısı giriniz.\n")
            continue

