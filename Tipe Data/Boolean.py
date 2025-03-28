### Tipe Data Booelan

a = True
b = False

## Tipe data Boolean adalah tipe data yang hanya memiliki dua nilai, yaitu True atau False.
## Tipe data ini biasanya digunakan untuk kondisi atau perbandingan.

print(a)
print(b)
print("\n")

## Di atas adalah cara mendeklarasikan variabel dengan tipe data Boolean.
## Tipe data ini erat kaitannya dengan sebuah kondisi atau perbandingan.
## Analogi sederhana dari Boolean adalah "Ya" dan "Tidak" atau "Benar" dan "Salah"

### Contoh 1
print("Apakah 10 lebih dari 5?\n", 10 > 5)

print("Apakah 10 kurang dari 5?\n", 10 < 5)

print("Apakah 10 sama dengan 5?\n", 10 == 5)

print("Apakah hasil dari 10 + 5 lebih dari 10?\n", 10 + 5 > 10)
print("\n")

### Contoh 2
x = 100
y = 200

if x > y :
    print("x lebih besar dari y")
else:   
   print("x lebih kecil dari y")

## FUngsi juga bisa mengembalikan nilai Boolean

### Contoh 3

def cekAngka(angka):
    if angka > 100:
        return True
    else:
        return False
    
print(cekAngka(200))
print(cekAngka(50))