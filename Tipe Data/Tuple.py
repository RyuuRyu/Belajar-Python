### Tipe Data Tuple

## Tuple adalah tipe data yang mirip dengan List, namun Tuple bersifat immutable atau tidak bisa diubah setelah dideklarasikan.
## Tuple menggunakan tanda kurung ().
## Tuple bisa berisi tipe data apapun dan tidak harus tipe data yang sama.
## Tuple bisa berisi Tuple lainnya, disebut Nested Tuple.
## Tuple bisa diakses menggunakan index karena bersifat ordered.
## Index pada Tuple dimulai dari 0, 1, 2, 3, dan seterusnya, seperti List.

### Contoh 1

tupleMobil = ("Toyota", "Honda", "Suzuki", "Mitsubishi")
print(tupleMobil)

## Karena Tuple bersifat ordered, maka kita bisa memasukan data duplikat ke dalam Tuple.

## Contoh 2 

tupleMobil = ("Toyota", "Honda", "Suzuki", "Mitsubishi", "Toyota")
print(tupleMobil)