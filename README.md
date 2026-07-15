# CS50P-belajar
* journey belajar dan dibawah ini catatan untuk built in kedepannya

## Macam-macam built in di Python
### A

* **`abs(x)`**: Mengembalikan nilai absolut (mutlak) dari sebuah angka.
* **`aiter(async_iterable)`**: Mengembalikan *asynchronous iterator* (iterator asinkron) untuk sebuah koleksi asinkron.
* **`all(iterable)`**: Mengembalikan `True` jika semua elemen di dalam *iterable* bernilai benar, atau jika koleksi tersebut kosong.
* **`anext(async_iterator)`**: Mengambil item berikutnya dari sebuah *asynchronous iterator*.
* **`any(iterable)`**: Mengembalikan `True` jika ada minimal satu elemen di dalam *iterable* yang bernilai benar.
* **`ascii(object)`**: Menghasilkan string representasi objek, namun secara otomatis mengubah karakter non-ASCII menjadi kode *escape* (seperti `\x` atau `\u`).

### B

* **`bin(x)`**: Mengonversi bilangan bulat menjadi string biner yang diawali dengan prefiks `0b`.
* **`bool(x)`**: Mengonversi suatu nilai menjadi tipe data Boolean (`True` atau `False`).
* **`breakpoint()`**: Menghentikan sementara eksekusi program dan memasukkannya ke dalam mode *debugger* interaktif.
* **`bytearray()`**: Membuat objek array byte baru yang bersifat *mutable* (elemennya dapat diubah).
* **`bytes()`**: Membuat objek byte baru yang bersifat *immutable* (elemennya tidak dapat diubah).

### C

* **`callable(object)`**: Memeriksa apakah suatu objek dapat dipanggil layaknya sebuah fungsi (`True`/`False`).
* **`chr(i)`**: Mengonversi angka (kode Unicode) menjadi satu karakter string yang sesuai.
* **`classmethod()`**: Sebuah dekorator untuk mengubah sebuah metode menjadi metode kelas (*class method*).
* **`compile()`**: Mengompilasi string teks atau *Abstract Syntax Tree* (AST) menjadi objek kode Python yang siap dieksekusi.
* **`complex()`**: Mengonversi angka atau string menjadi bilangan kompleks (memiliki bagian real dan imajiner, contoh: `1+2j`).

### D

* **`delattr(object, name)`**: Menghapus atribut tertentu dari sebuah objek secara dinamis.
* **`dict()`**: Membuat objek *dictionary* (kamus data berpasangan *key-value*).
* **`dir()`**: Jika diberi argumen, mengembalikan daftar atribut/metode dari objek tersebut. Jika tanpa argumen, mengembalikan nama-nama variabel di lingkup lokal saat ini.
* **`divmod(a, b)`**: Mengembalikan sebuah *tuple* yang berisi hasil bagi dan sisa pembagian bilangan `(a // b, a % b)`.

### E

* **`enumerate(iterable)`**: Menambahkan indeks penghitung numerik pada *iterable* dan mengembalikannya sebagai objek enumerasi.
* **`eval(expression)`**: Mengevaluasi dan menjalankan satu baris ekspresi kalkulasi/logika Python yang ditulis dalam bentuk string.
* **`exec(object)`**: Menjalankan blok kode Python yang panjang dan dinamis dari sebuah string atau objek kode yang terkompilasi.

### F

* **`filter(function, iterable)`**: Menyaring elemen-elemen dari *iterable* yang memenuhi kondisi sebuah fungsi (bernilai `True`).
* **`float(x)`**: Mengonversi string atau bilangan bulat menjadi bilangan desimal/pecahan (*floating-point*).
* **`format(value, format_spec)`**: Memformat sebuah nilai menjadi string berdasarkan aturan atau spesifikasi format tertentu.
* **`frozenset()`**: Membuat objek *set* (himpunan) baru yang bersifat *immutable* (tidak bisa dimodifikasi setelah dibuat).

### G

* **`getattr(object, name)`**: Mengambil nilai dari atribut sebuah objek berdasarkan string nama atributnya.
* **`globals()`**: Mengembalikan *dictionary* yang berisi seluruh tabel simbol variabel di lingkup global saat ini.

### H

* **`hasattr(object, name)`**: Memeriksa apakah sebuah objek memiliki atribut tertentu yang dicari (`True`/`False`).
* **`hash(object)`**: Mengembalikan nilai *hash* (angka unik identifikasi data) dari sebuah objek yang bersifat *immutable*.
* **`help()`**: Memanggil sistem bantuan (*help system*) interaktif bawaan Python untuk menampilkan dokumentasi.
* **`hex(x)`**: Mengonversi bilangan bulat menjadi string heksadesimal (basis 16) yang diawali dengan `0x`.

### I

