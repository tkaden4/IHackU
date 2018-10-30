

class Generator:
    def __init__(self, out):
        self.out = out

    def push(self, byte):
        self.out(0x00)
        self.out(byte)

    def pop(self):
        self.out(0x01)

    def dup(self):
        self.out(0x02)

    def swap(self):
        self.out(0x03)

    def add(self):
        self.out(0x04)

    def mul(self):
        self.out(0x05)

    def band(self):
        self.out(0x06)

    def bor(self):
        self.out(0x07)

    def bxor(self):
        self.out(0x08)

    def bnot(self):
        self.out(0x09)

    def lt(self):
        self.out(0x0A)

    def gt(self):
        self.out(0x0B)

    def eq(self):
        self.out(0x0C)

    def bprint(self):
        self.out(0x0D)

class Interpreter:
    def __init__(self):
        self.stack = bytearray(b"")

    def push(self, byte):
        self.stack.append(byte)

    def pop(self):
        return self.stack.pop()

    def pop2(self):
        return (self.pop(), self.pop())

    def dup(self):
        a = self.pop()
        self.push(a)
        self.push(a)

    def swap(self):
        a, b = self.pop2()
        self.push(a)
        self.push(b)

    def add(self):
        a, b = self.pop2()
        self.push((a + b) & 0xff)

    def mul(self):
        a, b = self.pop2()
        self.push((a * b) & 0xff)

    def band(self):
        a, b = self.pop2()
        self.push(a & b)

    def bor(self):
        a, b = self.pop2()
        self.push(a | b)

    def bxor(self):
        a, b = self.pop2()
        self.push(a ^ b)

    def bnot(self):
        a = self.pop()
        self.push(~a & 0xff)

    def lt(self):
        a, b = self.pop2()
        self.push(1 if a < b else 0)

    def gt(self):
        a, b = self.pop2()
        self.push(1 if a > b else 0)

    def eq(self):
        a, b = self.pop2()
        self.push(1 if a == b else 0)

    def bprint(self):
        print(chr(self.pop()), end="")


def push_str(self, s):
    for b in bytes(s, "ascii")[::-1]:
        self.push(b);

def random_noise(self, size):
    import random

    def comp_widget(self):
        a = random.randint(0, 0xff)
        b = random.randint(0, 0xff)
        self.push(a)
        self.push(b)
        if a < 155:
            self.gt()
        elif a < 200:
            self.eq()
        else:
            self.lt()

        self.pop()

    def expr_widget(self):
        self.push(random.randint(0, 0xff))
        self.push(random.randint(0, 0xff))
        op = random.randint(0, 1)
        if op == 1:
            self.add()
        else:
            self.mul()

        self.pop()
    
    def xor_widget(self):
        s = [chr(random.randint(0, 25) + ord('a')) for i in range(random.randint(5, 10))]
        for i,c in enumerate(s):
            self.push(ord(c))
            self.push(ord('a'))
            self.bxor()
            self.pop()

    possible_widgets = [comp_widget, expr_widget, xor_widget]

    for x in range(0, size):
        possible_widgets[random.randint(0, len(possible_widgets) - 1)](self)

def encode_key(self, key):
    push_str(self, key)


USAGE = "usage: dsl.py [generate|run] KEY"

def usage():
    import sys
    print(USAGE)
    sys.exit(1)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        usage()

    action = sys.argv[1]
    key = sys.argv[2]

    if action == "generate":
        g = Generator(lambda x : print(hex(x)))
    elif action == "run":
        g = Interpreter()
    else:
        usage()

    push_str(g, "}")

    random_noise(g, 20)

    encode_key(g, key);

    random_noise(g, 10)

    push_str(g, "ihacku{")

    for x in range(len("ihacku({})".format(key))):
        g.bprint()
