temp_count = 0
tac_code = []

def new_temp():
    global temp_count
    temp = f"t{temp_count}"
    temp_count += 1
    return temp

def generate_assignment(identifier, expr):
    tac_code.append(f"{identifier} = {expr}")
    return identifier

def generate_addition(expr1, expr2):
    temp = new_temp()
    tac_code.append(f"{temp} = {expr1} + {expr2}")
    return temp

def generate_number(value):
    return str(value)

def generate_if_statement(condition, body):
    label = new_label()
    tac_code.append(f"if {condition} goto {label}")
    tac_code.append(body)
    tac_code.append(f"{label}:")

def generate_while_statement(condition, body):
    start_label = new_label()
    end_label = new_label()
    tac_code.append(f"{start_label}:")
    tac_code.append(f"if not {condition} goto {end_label}")
    tac_code.append(body)
    tac_code.append(f"goto {start_label}")
    tac_code.append(f"{end_label}:")
