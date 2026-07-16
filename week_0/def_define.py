"""
Contoh sintaks: def hello(to="world"):
Artinya, jika programmer memanggil hello() tanpa argumen, 
maka Python secara otomatis akan menggunakan nilai "world"
sebagai sapaan. Namun, jika programmer memanggil hello("David"), 
maka "David" akan menggantikan nilai default tersebut.

"""

def hello(to="world"): #ketika () -> kosong dia defaultnya sesuai to (to = "...")
    print("hello,", to)

def main():
    hello()
    name = input ("siapa namamu? ")
    hello(name)

main() # -> cukup dipanggil main karena di dalam main udh manggil hello (...)
