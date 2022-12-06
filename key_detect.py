import sys


def getchar():
    str = ""
    while True:
        c = sys.stdin.read(1)  # reads one byte at a time, similar to getchar()
        if c == ' ':
            break
        str += c
        break
    print(str)
