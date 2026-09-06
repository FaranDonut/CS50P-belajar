def main():
    faces = input(" ")
    print(emoji(faces))

def emoji(n):
    n = n.strip().replace(':)','🙂').replace(':(','🙁')
    return n

main()


