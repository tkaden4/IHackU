# Base 16 Encoding

Base 16 is similar to base64 encoding, in that it produces plaintext output for any input.


Every 4 bits of the input stream is encoded as the first 16 letters of the alphabet, starting with
'a'. The uppermost bits are encoded first (MSB), then the lower bits are encoded (LSB).


For example: "Hello, World!" is encoded as "eigfgmgmgpcmcafhgphcgmgecb".
