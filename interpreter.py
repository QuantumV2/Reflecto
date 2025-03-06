
import random
import sys
class Interpreter:

    def __init__(self):
        self.stack = []
        self.ip = [0,0]
        self.dir = [1,0]
        self.is_running = False
        self.commands = {
            "/": self.do_reflect_slash,
            "\\": self.do_reflect_back_slash,
            "_": self.do_reflect_horizontal,
            "|": self.do_reflect_vertical,
            "?": self.do_reflect_random,

            "$": self.do_pop,
            "d": self.do_dup,
            "s": self.do_swap,
            "r": self.do_reverse,
            "b": self.do_size,
            "~": self.do_negate,

            "+": self.do_add,
            "-": self.do_sub,
            "*": self.do_mul,
            ":": self.do_div,
            "%": self.do_mod,
            "=": self.do_equ,
            ">": self.do_gts,
            "<": self.do_lts,

            "@": self.do_chrprint,
            "#": self.do_numprint,
            ",": self.do_inputchr,
            ".": self.do_inputnum,

            "!": self.do_skip,

            "E": self.do_end,
        }
    def run(self, code):
        sys.set_int_max_str_digits(0)
        self.is_running = True
        while self.is_running:
            self.ip[0], self.ip[1] = self.ip[0] % len(code), self.ip[1] % len(code[0])
            
            inst = code[self.ip[0]][self.ip[1]]
            if inst.isnumeric():
                self.stack.append(int(inst))
            if inst in self.commands:
                self.commands[inst]()
            self.move(self.dir)
            #print(inst, self.ip, self.stack)

    def util_popstack(self):
        if len(self.stack) <= 0:
            return 0
        return self.stack.pop()
    def util_peekstack(self, val):
        if len(self.stack) <= 0 or len(self.stack) < val - 1:
            return 0
        return self.stack[val]
    

    def do_reflect_slash(self):
            self.dir[0], self.dir[1] = -self.dir[1], -self.dir[0]
    def do_reflect_back_slash(self):
        self.dir[0], self.dir[1] = self.dir[1], self.dir[0]
    def do_reflect_horizontal(self):
        self.dir[1] = -self.dir[1]
    def do_reflect_vertical(self):
        self.dir[0] = -self.dir[0]
    def do_reflect_random(self):
        self.dir = random.choice([(0,1), (1,0), (0,-1), (-1,0)])
    def do_pop(self):
        self.util_pop_stack()
    def do_dup(self):
        val = self.util_peekstack(-1)
        self.stack.append(val)
    def do_swap(self):
        a = self.util_popstack()
        b = self.util_popstack()
        self.stack.append(a)
        self.stack.append(b)
    def do_reverse(self):
        if not self.stack:
            return
        self.stack = self.stack[::-1]
    def do_negate(self):
        val = self.util_pop_stack()
        val *= -1
        self.stack.append(val)


    def do_add(self):
        self.stack.append( self.util_popstack() + self.util_popstack())
    def do_sub(self):
        a = self.util_popstack()
        b = self.util_popstack()
        self.stack.append( b - a)
    def do_mul(self):
        self.stack.append(self.util_popstack() * self.util_popstack())
    def do_div(self):
        a = self.util_popstack()
        if a  == 0:
            raise ZeroDivisionError("Operand A is 0")
        b = self.util_popstack()
        self.stack.append( b // a)
    def do_mod(self):
        a = self.util_popstack()
        b = self.util_popstack()
        self.stack.append( b % a)
    def do_equ(self):
        a = self.util_popstack()
        b = self.util_popstack()
        self.stack.append( int(b == a) )
    def do_gts(self):
        a = self.util_popstack()
        b = self.util_popstack()
        self.stack.append( int(b > a) )
    def do_lts(self):
        a = self.util_popstack()
        b = self.util_popstack()
        self.stack.append( int(b < a) )


    def do_chrprint(self):
        print(chr(self.util_popstack()), end='')
    def do_numprint(self):
        print(self.util_popstack(), end='')

    def do_inputchr(self):
        inp = input()
        for char in inp[::-1]:
            self.stack.append(ord(char))
    def do_inputnum(self):
        inp = int(input())
        self.stack.append(inp)

    def do_skip(self):
        if self.util_popstack() == 0:
            self.move(self.dir)
        else:
            return
    def do_end(self):
        self.is_running = False
    def do_size(self):
        self.stack.append(len(self.stack))

    def move(self, b: tuple):
        self.ip[0] += self.dir[0]
        self.ip[1] += self.dir[1]