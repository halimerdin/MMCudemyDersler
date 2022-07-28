#Kodlama egzersizimizde bir sınıfın harf notlarını hesapladığımız programı geliştirerek
#kalanları "kalanlar.txt" dosyasında ve geçenleri "geçenler.txt" dosyasına yazmaya çalışın.
def notHesapla(satır):
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

    if(sonNot>90):
        harf="AA"
    elif(sonNot>=85):
        harf="BA"
    elif (sonNot >= 80):
        harf = "BB"
    elif (sonNot >= 75):
        harf = "CB"
    elif (sonNot >= 70):
        harf = "CC"
    elif (sonNot >= 65):
        harf = "DC"
    elif (sonNot >= 60):
        harf = "DD"
    elif (sonNot >= 55):
        harf = "FD"
    else:
        harf="FF"

    return isim+"----------->"+harf+"\n"

def kalanlarListeleme(a):
    a = a[:-1]
    liste=a.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    sonNot=not1*0.3 + not2*0.3 + not3*0.4

    while(sonNot=>55):
        if(sonNot):
        a=""
def gecenlerListeleme(x):
    x = x[:-1]
    liste = x.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    sonNot=not1*0.3 + not2*0.3 + not3*0.4

    #while(sonNot):


with open("dosya.txt","r",encoding="utf-8") as file:
    #ekleneceklerListesi=[]
    kalanlarListesi=[]
    gecenlerListesi=[]
    for i in file:
        #notHesapla(i)
        ekleneceklerListesi.append(notHesapla(i))
    #print(ekleneceklerListesi)
    with open("notlar.txt","w",encoding="utf-8") as file2:
        #dosyamızın her bir satırını oluşuturulan eklecekler listesini yazmak istiyoruz
        for i in ekleneceklerListesi:
            file2.write(i)