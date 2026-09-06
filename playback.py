def main():
    playback = input(" ")
    print(say(playback))

def say(n):
    n = n.strip().replace(" ","...")
    return n

main()

