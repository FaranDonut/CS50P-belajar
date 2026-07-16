def main():
    indoorvoice = input(" ")
    print(say(indoorvoice))

def say(n):
     n = " ".join(n.split()).lower()
     return n 

main()