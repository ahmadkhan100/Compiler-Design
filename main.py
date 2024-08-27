import subprocess
from symbol_table import symbol_table
from tac_generator import tac_code
from x86_generator import generate_x86

def main():
    # Step 1: Lexing and Parsing (Yacc + Lex)
    subprocess.run(["bison", "-d", "parser.y"])
    subprocess.run(["flex", "lexer.l"])
    subprocess.run(["gcc", "parser.tab.c", "lex.yy.c", "-o", "compiler", "-lfl", "-ly"])
    
    # Step 2: Execute the compiled parser to generate TAC
    subprocess.run(["./compiler", "<", "input.java"])
    
    # Step 3: Generate x86 assembly code from TAC
    x86_code = generate_x86(tac_code)
    
    # Step 4: Write x86 code to an assembly file
    with open("output.asm", "w") as f:
        f.write(x86_code)
    
    # Step 5: Assemble and link to create executable
    subprocess.run(["nasm", "-f", "elf32", "output.asm"])
    subprocess.run(["ld", "-m", "elf_i386", "-o", "output", "output.o"])

if __name__ == "__main__":
    main()
