sayi1 = int(input("Birinci sayıyı giriniz:"))
sayi2 = int(input("İkinci sayıyı giriniz:"))

toplama = sayi1+sayi2
cikarma = sayi1-sayi2
carpma = sayi1*sayi2
bolme = sayi1//sayi2
us_alma = pow(sayi1,sayi2)

islem=input("Bir işlem giriniz:")
print(islem + "'in sonucu : ")
if islem == "toplama":
    print(toplama)
elif islem == "cikarma":
    print(cikarma)
elif islem == "carpma":
    print(carpma)
elif islem == "bolme":
    print(bolme)
elif islem == "us_alma":
    print(us_alma)
else:
    print("Geçersiz,işlemi yeniden yazın.")
