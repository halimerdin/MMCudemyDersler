import sqlite3
con =sqlite3.connect("lib01.db") #veritabanı oluşturup bağlandık
#veritabanı isminin uzantısının .db olması gerekli
#Database üzerinde Sql sorgularını çalıştırmak için cursor bir tane imleç oluşturuyoruz
cursor =  con.cursor()

def makeTable():
    pass



con.close() # Bağlantıyı koparıyoruz.