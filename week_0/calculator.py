# wrong version, karena ini masih string
print ("wrong version")
x = input("angka berapa x nya? ")
y = input ("angka berapa y nya? ")
z = x + y 
print(z)

# right version, int itu juga fungsi (inilah yang membedakan variabel itu str atau int, dengan menambah fungsi int)
print ("right version")
x = int(input("angka berapa x nya? "))
y = int(input ("angka berapa y nya? "))
print("versi x+y = ", x + y) 
#atau
z = x + y
print("versi +variabel = ", z)
print(f"{z:,}") #untuk nampilin koma, contoh : 1000 jadi 1,000 (seribu)

# decimal, with float 
print ("input decimal please")
x = float(input("angka desimal berapa untuk x? "))
y = float(input("angka desimal berapa untuk y? "))
print(x+y)
z = x + y
print(round(z))
z = x / y
print (z)
print (f"{z:.2f}") # sama kaya round (...., 2) cuma ini di f string pada print 
z = round (x / y, 2) # artinya dibulatkan pada dua angka contoh 0.8571 jadi 0.86
print (z)


