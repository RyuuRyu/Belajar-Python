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

### Contoh menggunakan input
nama = input("Siapa nama kamu? ")
umur = input("Berapa umur kamu? ")
alamat = input("Dimana kamu tinggal?")
print("\n")

print("Halo " + nama + "\nJadi umur kamu " + umur + " tahun.\nDan kamu tinggal di " + alamat)
print("\n")