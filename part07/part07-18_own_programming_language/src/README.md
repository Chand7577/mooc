# Custom Programming Language Interpreter

This is a custom programming language interpreter built in Python, inspired by assembly language. It provides the ability to parse and execute a simple set of instructions, such as variable manipulation, arithmetic operations, conditional jumps, and printing outputs. The interpreter allows users to define labels for jumps and conditionals, making it possible to write simple programs and loops. 

This project is a learning exercise in creating a minimalistic interpreter, focusing on the core principles of language parsing, execution, and control flow management.

## Features
- **Variable Manipulation:** Supports creating, setting, and updating variables.
- **Arithmetic Operations:** Includes basic mathematical operations like addition, subtraction, multiplication, and division.
- **Control Flow:** Implement control structures such as conditional jumps, allowing basic program flow control and loops.
- **Output:** Print the values of variables or static strings to the console.


# Example Program

```assembly
; This is a simple program
SET A 5          ; Set A to 5
SET B 10         ; Set B to 10
ADD A B          ; Add B to A, result stored in A
PRINT A          ; Print the value of A (should print 15)
