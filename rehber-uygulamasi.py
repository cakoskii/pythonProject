rehber = {
    "Battal":{
        "Cep":312312321312,
        "İş":1655431444354,
        "Ev":83468464874686
    },
    "Ahmet":{
        "Cep":312312321312,
        "İş":1655431444354,
        "Ev":83468464874686
    },
    "Mürşide":{
        "Cep":312312321312,
        "İş":1655431444354,
        "Ev":83468464874686
    }
}
while True:
    isimler = rehber.keys()
    giris = input("Kişi adı : ")

    if giris in isimler:
        tel = input("İstediğiniz telefon numarası hangisidir? : ")
        print(rehber.get(giris).get(tel,"İstediğiniz numara mevcut değildir."))
    else:
        print("İstediğiniz kişi mevcut değildir.")
    cikis = input("Yeniden arama yapmak için enter'a basınız veya çıkış yapmak isterseniz Q tuşuna basıp enterlayın.")
    if cikis=="Q" or cikis=="q":
        print("Çıkış yapılıyor.")
        quit()
