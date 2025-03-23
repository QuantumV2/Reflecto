# Reflecto
### An esolang all about shiny mirrors   
## Overview
Reflecto is an esoteric 2d stack-based programming language inspired Befunge and ><>. Each instruction is a single symbol on a text file that performs operations like reflecting the instruction pointer, manipulating stack values, and basic arithmetic.

The program counter is always moving, starting out moving to the right from the top left corner and the direction being able to be altered by instructions.

There is also a register allowing for temporary data storage.

## Usage
    python main.py "examples/factorial.refl"
## Instructions
    Mirrors (/,\,_,|)   The most important part of the language, mirrors the instruction pointer like you think a mirror would (Moving right into a / mirror? You get launched up. Moving right into a | mirror? You bounce off off it!)

    0-9	Push a number onto the stack (e.g., 5 pushes 5).
    $	Pop the top value from the stack and discard it.
    d	Duplicate the top value on the stack.
    s	Swap the top two values on the stack.
    r	Reverse stack.
    b	Push stack size onto the stack

    +	Pop the top two values, add them, and push the result.
    -	Pop the top two values, subtract the second from the first, and push the result.
    *	Pop the top two values, multiply them, and push the result.
    :	Pop the top two values, divide the first by the second, and push the result.
    %	Pop the top two values, compute the modulo, and push the result.
    =	Pop the top two values, push 1 if they are equal, otherwise push 0.
    >	Pop the top two values, push 1 if the first is greater, otherwise push 0.
    <	Pop the top two values, push 1 if the first is smaller, otherwise push 0.

    &   Pop and store to register 
    ~   Get value from register and push to the stack

    @	Pop the top value and output it as a character.
    #	Pop the top value and output it as a number.
    ,	Read a character from input and push its Unicode value onto the stack.
    .	Read a number from input and push it onto the stack.

    !	Pop the top value; if it’s 0, skip the next command.

    E	End program execution.
