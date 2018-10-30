def b16encode(text):
    result = bytearray(b"")
    for byte in text:
        # Convert 
        upper = (byte >> 4) & 0x0f
        lower = byte & 0x0f
        result.append(upper + ord('a'))
        result.append(lower + ord('a'))
    return result


def b16decode(text):
    result = bytearray(b"")
    for (b1, b2) in [(text[i], text[i + 1]) for i in range(0, len(text)-1, 2)]:
        b1 = b1 - ord('a')
        b2 = b2 - ord('a')
        result.append((b1 << 4) | b2)
    return result


HELP = "usage: base16 [decode|encode] TEXT"

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print(HELP)
        sys.exit(1)

    text = sys.argv[2]
    if sys.argv[1] == "decode":
        print(b16decode(bytes(text, "ascii")).decode("ascii"))
    elif sys.argv[1] == "encode":
        print(b16encode(bytes(text, "ascii")).decode("ascii"))
    else:
        print(HELP)
        sys.exit(1)
