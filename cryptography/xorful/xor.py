
# Simple XOR encryption
def encrypt(plaintext, key):
    keylen = len(key)
    encrypted = bytearray(b"")
    for i, c in enumerate(plaintext):
        encrypted.append(c ^ key[i % keylen]);
    return encrypted
