# Reflecto
### An esolang all about shiny mirrors   
    
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
    &	Pop the top value and store it in a register (if you want to add registers).
    ~	Pop the top value and push it back as a negative.

    +	Pop the top two values, add them, and push the result.
    -	Pop the top two values, subtract the second from the first, and push the result.
    *	Pop the top two values, multiply them, and push the result.
    :	Pop the top two values, divide the first by the second, and push the result.
    %	Pop the top two values, compute the modulo, and push the result.
    =	Pop the top two values, push 1 if they are equal, otherwise push 0.
    >	Pop the top two values, push 1 if the first is greater, otherwise push 0.
    <	Pop the top two values, push 1 if the first is smaller, otherwise push 0.

    @	Pop the top value and output it as a character (e.g., ASCII).
    #	Pop the top value and output it as a number.
    ,	Read a character from input and push its ASCII value onto the stack.
    .	Read a number from input and push it onto the stack.

    !	Pop the top value; if it’s 0, skip the next command.

    E	End program execution.
