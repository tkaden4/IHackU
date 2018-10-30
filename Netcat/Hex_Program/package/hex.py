import random
import socket
import sys

class Hex_Challenge:
    row_f = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    row_l = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    row_a = [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1]
    row_g = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    row_space = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_i = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    row_s = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    row_h = [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1]
    row_e = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    row_x = [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1]
    numtostring = { 0 : "0", 1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9", 10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F", }
    problem_type = { 0 : "addition", 1 : "subtraction", 2 : "multiplication", }
    min_length = 5
    fixedlength = 8

    def __init__(self, alpha_len=5, height=9, flag_len=3, symbol=15):
        self.hextable = []
        self.row_index = -1
        #funtion_type = { "addition" : plus(), "subtraction" : minus(), "multiplication" : multiply(), }
        self.answer_hex_string = []
        self.random_hex_string = []
        self.table_f = []
        self.table_l = []
        self.table_a = []
        self.table_g = []
        self.table_space = []
        self.table_i = []
        self.table_s = []
        self.table_h = []
        self.table_e = []
        self.table_x = []

        self.length = alpha_len
        self.height = height
        self.flaglength = flag_len
        self.symbol = symbol
        
        self.init_tab_r(self.table_f, self.row_f, self.symbol, self.length, self.height)
        self.init_tab_r(self.table_l, self.row_l, self.symbol, self.length, self.height)
        self.init_tab_c(self.table_a, self.row_a, self.symbol, self.length, self.height)
        self.init_tab_c(self.table_g, self.row_g, self.symbol, self.length, self.height)
        self.init_tab_r(self.table_space, self.row_space, self.symbol, self.length, self.height)
        self.init_tab_r(self.table_i, self.row_i, self.symbol, self.length, self.height)
        self.init_tab_c(self.table_s, self.row_s, self.symbol, self.length, self.height)
        self.init_tab_c(self.table_h, self.row_h, self.symbol, self.length, self.height)
        self.init_tab_r(self.table_e, self.row_e, self.symbol, self.length, self.height)
        self.init_tab_c(self.table_x, self.row_x, self.symbol, self.length, self.height)
        self.assign_hextable()

    def print_hextable(self, flaglen=3, fixedlen=8, length=5, height=9):
        for i in range(height):
            for j in range(flaglen+fixedlen):
                for k in range(length):
                    print(self.numtostring[self.hextable[i][j][k]]),
                print("0"),
            print("")

    def print_hex_row(self, hex_row):
        for i in range(len(hex_row)):
            print(self.numtostring[hex_row[i]]),
        print("")

    def create_hex_string(self, hex_row):
        hex_string = ""
        hex_list = []
        for i in range(len(hex_row)):
            hex_list.append(self.numtostring[hex_row[i]])
            #hex_string += numtostring[hex_row[i]]
        hex_string = ''.join(hex_list)
        #print hex_string
        return hex_string
    
    def print_rows(self, socket, bufferSize, height=9):
        all_correct = False
        key = -1
        for i in range(height):
            self.row_index = i
            for j in range(self.flaglength+self.fixedlength):
                self.hextable[i][j].append(0)
            self.reformat_hex_string(self.row_index, self.flaglength, self.fixedlength, self.length)
            hex_string = self.create_hex_string(self.answer_hex_string)
            answer = hex_string
            print("Answer to the question is: " + answer + ".")
            key = random.randint(0,1)
            if self.problem_type[key] == "addition":
                self.plus(self.row_index, self.length)
            elif self.problem_type[key] == "subtraction":
                self.minus(self.row_index, self.length) 
            #self.funtion_type[problem_type[key]](self.row_index, self.length)
            if key == 0:
                hex_string = self.create_hex_string(self.answer_hex_string)
                socket.send(bytearray("Problem #" + str(i+1) + ":                           " + 
                                    hex_string + "\r\n", "UTF-8")) 
    
                hex_string = self.create_hex_string(self.random_hex_string)
                socket.send(bytearray("Please add the following hexadecimal: " + 
                           hex_string + "\r\n", "UTF-8"))
    
            elif key == 1:
                hex_string = self.create_hex_string(self.answer_hex_string)
                if len(self.answer_hex_string) == 67:
                    socket.send(bytearray("Problem #" + str(i+1) + ":                               " +
                           hex_string + "\r\n", "UTF-8"))

                elif len(self.answer_hex_string) == 66:
                    socket.send(bytearray("Problem #" + str(i+1) + ":                                 " +
                           hex_string + "\r\n", "UTF-8"))
    
                hex_string = self.create_hex_string(self.random_hex_string)
                socket.send(bytearray("Please subtract the following hexadecimal: " +
                                      hex_string + "\r\n", "UTF-8"))
    
            socket.send(bytearray("Answer: ", "UTF-8"))
            del self.answer_hex_string[:]
            del self.random_hex_string[:]
            try:
                while True:
                    chunk = socket.recv(bufferSize)
                    chunk = chunk.decode("utf-8")
                    chunk = chunk[:-1]
                    #print("User's answer is " + chunk + ".")
                    #print(chunk)
                    if(answer == chunk):
                        all_correct = True
                        socket.send(bytearray("Correct!\r\n\r\n", "UTF-8"))
                        break
                    else:
                        all_correct = False
                        socket.send(bytearray("Incorrect, please give the correct answer.\r\n", "UTF-8"))
                        socket.send(bytearray(">", "UTF-8"))

            except IOError as e1:
                all_correct = False
                #print("Received keyboard interrupt from the user.")
                break
    
        if all_correct:
            socket.send(bytearray("Congratulation! All problems has been solved, did you manage to find the cookie?\r\n", "UTF-8"))
            socket.send(bytearray("Hint: it's in the answer(s)", "UTF-8"))
        else:
            return -1

        return 1

    def generate_hex_string(self, code, row_index, length):
        for i in range(len(self.hextable[row_index]) * (length + 1)):
            random_hex = random.randint(0, 15)
            if code == 0 and i == 0:
                random_hex = random.randint(0, 14)
            self.random_hex_string.append(random_hex)
        #print("random hex string")
        #print_hex_row(random_hex_string)
        #print

    def reformat_hex_string(self, row_index, flaglen=3, fixedlen=8, length=5):
        for i in range(flaglen+fixedlen):
            for j in range(length+1):
                self.answer_hex_string.append(self.hextable[row_index][i][j])
        #print("reformat string")
        #self.print_hex_row(self.answer_hex_string)
        #print
    
    def plus(self, row_index, length):
        code = 0
        self.generate_hex_string(code, row_index, length)
        for i in range((len(self.hextable[row_index]) * (length + 1)) - 1, -1, -1):
            if self.answer_hex_string[i] >= self.random_hex_string[i]:
                self.answer_hex_string[i] = self.answer_hex_string[i] - self.random_hex_string[i]
            elif self.answer_hex_string[i] < self.random_hex_string[i]:
                self.answer_hex_string[i-1] = self.answer_hex_string[i-1] - 1
                self.answer_hex_string[i] = self.answer_hex_string[i] + 16
                self.answer_hex_string[i] = self.answer_hex_string[i] - self.random_hex_string[i]
        #print("answer_hex_string")
        #print_hex_row(answer_hex_string)
        #print
    
    def minus(self, row_index, length):
        code = 1
        self.generate_hex_string(code, row_index, length)
        place_holder = -1
        for i in range((len(self.hextable[row_index]) * (length + 1)) - 1, -1, -1):
            place_holder = self.answer_hex_string[i] + self.random_hex_string[i]
            if i == 0 and place_holder > 15:
                self.answer_hex_string[i] = place_holder - 16
                self.answer_hex_string.insert(0,1)
            elif place_holder > 15:
                self.answer_hex_string[i] = place_holder - 16
                self.answer_hex_string[i-1] = self.answer_hex_string[i-1] + 1
            else:
                self.answer_hex_string[i] = place_holder

    def multiply(self, row_index, length):
        pass

    #funtion_type = { "addition" : plus, "subtraction" : minus, "multiplication" : multiply, }

    def assign_hextable(self, height=9):
        for i in range(height):
            self.hextable.append([])
            self.hextable[i].append(self.table_f[i])
            self.hextable[i].append(self.table_l[i])
            self.hextable[i].append(self.table_a[i])
            self.hextable[i].append(self.table_g[i])
            self.hextable[i].append(self.table_space[i])
            self.hextable[i].append(self.table_i[i])
            self.hextable[i].append(self.table_s[i])
            self.hextable[i].append(self.table_space[i])
            self.hextable[i].append(self.table_h[i])
            self.hextable[i].append(self.table_e[i])
            self.hextable[i].append(self.table_x[i])

    def init_tab_r(self, table, row, symbol, length=5, height=9):
        assign_value = 9
        for i in range(height):
            table.append([])
            for j in range(length):
                if j + 1 > self.min_length:
                    if assign_value < 5:
                        assign_value = random.randint(0,1)
                    table[i].append(assign_value)
                    break
                assign_value = row[i*self.min_length+j] * symbol
                if assign_value < 1:
                    assign_value = random.randint(0,1)
                table[i].append(assign_value)

    def init_tab_c(self, table, row, symbol, length=5, height=9):
        assign_value = 9
        for i in range(height):
            table.append([])
            for j in range(length):
                if length > self.min_length and j == (length / 2 + 1):
                    if assign_value < 5:
                        assign_value = random.randint(0,1)
                    table[i].append(assign_value)
                elif j + 1 > self.min_length:
                    break
                assign_value = row[i*self.min_length+j] * symbol
                if assign_value < 1:
                    assign_value = random.randint(0,1)
                table[i].append(assign_value)

    def print_table(self, table):
        for i in range(len(table)):
            print("the " + str(i) + " row is " + str(table[i]))
    
