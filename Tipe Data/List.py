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
print(randomList)

## Karena data yang berada di dalam List berurutan, maka kita bisa bisa memasukan data duplikat ke dalam List.

### Contoh 2
listBuah = ["Apple", "Banana", "Cherry", "Apple", "Cherry"]
print(listBuah, "\n")

## Kita juga bisa mendeklarasikan List kosong dan menambahkan item ke dalam List tersebut.

appendList = []
print(appendList)
appendList.append("Apple")
appendList.append("Banana")
print(appendList)

## insert() dan append() adalah method yang digunakan untuk menambahkan item ke dalam List.
## Perbedaan antara insert dan append adalah, insert menambahkan item ke dalam List pada index tertentu.
## Sedangkan append menambahkan item ke dalam List pada akhir List.

appendList.insert(0, "Cherry") #Cherry akan menjadi item pertama dalam List.
appendList.insert(3, "Mango") #Mango akan menjadi item keempat dalam List.
print(appendList, "\n")


### Mengakses item dalam List

## Kita bisa mengakses item dalam List menggunakan index yang dimulai dari [0] sebagai Item pertama.
listPesawatTempur = [["F-16", "F-22", "F-35"], ["SU-35", "SU-57", "SU-30"]]
print(listPesawatTempur[0][1]) #Output = F-22
print(listPesawatTempur[1][2], "\n") #Output = SU-30

## Kita juga bisa menggunakan negative index untuk mengakses item dari belakang.
print(listPesawatTempur[0][-1]) #Output = F-35
print(listPesawatTempur[1][-2]) #Output = SU-57
print("\n")

### Slicing List

## Slicing List adalah cara untuk mengambil beberapa item dari List.
## Slicing List menggunakan tanda [:] dan bisa diisi dengan index awal dan index akhir.
## Jika index awal tidak diisi, maka akan dimulai dari index 0.
## Jika index akhir tidak diisi, maka akan diambil sampai index terakhir.

listBuah2 = ["Apple", "Banana", "Chery", "Orange", "Grape", "Watermelon"]
print(listBuah2[1:4]) #Output = ["Banana", "Cherry", "Orange"]
print(listBuah2[:4]) #Output = ["Apple", "Banana", "Cherry", "Orange"]
print("\n")

### Mengubah item dalam List

## Kita bisa mengubah item dalam List dengan cara mengakses item tersebut menggunakan index dan menggantinya dengan item baru.
## Kita juga bisa mengubah item dalam List menggunakan Slicing List.

listBuah2 [1] = "Mango"
listBuah2 [0] = "Guava"
listBuah2[2:4] = ["Pineapple", "Kiwi"] #Mengganti item index 2 dan 3 dengan item baru.
print(listBuah2)

### Extend List

## Extend List adalah cara untuk menambahkan item dari List lain ke List yang sudah ada.
## Extend List menggunakan method extend().
## Method extend() akan menambahkan item dari List lain ke List yang sudah ada.
## Isi dari List Sayur akan ditambahkan ke List Buah dan letaknya akan berada di akhir List Buah.

listSayur = ["Carrot", "Cabbage", "Broccoli"]
listBuah2.extend(listSayur)
print(listBuah2, "\n")


