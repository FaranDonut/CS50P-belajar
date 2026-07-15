x = input("angka berapa x nya? ")
y = input ("angka berapa y nya? ")

# wrong version, karena ini masih string
print ("wrong version")
z = x + y 
print(z)

# right version, int itu juga fungsi (inilah yang membedakan variabel itu str atau int)
print ("right version")
z = int (x) + int (y)
print(z)
