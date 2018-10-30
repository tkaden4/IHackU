# Shifty

Decode a key that has been shift-encoded with an unknown shift width.

Caveats: encode.py will convert strings to uppercase before encoding, and must only be alphabetical.

## Setup

Don't include `encrypt.py` or `solve.py`.

```Bash
./encrypt.py <SHIFT_DISTANCE> <TOKEN_FOR_THIS_CHALLENGE> > crypttext.txt
```

## Solution

See `solve.py` for the solver. Essentially we have a key encrypted by some sort of shift.

```Bash
./solve.py <CRYPT_TEXT>
```
