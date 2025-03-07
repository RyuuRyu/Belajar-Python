### Variabel
age = 20
name = "Ryu"
hobby = "Programming"

### Memanggil Variabel secara terpisah
print(age)
print(name)
print(hobby)

### Memanggil Variabel secara bersamaan dalam sebuah text

## Menggunakan operator +
print("Hello, my name is " + name + " and I am " + str(age) + " years old. I love " + hobby)
print("\n")

## Menggunakan operator ,
print("Hello, my name is", name, "and I am", age, "years old. I love", hobby)
print("\n")

## Menggunakan f-string
print (f"Hello, my name is {name}. and I am {age} years old. I love {hobby}")
print ("\n")

## Menggunakan format()
print ("Hello, my name is {}. and I am {} years old. I love {}".format(name, age, hobby))
print("\n")

### Mendeklarasikan beberapa Variabel dan memanggilnya secara bersamaan
umur, nama, hobbi = 20, "Jonathan", "Drawing"
print (umur, nama, hobbi)

### Note!

## Pada pemanggilan variabel pada text smenggunakan operator +, untuk variabel age ditulis str(age).
## Karena age adalah tipe data integer, sedangkan variabel name dan hobby adalah tipe data string.
## Sedangkan pada pemanggilan variabel menggunakan operator , tidak perlu menambahkan str(age).
## Karena operator , akan secara otomatis mengkonversi tipe data integer ke string.

## Namun jika kita memanggil variabel menggunakan operator +, tapi tetap menulis variabel age tanpa str(age).
## Maka akan muncul error seperti ini: TypeError: can only concatenate str (not "int") to str.
## Karena operator + tidak bisa secara otomatis mengkonversi tipe data integer ke string.

## Sedangkan untuk f-string dan format() tidak perlu menambahkan str(age) karena kedua cara tersebut.
## Tidak perlu mengkonversi tipe data integer ke string.