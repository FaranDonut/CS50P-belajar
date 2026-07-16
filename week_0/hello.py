# ask name
name = input("nama siapa?? ") 
print("halo, ")
print(name)
#atau
print("halo,",name) # (,) ga pake spasi
#atau
print("halo, " + name) # (+) pake spasi 
#atau 
print(f"halo, {name}") # ({name}) harus ada (f) sebelum " "

# materi string (str), ketika ada spasi berlebih, coba input spasi 2-3x sebelum memasukkan nama dan coba pakai 2-3 kalimat(nama panjang) dan semua huruf kecil, str bisa amanin kalimatnya 
temen = input ("siapa nama temenmu?? ")
print("before,",temen)
temen = temen.strip().title() # -> fungsi .strip() untuk menghilangkan white space (blank dari spasi) dan .title() untuk menjadikan setiap awalan kata memiliki hurf kapital besar seperti judul buku/nama orang/ kota dll
print("after,",temen)
