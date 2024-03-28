import string


def isimdogrulama():

    def isim():

        
        while True:
            
            
            kullanici_input = input("\nİsminizi giriniz:")
            for karakter in kullanici_input:
                
                
                if karakter.isdigit():         
                    print("Numara kullanmadan giriş yapınız.\n")
                    break
                elif karakter in string.punctuation:
                    print("Özel karakter kullanmayınız.\n")
                    break
                elif karakter == " ":
                    print("Boşluk kullanmadan giriş yapınız.\n")
                    break
                
                elif len(kullanici_input) == 1:
                    print("Muhtemelen tek harfli bir isme sahip değilsinizdir :)\n")
                    break
                elif len(kullanici_input) == 2:
                    print("Muhtemelen iki harfli bir isme sahip değilsinizdir :)\n")
                    break
                
                
            else:
                # Döngü hatasız tamamlandıysa, yani herhangi bir rakam veya özel karakter yoksa
                return kullanici_input
            
        
            

    kullanici_ismi = isim()
    kullanici_son_hal = kullanici_ismi.capitalize()
    print(f"\nHoşgeldin {kullanici_son_hal},")