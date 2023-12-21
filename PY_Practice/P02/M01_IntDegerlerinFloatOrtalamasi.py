#Soru 1- Int olarak verilen 3 degerin ortalamasini float olarak ve tamsayi olarak
#yazdiran bir kod yazin

v1 = int(input("1. tamsayiyi giriniz: ")) #8
v2 = int(input("2. tamsayiyi giriniz: ")) #5
v3 = int(input("3. tamsayiyi giriniz: ")) #4

print(f"Kullanicidan alinan uc sayinin float ortalamasi: {(v1 + v2 + v3) / 3 }") #Kullanicidan alinan uc sayinin float ortalamasi: 5.666666666666667
print(f"Kullanicidan alinan uc sayinin tamsayi ortalamasi: {(v1 + v2 + v3) // 3 }") #Kullanicidan alinan uc sayinin tamsayi ortalamasi: 5