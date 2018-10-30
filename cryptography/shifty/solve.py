#!/usr/bin/python

import sys

def candidates(text):
    for i in range(0, 26):
        yield "".join([chr(ord('A') + (ord(d) - ord('A') + i) % 26) for d in text])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: solve.py TEXT")
    else:
        for c in candidates(sys.argv[1]):
            print(c)