* **`id(object)`**: Mengembalikan identitas unik (alamat memori fisik) dari suatu objek selama program berjalan.
* **`input()`**: Menerima masukan (*input*) teks dari pengguna melalui konsol.
* **`int(x)`**: Mengonversi string atau angka pecahan menjadi bilangan bulat.
* **`isinstance(object, classinfo)`**: Memeriksa apakah suatu objek adalah instansiasi dari kelas tertentu atau turunan kelas tersebut.
* **`issubclass(class, classinfo)`**: Memeriksa apakah sebuah kelas merupakan turunan (*subclass*) dari kelas lainnya.
* **`iter(iterable)`**: Mengembalikan objek *iterator* dari sebuah koleksi data agar dapat diproses urutannya satu per satu.

### L

* **`len(s)`**: Mengembalikan jumlah item, panjang data, atau panjang karakter dari sebuah objek.
* **`list()`**: Membuat tipe data *list* (koleksi data berurutan yang bisa diubah).
* **`locals()`**: Mengembalikan *dictionary* yang berisi seluruh tabel simbol variabel di lingkup lokal saat ini.

### M

* **`map(function, iterable)`**: Menerapkan fungsi secara paralel ke setiap item dalam *iterable* dan mengembalikan *iterator* hasilnya.
* **`max()`**: Mencari dan mengembalikan nilai terbesar dari sebuah *iterable* atau kumpulan argumen.
* **`memoryview(object)`**: Membuka akses *buffer interface* ke memori suatu objek biner tanpa perlu menyalin data aslinya.
* **`min()`**: Mencari dan mengembalikan nilai terkecil dari sebuah *iterable* atau kumpulan argumen.

### N

* **`next(iterator)`**: Mengambil item atau elemen berikutnya dari sebuah *iterator*.

### O

* **`object()`**: Mengembalikan objek dasar tanpa fitur. Ini merupakan *base class* (induk tertinggi) dari semua kelas di dalam Python.
* **`oct(x)`**: Mengonversi bilangan bulat menjadi string oktal (basis 8) yang diawali dengan `0o`.
* **`open()`**: Membuka berkas (*file*) dari komputer dan mengembalikan objek *file* tersebut untuk proses baca/tulis.
* **`ord(c)`**: Mengonversi satu karakter string menjadi angka kode Unicode aslinya. (Kebalikan dari `chr()`).

### P

* **`pow(base, exp)`**: Menghitung hasil dari `base` pangkat `exp`. Jika ada parameter ketiga `pow(base, exp, mod)`, hasilnya akan langsung di-modulo.
* **`print()`**: Mencetak teks atau representasi objek ke layar/konsol keluaran.
* **`property()`**: Fungsi bawaan yang digunakan sebagai dekorator untuk membuat properti (pembungkus *getter*, *setter*, *deleter*) di dalam kelas.

### R

* **`range()`**: Menghasilkan deret angka secara berurutan, sangat umum digunakan sebagai pencacah dalam perulangan `for`.
* **`repr(object)`**: Mengembalikan representasi resmi objek berupa string yang dapat dieksekusi ulang oleh fungsi `eval()`.
* **`reversed(seq)`**: Mengembalikan *iterator* yang mengurutkan data secara terbalik (dari belakang ke depan).
* **`round(number)`**: Membulatkan angka pecahan ke jumlah digit desimal tertentu, atau ke bilangan bulat terdekat.

### S

* **`set()`**: Membuat objek himpunan (*set*) yang berisi elemen-elemen unik (otomatis menghapus duplikat) dan tidak memiliki urutan.
* **`setattr(object, name, value)`**: Menetapkan atau mengubah nilai sebuah atribut pada objek secara dinamis.
* **`slice()`**: Membuat objek pemotong (*slice object*) yang menentukan batasan awal, akhir, dan interval untuk memotong indeks.
* **`sorted(iterable)`**: Mengembalikan *list* baru yang berisi elemen-elemen yang sudah diurutkan dari nilai terkecil hingga terbesar (atau alfabetis).
* **`staticmethod()`**: Sebuah dekorator untuk mengubah sebuah metode menjadi metode statis (*static method*) yang independen dari instansiasi kelas.
* **`str()`**: Mengonversi objek atau nilai apa pun menjadi bentuk string (teks).
* **`sum(iterable)`**: Menjumlahkan seluruh angka yang ada di dalam sebuah koleksi data (*iterable*).
* **`super()`**: Mengembalikan objek proksi yang memungkinkan pemanggilan metode milik kelas induk (*parent class*) dari dalam kelas anak.

### T

* **`tuple()`**: Membuat tipe data *tuple* (koleksi data berurutan yang tidak bisa dimodifikasi atau *immutable*).
* **`type(object)`**: Mengembalikan informasi mengenai tipe data atau kelas pembuat dari objek tersebut.

### V

* **`vars()`**: Mengembalikan *dictionary* internal (`__dict__`) dari sebuah modul, kelas, atau objek yang berisi seluruh atributnya.

### Z

* **`zip(*iterables)`**: Menggabungkan elemen-elemen dari beberapa *iterable* menjadi pasangan-pasangan *tuple* secara sejajar.

### _ (Underscore)

* **`__import__()`**: Fungsi internal tingkat rendah yang secara tidak langsung dipanggil oleh interpreter Python saat Anda menjalankan perintah `import` modul. (Sangat jarang dipanggil secara langsung oleh *programmer*).
