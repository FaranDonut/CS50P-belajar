# ==========================================
# 1. VERSI SEBELUM (Tanpa return / Pakai print)
# ==========================================
emoticon_sebelum = "v.v"

def main_sebelum():
    global emoticon_sebelum
    print("--- Output Versi Sebelum ---")
    
    # Fungsi say_sebelum() langsung mencetak ke layar
    say_sebelum("Is anyone there?")
    say_sebelum("tes")

    emoticon_sebelum = ":D"
    say_sebelum("Oh, hi!")
    say_sebelum("tes")

def say_sebelum(phrase):
    # Melakukan perakitan teks sekaligus pencetakan
    print(phrase + " " + emoticon_sebelum)


# ==========================================
# 2. VERSI SESUDAH (Menggunakan return)
# ==========================================
emoticon_sesudah = "v.v"

def main_sesudah():
    global emoticon_sesudah
    print("\n--- Output Versi Sesudah ---")
    
    # Fungsi say_sesudah() mengembalikan teks, 
    # jadi kita butuh print() di sini untuk menampilkannya
    print(say_sesudah("Is anyone there?"))
    
    emoticon_sesudah = ":D"
    print(say_sesudah("Oh, hi!"))


def say_sesudah(phrase):
    # Murni hanya merakit teks lalu menyetorkannya kembali
    return phrase + " " + emoticon_sesudah


# ==========================================
# 3. MENJALANKAN KEDUA FUNGSI UTAMA
# ==========================================
main_sebelum()
main_sesudah()