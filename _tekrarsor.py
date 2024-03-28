from _konusmaMetni import hosgeldiniz
from _yönlendirme import yonlendirme

def soru():

    while True:

        kullanici_input = input("\n Ana Menü'ye dönmek için => 1\n Oturumu sonlandırmak için => 2\n numaralarından birini tuşlayınız: ")

        if kullanici_input.isdigit():          
            

            if kullanici_input == '1':
                return hosgeldiniz(), yonlendirme(), soru()
                
            
                
            
            elif kullanici_input == '2':
                print("\nOturumu sonlandırdınız. İyi günler dileriz.")
                break

            elif kullanici_input != '1' or kullanici_input != '2':
                print("Geçerli numaralı giriniz")
                continue           
            

        else:
            print("Hatalı karakter girildi.\n")
            continue
    