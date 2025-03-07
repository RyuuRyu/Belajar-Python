### Tipe Data List

list = ["Ryu", "Jonathan", "Programmer", 20, "Jakarta"]

## List adalah tipe data yang berisi kumpulan item atau nilai, yang di tulis menggunakan tanda kurung siku [].
## List sama saja dengna Array pada bahasa pemrograman lainnya.
## Hanya saja List bisa berisi tipe data apapun dan tidak harus tipe data yang sama.
## LIst bahkan bisa berisi List lainnya, disebut Nested List.
## List bisa diubah atau dihapus nilainya setelah dideklarasikan.
## Data yang berada di dalam List berurutan dan bisa diakses menggunakan index.
## Index pada List dimulai dari 0, 1, 2, 3, dan seterusnya, seperti Array pada umumnya.

### Contoh 1
randomList = ["Apple", 123, True, 3.14, ("Banana", "Cherry"), ["Python", "Java", "C++"]]
print(randomList, "\n")

## Karena data yang berada di dalam List berurutan, maka kita bisa bisa memasukan data duplikat ke dalam List.

### Contoh 2
listBuah = ["Apple", "Banana", "Cherry", "Apple", "Cherry"]
print(listBuah, "\n")

## Kita juga bisa mendeklarasikan List kosong dan menambahkan item ke dalam List tersebut.

appendList = []
appendList.append("Apple")
appendList.append("Banana")
appendList.append("Orange")
appendList.append("Cherry")
print(appendList, "\n")

### Mengakses item dalam List

## Kita bisa mengakses item dalam List menggunakan index yang dimulai dari [0] sebagai Item pertama.

listPesawatTempur = [["F-16", "F-22", "F-35"], ["SU-35", "SU-57", "SU-30"]]
print(listPesawatTempur[0][1]) #Output = F-22
print(listPesawatTempur[1][2]) #Output = SU-30
print("\n")

## Kita juga bisa menggunakan negative index untuk mengakses item dari belakang.
print(listPesawatTempur[0][-1]) #Output = F-35
print(listPesawatTempur[1][-2]) #Output = SU-57

### Note!
