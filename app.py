from _konusmaMetni import hosgeldiniz
from _isimdogrulama import isimdogrulama
from _yönlendirme import yonlendirme
from _tekrarsor import soru


try:
    isimdogrulama()    
    hosgeldiniz()
    yonlendirme()
    soru()
        
        
except:
    print("\nOturumu sonlandırdınız. İyi günler dileriz.")    

