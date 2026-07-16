#without return, u can only print in this function not in main1(ga di kembalikan (return))
def area1(lenght, width):
    print(str(lenght * width) + " square feet")

def main1():
    area1(50, 20)
    area1(50, 50)
    print(area1(50, 20) + area1(50,50))  # bugnya disini, karena tidak di kembalikan nilainya
                                         # saat di operasikan(+,-,*,/,%,dll) tidak bisa dan terjadilah eror

###########################################################################
# it's difference with return, kalau di return dia bakal balik ke mainnya
# (more efficient and flexible)
def area2(lenght, width) :
    return lenght * width

def main2():
    house = area2(50, 20)
    yard = area2(50, 50)
    total = house + yard
    print(str(total) + " square feet")

main2()
main1() # ketika main 1 dipanggil dia error karena (none + none)

