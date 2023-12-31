#Soru 1- Kullanicidan 4 basamakli pozitif bir tamsayi alip rakamlar toplamini bulalim
#Ipucu 1: Sayi % 10 => Bize son basamagi verir
#1469 % 10 = 9
#Ipucu 2: Int Sayi /10 => Bize son basamak haric sayiyi verir
#int sayi=1469;
#sayi = sayi / 10 =>
#sayi’ya 46 degerini atar

v = int(input("4 basamakli bir sayi giriniz: "))

birlerBasamagi = v % 10
v = v // 10
onlarBasamagi = v % 10
v = v // 10
yuzlerBasamagi = v % 10
v = v // 10
binlerBasamagi = v % 10

print(f"Girilen 4 basamakli sayinin rakamlar toplami {birlerBasamagi + onlarBasamagi + yuzlerBasamagi + binlerBasamagi}")