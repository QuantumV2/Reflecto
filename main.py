import interpreter
import sys

def read_code(filename):
    with open(filename, 'r') as file:
        lines = [line.rstrip('\n') for line in file]
        max_length = max(len(line) for line in lines)
        padded_lines = [line.ljust(max_length, ' ') for line in lines]
        height = len(padded_lines)
        width = max_length
        code = [[padded_lines[y][x] for y in range(height)] for x in range(width)]
        return code

interp = interpreter.Interpreter()
code = read_code(sys.argv[1])
interp.run(code)