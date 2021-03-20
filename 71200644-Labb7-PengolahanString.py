#71200644
#Freany usmany
#Universitas Kristen Duta Wacana

#Buatlah program untuk menghitung jumlah spasi kosong,bilangan,huruf vokal,dan konsonan.....

kalimat =input("Kalimat: ")

jumSpasi = 0
jumDigit = 0
jumVokal = 0
jumKonsonan = 0
for c in kalimat:
    if c.isspace():
        jumSpasi+=1
    elif c.isdigit():
        jumDigit+=1
    elif c.isalpha():
        if c in "aiueo":
            jumVokal +=1
        else:
            jumKonsonan +=1

print(f"jumlah spasi: {jumSpasi}")
print(f"jumlah Digit: {jumDigit}")
print(f"jumlah vokal: {jumVokal}")
print(f"jumlah Konsonan: {jumKonsonan}")