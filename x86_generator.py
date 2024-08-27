x86_code = []

def generate_x86(tac_code):
    for line in tac_code:
        parts = line.split()
        if "=" in line and "+" in line:
            x86_code.append(f"mov eax, {parts[2]}")
            x86_code.append(f"add eax, {parts[4]}")
            x86_code.append(f"mov {parts[0]}, eax")
        elif "=" in line:
            x86_code.append(f"mov {parts[0]}, {parts[2]}")
        elif "if" in line:
            x86_code.append(f"cmp {parts[1]}, 0")
            x86_code.append(f"jne {parts[-1]}")
        elif "goto" in line:
            x86_code.append(f"jmp {parts[1]}")
        elif ":" in line:
            x86_code.append(f"{parts[0]}")

    return "\n".join(x86_code)
