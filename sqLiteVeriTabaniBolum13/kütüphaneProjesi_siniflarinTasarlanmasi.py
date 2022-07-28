import sqlite3

import time

class Kitap():
    def __init__(self,isim,yazar,yayınevi,tur,baski):
        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tur = tur
        self.baski = baski
    def __str__(self):
        return "Kitap Ismi: {}\nYazar: {}\nYayinevi: {}\nTur: {}\nBaski: {}\n".format(self.isim,self.yazar,self.yayınevi,self.tur,self.baski)

class Kutuphane():
"""
asıl işlemlerin yapıldığı yer olacak
bu class içinde veri tabanına bağlanılacak ve kitaplarla ilgili değişik işlemler yapılacak


"""
    def __init__(self):
        #self.baglantiOlustur()
        pass


    def baglantiOlustur(self):
        self.baglanti=sqlite3.connect("lib01.db")
        self.cursor=self.baglanti.cursor()
        sorgu="Create Table If not exists books (Isim TEXT, Yazar TEXT,Yayınevi TEXT, Tur TEXT,Baski INT)"
        self.cursor.execute(sorgu)#tablo olu























