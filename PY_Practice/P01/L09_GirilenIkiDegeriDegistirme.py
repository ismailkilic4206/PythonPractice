#Soru 8- Kullanicidan iki sayi alip, ucuncu bir degisken kullanmadan ikisinin
#degerlerini degistirin(swap).

k = int(input("Ilk Deger (k): "))
l = int(input("Ikinci Deger (l): "))

k = k + l
l = k - l
k = k - l
print(f"Girmis oldugunuz k'nin yeni degeri: {k} l'nin yeni degeri: {l}")
