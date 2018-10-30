#!/usr/bin/python

import sys

def encode(text, shift):
    return "".join([chr(ord('A') + ((ord(d) - ord('A') + shift) % 26)) for d in text])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("USAGE: encode.py TEXT SHIFT")
        sys.exit(1)
    else:
        text = sys.argv[1].upper()
        shift = int(sys.argv[2])
        print(encode(text, shift))
