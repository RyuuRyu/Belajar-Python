### Global Variabel
pi = 3.14
diameter = 100
radius = diameter / 2
tinggi = 200


## Global Variabel adalah variabel yang dideklarasikan di luar fungsi.
## Variabel ini dapat diakses di semua fungsi yang ada dalam program.

### Contoh 1
def luas_lingkaran(jari_jari):
    return pi * jari_jari ** 2

luas_lingkaran = luas_lingkaran(radius)
print (f"Luas lingkaran dengan diameter {diameter} cm adalah {luas_lingkaran} cm\u00b2")
print("\n")

### Logika dari fungsi luas_lingkaran:
## - Variabel diameter dideklarasikan dengan nilai 50.
## - Variabel radius dideklarasikan dengan nilai diameter / 2.
## - Fungsi luas_lingkaran() dideklarasikan dengan parameter jari_jari.
## - Fungsi luas_lingkaran() mengembalikan hasil dari pi * jari_jari ** 2.
## - Variabel luas_lingkaran dideklarasikan dengan hasil dari fungsi luas_lingkaran(radius).

### Note!
## Pada baris ke 14, fungsi luas_lingkaran dipanggil dengan parameter radius.
## Radius adalah variabel yang dideklarasikan dengan nilai diameter / 2.
## Namun kenapa ketika kita memanggil luas_lingkaran = luas_lingkaran(radius) hasilnya tidak error?
## Padahal kita menggunakan parameter yang berbeda dengan parameter yang dideklarasikan pada fungsi luas_lingkaran(jari-jari).
## Hal ini terjadi karena variabel radius adalah variabel global.
## Variabel global adalah variabel yang dideklarasikan di luar fungsi.
## Variabel global dapat diakses di semua fungsi yang ada dalam program.
## Jadi pada luas_lingkaran = luas_lingkaran(radius), itu sama saja kita memberi parameter (jari_jari) nilai dari variabel radius.
## Dan nilai dari radius akan di eksekusi oleh fungsi luas_lingkaran(jari-jari) pada baris ke 11 dan 12.

### Contoh 2

def volume_tabung(jari_jari, tinggi):
    return pi * jari_jari ** 2 * tinggi

volume_tabung = volume_tabung(radius, tinggi)
print (f"Volume tabung dengan diameter {diameter} cm dan tinggi {tinggi} cm adalah {volume_tabung} cm\u00b3")
print("\n")

## Pada contoh 2, kita bisa memanggil variabel pi, diameter, radius, ddan tinggi tanpa harus mendeklarasikan variabel di dalam fungsi volume_tabung.
## Karena keempat variabel tersebut adalah variabel global, jadi fungsi volume_tabung bisa mengakses variabel pi yang dideklarasikan di luar fungsi.