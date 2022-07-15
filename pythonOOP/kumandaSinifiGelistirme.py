import random
import time

class Kumanda():
    def __init__(self,tvDurum="Kapalı",tvSes=0,kanalListesi=["Trt"],kanal="TRT"):
        self.tvDurum=tvDurum
        self.tvSes = tvSes
        self.kanalListesi = kanalListesi
        self.kanal = kanal

    def tvAC(self):
        if(self.tvDurum=="Açık"):
            print("TV zaten açık...")
        else:
            print("TV açılıyor...")
            self.tvDurum="Açık"

    def tvKapat(self):
        if(self.tvDurum=="Kapalı"):
            print("TV zaten kapalı")
        else:
            print("TV kapanıyor")
            self.tvDurum="Kapalı"

    def sesAyarlari(self):
        while True:
            cevap=input("sesi azaltmak için '<'\nsesi artırmak için '>'\n çıkış: çıkış  ")

            if(cevap=='<'):
                if(self.tvSes!=0):
                    self.tvSes-=1
                    print("Ses: ",self.tvSes)
            elif (cevap=='>'):
                if (self.tvSes != 31):
                    self.tvSes += 1
                    print("Ses: ", self.tvSes)
            else:
                print("ses güncellendi",self.tvSes)
                break

    def kanalEkle(self,kanalIsmi):
        print("kanal ekleniyor")
        time.sleep(1)
        self.kanalListesi.append(kanalIsmi)

        print(kanalIsmi,": kanalı eklendi")

    def rastgeleKanal(self):
        rastgele=random.randint(0,len(self.kanalListesi)-1)

        self.kanal=self.kanalListesi[rastgele]

        print(("şuanki kanal: ",self.kanal))

    def __len__(self):
        return len(self.kanalListesi)

    def __str__(self):
        return "TV durumu: {}\nTV Ses: {}\nkanal listesi {}\nŞu an ki kanal: {}".format(self.tvDurum,self.tvSes,self.kanalListesi,self.kanal)

kumanda=Kumanda()

print("""
TELEVİZYON UYGULAMASI
1.Tv aç
2.Tv kapat
3.Ses ayarları
4.kanal ekle
5.kanal sayısını öğrenme
6.Rastgele kanala geçme
7.televizyon bilgileri
çıkmak için q ya basın
""")

while True:
    islem=input("işlemi giriniz: ")

    if(islem=="q"):
        print("program sonlandırılıyor...")
        break

    elif(islem=="1"):
        kumanda.tvAC()

    elif(islem=="2"):
        kumanda.tvKapat()

    elif(islem=="3"):
        kumanda.sesAyarlari()

    elif(islem=="4"):
        kanalIsimleri=input("kanal isimlerini virgül(,) ile ayırarak giriniz: ")
        kanalListesi=kanalIsimleri.split(",")
        for eklenecekler in kanalListesi:
            kumanda.kanalEkle(eklenecekler)
    elif(islem=="5"):
        print("kanal satısı:",len(kumanda))

    elif(islem=="6"):
        kumanda.rastgeleKanal()
    elif(islem=="7"):
        print((kumanda))

    else:
        print("geçersiz işlem")



