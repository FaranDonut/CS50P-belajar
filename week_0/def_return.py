def main():
    x = int(input("berapa x nya: "))
    print("pangkat kuadrat x dengan print adalah", falsesquare(x)) #ketika di print untuk dipanggil lagi dia tidak kemabli(return), sehingga ouputnya none
    print("pangkat kuadrat x dengan return adalah", square(x))
    falsesquare(x) # di print pada fungsi def falsesquare nya 
    square(x) # tidak bakal keluar karena belum di print, makanya di main(), di print (ini logika yang di recommend)

def falsesquare(n): 
    print ("pada fungsi falsesquare(n), bukan dipanggil di main  (bukan main)", n*n) # tetep terhitung, tapi untuk memanggil di def lain bakal none 
  
def square(n):
    return n**2 # jadi return kegunaannya(fungsinya) adalah memasukkan x (square(x))  ke  n (square(n)) lalu n akan di kuadrat, 
                # dimana hasilnya akan dikembalikn menjadi x di def main() pada square(X) 

main()