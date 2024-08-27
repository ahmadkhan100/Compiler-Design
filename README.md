# Java to x86 Compiler

## Overview
This project implements a simple compiler that translates a subset of Java code into x86 assembly code. The project is built using Lex (Flex) for lexical analysis, Yacc (Bison) for parsing, and Python for intermediate code generation and final assembly code generation.

## Project Structure
- `lexer.l`: Lexical analyzer definition file.
- `parser.y`: Syntax analyzer definition file using Yacc.
- `symbol_table.py`: Python script managing the symbol table.
- `tac_generator.py`: Python script for generating three-address code (TAC).
- `x86_generator.py`: Python script for converting TAC to x86 assembly code.
- `main.py`: Main script to run the entire compilation process.
- `Makefile`: Build automation script.
- `README.md`: Project documentation.

## How to Build and Run
1. **Build the Compiler:**
   ```bash
   make

   Compile a Java Program:

Place your Java code in an input.java file.
Run the compiler:
```bash
python3 main.py





