### Menerima Input dari User

# input("What is your name? ")
# input("How old are you? ")
# input("What are you doing here? ")

### Menggunakan Variabel

name = input("What is your name? ")
age = input("How old are you? ")
activity = input("What are you doing here? ")

print(f"Hello, {name}.\nI see, so your age is {age} years old. And you're currently {activity} right now.\nAnd good luck with that ^^")

## Logikanya sama seperti pada pemanggilan variabel menggunakan f-string.
## Kita hanya perlu menambahkan input() pada variabel yang akan kita gunakan.
## input dari user akan di simpan secara sementara pada variabel yang kita buat.
## dan kemudian kita panggil variabel tersebut pada print statement yang kita buat.