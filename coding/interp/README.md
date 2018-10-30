# Greivm

A simple stack-based virtual machine.

## Specification

### Opcodes (1 byte each)

```
0x00 : push <byte>         # push the following byte to the stack
0x01 : pop                 # pop a byte from the stack
0x02 : dup                 # duplicate top of stack
0x03 : swap                # swap top of stack and top-1 of stack

0x04 : add                 # pop 2 bytes and push result of addition
0x05 : mul                 # pop 2 bytes and push result of multiplication

0x06 : and                 # bitwise AND
0x07 : or                  # bitwise OR
0x08 : xor                 # bitwise XOR
0x09 : not                 # bitwise NOT

0x0A : lt                  # push 1 if first operand is less than second operand, 0 otherwise
0x0B : gt                  # push 1 if first operand is greater than second operand, 0 otherwise
0x0C : eq                  # push 1 if first operand is equal to second operand, 0 otherwise

0x0D : print               # pop from stack and print (as character)
```

### Example Program

```
0x00 0x0A   : push 10
0x0D        : print
0x00 0xff   : push -1
0x04        : add
```
