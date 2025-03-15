### Tipe Data String

nama = "Ryu"
umur = "20"
alamat = "Jakarta"
pekerjaan = "Programmer"

## Tipe Data String adalah tipe data yang berisi text atau kalimat.
## Tipe data ini bisa berisi huruf, angka, simbol, dan karakter khusus lainnya.
## Setiap mendeklarasikan tipe data String maka harus menambahkan tanda kutip ("") atau ('') pada text yang akan di deklarasikan.
## Tipe data ini bisa di deklarasikan dengan menggunakan tanda kutip satu ('') atau dua ("").

## Pada contoh di atas, kita mendeklarasikan beberapa variabel dengan tipe data String.
## Variabel nama berisi "Ryu", variabel umur berisi "20", variabel alamat berisi "Jakarta", dan variabel pekerjaan berisi "Programmer".

### Contoh 1
print("Halo, nama saya adalah " + nama + ". Saya berumur " + umur + " tahun. Saya tinggal di " + alamat + " dan bekerja sebagai " + pekerjaan)
print("\n")

## Contoh diatas adalah salah satu cara untuk memanggil variabel yang berisi tipe data String.
## Caranya sama seperti yang sudah dicoba pada file Variables.py
## Kita hanya perlu menambahkan tanda kutip pada text yang akan kita tampilkan.

### Contoh 2
print("Halo, nama saya adalah Ryu. Saya berumur 20 tahun. Saya tinggal di Jakarta dan bekerja sebagai Programmer")
print("\n")

## Perbedaan antara Contoh 1 dan Contoh 2 adalah pada Contoh 1 kita memanggil variabel yang berisi tipe data String
## Sedangkan pada Contoh 2 kita langsung menuliskan text yang akan kita tampilkan tanpa memanggil variabel.

print("##############################################")
print("\n")

### Contoh menggunakan input
# nama = input("Siapa nama kamu? ")
# umur = input("Berapa umur kamu? ")
# alamat = input("Dimana kamu tinggal? ")
# print("\n")

# print("Halo " + nama + "\nJadi umur kamu " + umur + " tahun.\nDan kamu tinggal di " + alamat)
# print("\n")

## Kita juga bisa mendeklarasikan sebuah string sebagai nilai dari variabel
## Dan kita bisa memanggil variabel tersebut sebagai nilai dari variabel lainnya.

print("##############################################")
print("\n")

### Contoh 3

namaSaya = "Ryu"
namaPanggilan = "Jonathan"
namaLengkap = "Halo, nama saya adalah " + namaSaya + " tapi teman-teman memanggil saya " + namaPanggilan
print(namaLengkap,"\n")

### Escape Character

## Escape Character adalah karakter khusus yang digunakan untuk memberikan efek tertentu pada text.
## Karakter ini diawali dengan tanda backslash (\).
## Seperti pada contoh diatas, kita banyak menggunakan karakter backslash (\n) yang berfungsi untuk memberikan efek baris baru pada text.
## Meskipun tidak perlu membuat fungsi print yang berisi (\n) seara terpisah, kita bisa langsung memasukkannya kedalam teks.

### Contoh 4

## Baris Baru
print("Halo. Nama saya adalah Ryu.\nSaya berumur 20 tahun.\nDan saya tinggal di Jakarta.\n")

## Efek Tab
print("Nama\t: Ryu\nUmur\t: 20 tahun\nAlamat\t: Jakarta")

## Backslash
print("C:\\User\\Ryu")

## Single Quote
print("Halo, nama saya 'Ryu'\n")
print('Halo, nama saya "Ryu"\n')  

## Pada kasus Quote, kita bisa menggunakan tanda kutip satu ('') atau dua ("") untuk menampilkan text yang berisi tanda kutip.
## Kita bisa memasukan kata yang di himpit kutip kedalam text, maka kita bisa menggunakan tanda kutip yang berbeda.
## Namun bagaimana jika kita sudah menggunakan kutip dua ("") namun kita ingin menampilkan text yang berisi kutip dua juga?
## Maka kita bisa menggunakan Blackslash seperti pada contoh lainnya diatas.

print("\"E = mc\u00b2\"\n-Albert Einstein")
print("\n")

### String Methods

## String Methods adalah method yang digunakan untuk memanipulasi tipe data String.
## Beberapa method yang sering digunakan adalah:
## 1. capitalize() = Mengubah huruf pertama dari text menjadi huruf kapital.
## 2. lower() = Mengubah semua huruf dalam text menjadi huruf kecil.
## 3. upper() = Mengubah semua huruf dalam text menjadi huruf kapital.
## 4. replace() = Mengganti text dengan text lainnya.
## 5. split() = Memisahkan text menjadi List.
## 6. join() = Menggabungkan text dari List.

### Contoh 5

text = "Halo, nama saya adalah Ryu"
print(text.capitalize()) 
print(text.lower())
print(text.upper())
print(text.replace("Ryu", "Jonathan"))
print(text.split())

## Selain contoh diatas, ada banyak method lainnya yang bisa digunakan untuk memanipulasi tipe data String.
## Kita bisa mencari method-method tersebut di dokumentasi Python atau https://www.w3schools.com/python/ref_string_center.asp

