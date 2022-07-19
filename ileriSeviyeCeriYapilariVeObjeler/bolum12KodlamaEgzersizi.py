class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            dosyaIcerigi=file.read()
            kelimeler=dosyaIcerigi.split()#içerisine bişey verilmediği için boşluğa göre ayırdı
            self.sadeKelimler=list()#başka yerlerde kullanabilmek için classın elemanı yaptık


            #print(dosyaIcerigi)
            for i in kelimeler:
                #print(i)
                i=i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")

                self.sadeKelimler.append(i)
    def tumKelimeler(self):
        kelimelerKumesi=set()#bir kelimeden bir den fala gelmesi ihtimaline karşı küme kullanıldı
        for i in self.sadeKelimler:
            kelimelerKumesi.add(i)
        print("Tüm kelimeler....")
        for i in kelimelerKumesi:
            print(i)
            print("***********")
                #dögü bittikten sonra elimizde sadece sadeleşmiş kelimler bulunacak
            #bu sade kelimeleri bastırmak için
            """for i in self.sadeKelimler:
                print(i)"""
    def kelimeFrekansı(self):#bir kelimenin kaç defa geçtiğini bulmak için
        kelimeSozluk=dict()
        for i in self.sadeKelimler:
            if(i in kelimeSozluk):#kelime kelime sözlüğünde şu anda var mı?
                kelimeSozluk[i]+=1
            else:#eğer o kelimemiz ilk defa geliyorsa
                kelimeSozluk[i]=1
        for kelime,sayi in kelimeSozluk.items():
            print("{} kelimesi {} defa geçiyor....".format(kelime,sayi))
            print("----------------------------------------")

dosya=Dosya()
#dosya.tumKelimeler()
dosya.kelimeFrekansı()
