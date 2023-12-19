#Soru 5- Kullanicidan ismini, soyismini ve yasini alip asagidaki formatta yazdirin.
#girilen bilgiler : J Doe, 44

name = str(input("Lutfen isminizi giriniz: ")) #ahmet
surname = str(input("Lutfen soyisminizi giriniz: ")) #gulay
age = int(input("Lutfen yasinizi giriniz: ")) #32

print(f"{name[0].upper()} {surname[0].upper()}{surname[1:len(surname)].lower()}, {age}")