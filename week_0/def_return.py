def main():
    x = int(input("berapa x nya: "))
    print("pangkat kuadrat x dengan print adalah", falsesquare(x))
    print("pangkat kuadrat x dengan return adalah", square(x))

def falsesquare(n): 
    print (n*n) # tetep terhitung, tapi untuk memanggil di def lain bakal none 
  
def square(n):
    return n**2 # jadi return kegunaannya(fungsinya) adalah memasukkan x (square(x))  ke  n (square(n)) lalu n akan di kuadrat, 
                # dimana hasilnya akan dikembalikn menjadi x di def main() pada square(X) 

main()