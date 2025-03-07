### Tipe Data Integer (Bilangan Bulat)

a = 10
b = 5

print(a, b)

## Diatas adalah cara mendeklarasikan variabel dengan tipe data Integer.
## Berbeda dengan String, tipe data Integer tidak memerlukan tanda kutip.
## Tipe data Integer adalah tipe data yang berisi bilangan bulat.
## Dengan tipe data Integer, kita bisa melakukan operasi matematika seperti penjumlahan, pengurangan, perkalian, dan pembagian.
## Beberapa operator aritmatika di tulis sebagai berikut:
## Penjumlahan = +  
## Pengurangan = -
## Perkalian = *
## Pembagian = /
## Sisa Bagi = %
## Pangkat = **
## Pembagian Bulat = //

### Contoh 1
print("Hasil dari 10 + 5 adalah", a + b)
print("\n")

## Kita juga bisa menyimpan hasil operasi matematika ke dalam variabel sebuah variabel

### Contoh 2
x = 50
y = 10
z = x - y

print("Hasil dari 50 - 10 adalah", z)
print("\n")

## Kita juga bisa melakukan operasi matematika langsung pada print statement

### Contoh 3
print("Hasil dari 100 * 2 adalah", 100 * 2)
print("\n")

## Contoh Soal 1
print("Diketahui sebuah lingkaran dengan jari-jari 7 cm. Berapakah keliling lingkaran tersebut?")
print("Luas lingkaran = π * r^2")

## Maka kita bisa memasukan nilai jari-jari ke dalam sebuah variabel, dan melalukan operasi matematika pada print statement
r = 7
pi = 3.14
luas = pi * r ** 2

print("Luas lingkaran tersebut adalah", luas)
print("\n")

## Contoh Soal 2
print("Diketahui sebuah segitiga dengan alas 10 cm dan tinggi 5 cm. Berapakah luas segitiga tersebut?") 
print("Luas segitiga = 1/2 * alas * tinggi")

alas = 10
tinggi = 5

print("Luas segitiga tersebut adalah", 1/2 * alas * tinggi)
print("\n")


### Number Casting (Konversi Tipe Data)

## Pada Ptyhon, kita bisa mengkonversi tipe data integer ke float, atau sebaliknya.

### Contoh 4
pembulatan = (int(10.5))
print("10.5 dibulatkan akan menjadi", pembulatan)

## Pada contoh diatas, 10.5 dikonversi menjadi angka bulat dengan menggunakan fungsi int().
## Maka outputnya adalah 10, karena 10.5 dibulatkan ke bawah menjadi 10.

### Contoh 5
pembulatan2 = (int(3.14))
print("3.14 dibulatkan akan menjadi", pembulatan2)