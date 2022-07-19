from typing import Any


def gecenleriHesapla(satır):
    #\n dışında bütün satırı almak için
    satır=satır[:-1]

    #print(satır)
    liste=satır.split(",")
    #print(liste)

    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])

    sonNot=not1*0.3 + not2*0.3 + not3*0.4

    if(sonNot>90 and sonNot<=100):
        harf="AA"
    elif(sonNot>=85 and sonNot<=90):
        harf="BA"
    elif (sonNot >= 80 and sonNot<85):
        harf = "BB"
    elif (sonNot >= 75 and sonNot<80):
        harf = "CB"
    elif (sonNot >= 70 and sonNot<75):
        harf = "CC"
    elif (sonNot >= 65 and sonNot<70):
        harf = "DC"
    elif (sonNot >= 60 and sonNot<65):
        harf = "DD"
    elif (sonNot>55 and sonNot<60):
        harf = "EE"
    else:
        return ""
    return isim+"----------->"+harf+"\n"



def kalanlariHesapla(kalanlar):
    grade=""

    kalanlar=kalanlar[:-1]
    kalanlarListesi=kalanlar.split(",")

    name = kalanlarListesi[0]
    note1 = int(kalanlarListesi[1])
    note2 = int(kalanlarListesi[2])
    note3 = int(kalanlarListesi[3])
    #a = name + "------->" + grade + "\n"
    sonuc= note1 * 0.3 + note2 * 0.3 + note3 * 0.4

    if(sonuc>50 and sonuc<=55):
        grade = "FD"
    elif(sonuc<=50):
        grade = "FF"
    else:
        print("burdayım")
        return ""

    return name + "------->" + grade + "\n"


with open("dosya.txt","r",encoding="utf-8") as file:
    gecenlerListesi=[]
    kalanlarListesi=[]
    for i in file:
        gecenleriHesapla(i)
        kalanlariHesapla(i)
        gecenlerListesi.append(gecenleriHesapla(i))
        kalanlarListesi.append(kalanlariHesapla(i))

    #print(gecenlerListesi)
    with open("gecenler.txt","w",encoding="utf-8") as file2:
        #dosyamızın her bir satırını oluşuturulan eklecekler listesini yazmak istiyoruz
        for i in gecenlerListesi:
            file2.write(i)

    with open("kalanlar.txt","w",encoding="utf-8") as file3:
        for i in kalanlarListesi:
            file3.write(i)
