"""
class Accont:
    def __init__(self, isim, numara, bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye
    def HesapBilgileri(self):
        print("İsim: ", self.isim)
        print("Numara: ", self.numara)
        print("Bakiye", self.bakiye)
    def ParaCek(self, miktar):
        if(self.bakiye-miktar<0):
            print("Bakiyeniz yeterli değil...")
        else:
            self.bakiye-=miktar
            print("Yeni Bakiye: ", self.bakiye)
    def ParaYatır(self,miktar):
        self.bakiye += miktar
        print("Yeni Bakiye: ", self.bakiye)

"""

info = input("Giriş Yap[1], Kayıt Yap[2]: ")

while info == "2":
    username = input("Kullanıcı Adı Oluştur: ")
    password = input("Şifre Oluştur: ")
    password1 = input("Şifreyi Tekrarla: ")
    if password == password1:
        file = open(username + ".txt", "w")
        file.write(username + " : " + password)
        file.close()
        welcome = "y"
        yonetim_paneli = True
        break
    print("Şifreler Aynı değil...")

while info == "1":
    login1 = input("Kullanıcı adı: ")
    login2 = input("Şifre: ")
    file = open(login1 + ".txt", "r")
    data = file.readline()
    file.close()
    if data == login1 + ":" + login2:
        yonetim_paneli = True
        break
    print("Kullanıcı adı veya şifre yanlış !")

while yonetim_paneli:
    print("Welcome to ABC Bank Select operation. ")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    break

